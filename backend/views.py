
from django.shortcuts import render
from django.http import HttpResponse
from .models import Story
from rest_framework import generics, status
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .serializers import StorySerializer
from apscheduler.schedulers.background import BackgroundScheduler
from backend.task import fetch_top_stories_and_comments


def start(request):
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_top_stories_and_comments, "interval", minutes=1)
    scheduler.start()

    stories = Story.objects.all()

    return HttpResponse(stories)


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100

class LatestStoriesView(generics.ListAPIView):
    queryset = Story.objects.all().order_by('-time')  # Get latest 10 stories
    serializer_class = StorySerializer
    pagination_class = CustomPageNumberPagination

class FilteredStoriesView(generics.ListAPIView):
    serializer_class = StorySerializer
    filter_backends = [SearchFilter]
    search_fields = ['title']
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        filter_param = self.request.query_params.get('filter', '').lower()

        if filter_param == 'ask':
            return Story.objects.filter(title__icontains='Ask Hn') | Story.objects.filter(title__icontains='ask hn')
        elif filter_param == 'show':
            return Story.objects.filter(title__icontains='Show Hn') | Story.objects.filter(title__icontains='show hn')
        elif filter_param == 'job':
            return Story.objects.filter(title__icontains='hiring')

        return Story.objects.none()

class StorySearchView(generics.ListAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    filter_backends = [SearchFilter]
    pagination_class = CustomPageNumberPagination
    search_fields = ['title', 'text']  # Fields to search through



class StoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer

    def perform_destroy(self, instance):
        if instance.fetched == False:
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail": "Cannot delete items from Hacker News"}, status=status.HTTP_403_FORBIDDEN)

    def perform_update(self, serializer):
        if serializer.instance.fetched == False:
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"detail": "Cannot update items from Hacker News"}, status=status.HTTP_403_FORBIDDEN)



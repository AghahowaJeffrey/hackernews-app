
from django.shortcuts import render, redirect
from .models import Story
from rest_framework import generics, status
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .serializers import StorySerializer


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class FilterByScoreView(generics.ListAPIView):
    serializer_class = StorySerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        return Story.objects.all().order_by('-score')

class LatestStoriesView(generics.ListAPIView):
    queryset = Story.objects.all().order_by('-time')  # Get latest stories
    serializer_class = StorySerializer
    pagination_class = CustomPageNumberPagination
    
class TopStoriesView(generics.ListAPIView):
    queryset = Story.objects.all().order_by('score')  # Get top stories
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
            return Story.objects.filter(title__icontains='Ask HN') | Story.objects.filter(title__icontains='ask hn')
        elif filter_param == 'show':
            return Story.objects.filter(title__icontains='Show HN') | Story.objects.filter(title__icontains='show hn')
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
        if instance.fetched:
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_update(self, serializer):
        if serializer.instance.fetched == False:
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"detail": "Cannot update items from Hacker News"}, status=status.HTTP_403_FORBIDDEN)



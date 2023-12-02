
from django.shortcuts import render
from apscheduler.schedulers.background import BackgroundScheduler
from backend.task import fetch_top_stories_and_comments
from .models import Story
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from django.http import JsonResponse, HttpResponse
from django.views import View
from rest_framework import generics, status
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .serializers import StorySerializer
from .task import sync_fetch_top_stories_and_comments
from django.http import JsonResponse
from django.views import View
import asyncio


async def fetch_stories_and_comments_async():
    await fetch_top_stories_and_comments()

class FetchStoriesCommentsView(View):
    async def get(self, request):
        # Call the asynchronous function within an async view
        await fetch_top_stories_and_comments()
        return JsonResponse({'message': 'Fetching stories and comments completed.'})

# def task_status(request):
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(fetch_stories_and_comments_async, 'interval', seconds=10)
#     scheduler.start()

#     stories = Story.objects.all()

    # return HttpResponse(stories)





# class FetchStoriesCommentsView(View):
#     async def get(self, request):
#         await fetch_stories_and_comments_async()
#         return JsonResponse({'message': 'Fetching stories and comments completed.'})

# async def schedule_background_task():
#     while True:
#         await asyncio.sleep(60)  # Wait for 60 seconds
#         await fetch_stories_and_comments_async()

# def start_background_task():
#     asyncio.create_task(schedule_background_task())

# def task_status(request):
#     start_background_task()
#     stories = Story.objects.all()
#     return HttpResponse(stories)



class CustomPageNumberPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100

class LatestStoriesView(generics.ListAPIView):
    queryset = Story.objects.all().order_by('-time')[:10]  # Get latest 10 stories
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
        if instance.created_in_api:
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail": "Cannot delete items from Hacker News"}, status=status.HTTP_403_FORBIDDEN)

    def perform_update(self, serializer):
        if serializer.instance.created_in_api:
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"detail": "Cannot update items from Hacker News"}, status=status.HTTP_403_FORBIDDEN)


 




# class FetchStoriesCommentsView(View):
#     async def get(self, request):
#         await fetch_top_stories_and_comments()
#         return JsonResponse({'message': 'Fetching stories and comments completed.'})

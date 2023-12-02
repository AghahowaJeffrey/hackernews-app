
from django.shortcuts import render
from apscheduler.schedulers.background import BackgroundScheduler
from backend.task import fetch_top_stories_and_comments
from .models import Story
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from django.http import JsonResponse, HttpResponse
from django.views import View
from rest_framework import generics
from rest_framework.filters import SearchFilter
from .models import Story
from .serializers import StorySerializer

async def fetch_stories_and_comments_async():
    await fetch_top_stories_and_comments()

class FetchStoriesCommentsView(View):
    async def get(self, request):
        await fetch_stories_and_comments_async()
        return JsonResponse({'message': 'Fetching stories and comments completed.'})

async def schedule_background_task():
    while True:
        await asyncio.sleep(60)  # Wait for 60 seconds
        await fetch_stories_and_comments_async()

def start_background_task():
    asyncio.create_task(schedule_background_task())

def task_status(request):
    start_background_task()
    stories = Story.objects.all()
    return HttpResponse(stories)

class LatestStoriesView(generics.ListAPIView):
    queryset = Story.objects.all().order_by('-time')[:10]  # Get latest 10 stories
    serializer_class = StorySerializer

class FilteredStoriesView(generics.ListAPIView):
    serializer_class = StorySerializer
    filter_backends = [SearchFilter]
    search_fields = ['title']

    def get_queryset(self):
        filter_param = self.request.query_params.get('filter', '').lower()

        if filter_param == 'ask':
            return Story.objects.filter(title__icontains='Ask Hn') | Story.objects.filter(title__icontains='ask hn')
        elif filter_param == 'show':
            return Story.objects.filter(title__icontains='Show Hn') | Story.objects.filter(title__icontains='show hn')
        elif filter_param == 'job':
            return Story.objects.filter(url__isnull=True)

        return Story.objects.none()

class StorySearchView(generics.ListAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'text']  # Fields to search through





# from django.http import JsonResponse
# from django.views import View
# import asyncio


# def task_status(request):
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(fetch_top_stories_and_comments, 'interval', seconds=10)
#     scheduler.start()

#     stories = Story.objects.all()

#     return HttpResponse(stories)


# class FetchStoriesCommentsView(View):
#     async def get(self, request):
#         await fetch_top_stories_and_comments()
#         return JsonResponse({'message': 'Fetching stories and comments completed.'})

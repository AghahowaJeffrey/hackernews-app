from django.http import HttpResponse
from django.shortcuts import render
from apscheduler.schedulers.background import BackgroundScheduler
from backend.task import fetch_top_stories_and_comments
from .models import Story
from django.http import JsonResponse
from django.views import View
import asyncio


# def task_status(request):
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(fetch_top_stories_and_comments, 'interval', seconds=10)
#     scheduler.start()

#     stories = Story.objects.all()

#     return HttpResponse(stories)


class FetchStoriesCommentsView(View):
    async def get(self, request):
        await fetch_top_stories_and_comments()
        return JsonResponse({'message': 'Fetching stories and comments completed.'})
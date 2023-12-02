

import asyncio
import httpx
from datetime import datetime
from .models import Story, Comment
from asgiref.sync import sync_to_async

async def fetch_comment(session, story_data, comment_id):
    item_url = f'https://hacker-news.firebaseio.com/v0/item/{comment_id}.json?print=pretty'
    response = await session.get(item_url)
    if response.status_code == 200:
        comment_data = response.json()
        parent_story_instance, _ = await sync_to_async(Story.objects.get_or_create)(
            story_id=story_data['id'],
            defaults={
                'title': story_data.get('title', ''),
                'by': story_data.get('by', ''),
                'descendants': story_data.get('descendants', 0),
                'score': story_data.get('score', 0),
                'text': story_data.get('text', ''),
                'time': datetime.fromtimestamp(story_data.get('time', 0)),
                'type': story_data.get('type', 'story'),
                'url': story_data.get('url'),
                'kid': comment_data
            }
        )

        await sync_to_async(Comment.objects.update_or_create)(
            comment_id=comment_data['id'],
            defaults={
                'parent_story': parent_story_instance,
                'by': comment_data.get('by', ''),
                'text': comment_data.get('text', ''),
                'time': datetime.fromtimestamp(comment_data.get('time', 0)),
                'type': comment_data.get('type', 'comment'),
            }
        )

async def fetch_story_and_comments(session, story_id):
    item_url = f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json?print=pretty'
    response = await session.get(item_url)
    if response.status_code == 200:
        story_data = response.json()
        await sync_to_async(Story.objects.update_or_create)(
            story_id=story_data['id'],
            defaults={
                'title': story_data.get('title', ''),
                'by': story_data.get('by', ''),
                'descendants': story_data.get('descendants', 0),
                'score': story_data.get('score', 0),
                'text': story_data.get('text', ''),
                'time': datetime.fromtimestamp(story_data.get('time', 0)),
                'type': story_data.get('type', 'story'),
                'url': story_data.get('url')
            }
        )

        if 'kids' in story_data:
            comment_tasks = []
            for comment_id in story_data['kids'][:10]:
                comment_tasks.append(fetch_comment(session, story_data, comment_id))

            await asyncio.gather(*comment_tasks)

async def fetch_top_stories_and_comments():
    top_stories_url = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
    semaphore = asyncio.Semaphore(100)
    async with httpx.AsyncClient(http2=True, limits=httpx.Limits(max_keepalive_connections=100)) as session:
        async with semaphore:
            response = await session.get(top_stories_url)
            if response.status_code == 200:
                top_stories_ids = response.json()

                story_tasks = []
                for story_id in top_stories_ids[:10]:
                    story_tasks.append(fetch_story_and_comments(session, story_id))

                await asyncio.gather(*story_tasks)
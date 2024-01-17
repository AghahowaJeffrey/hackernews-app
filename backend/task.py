
import requests
from datetime import datetime, timedelta
from .models import Story, Comment
from apscheduler.schedulers.background import BackgroundScheduler



def fetch_comment(story_data, comment_id):
    item_url = f'https://hacker-news.firebaseio.com/v0/item/{comment_id}.json?print=pretty'
    response = requests.get(item_url)
    if response.status_code == 200:
        comment_data = response.json()
        parent_story_instance, _ = Story.objects.get_or_create(
            defaults={
                'title': story_data.get('title', ''),
                'fetched': True,
                'by': story_data.get('by', ''),
                'descendants': story_data.get('descendants', 0),
                'score': story_data.get('score', 0),
                'text': story_data.get('text', ''),
                'time': datetime.fromtimestamp(story_data.get('time', 0)),
                'type': story_data.get('type', 'story'),
                'url': story_data.get('url'),

            }
        )

        Comment.objects.update_or_create(
            comment_id=comment_data['id'],
            defaults={
                'parent_story': parent_story_instance,
                'by': comment_data.get('by', ''),
                'text': comment_data.get('text', ''),
                'time': datetime.fromtimestamp(comment_data.get('time', 0)),
                'type': comment_data.get('type', 'comment'),
            }
        )

def fetch_story(story_id):
    item_url = f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json?print=pretty'
    response = requests.get(item_url)
    if response.status_code == 200:
        story_data = response.json()
        Story.objects.update_or_create(
            defaults={
                'title': story_data.get('title', ''),
                'fetched': True,
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
            for comment_id in story_data['kids']:
                fetch_comment(story_data, comment_id)

def fetch_top_stories_and_comments():
    top_stories_url = 'https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty'
    
    response = requests.get(top_stories_url)
    if response.status_code == 200:
        top_stories_ids = response.json()

        for story_id in list(reversed(top_stories_ids[:100])):
            fetch_story(story_id)

def start_task():
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_top_stories_and_comments, "date", run_date=datetime.now() + timedelta(minutes=1), max_instances=1)
    scheduler.start()

def start_interval():
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_top_stories_and_comments, "interval", minutes=5)
    scheduler.start()





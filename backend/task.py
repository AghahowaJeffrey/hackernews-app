
import requests
from datetime import datetime
from .models import Story, Comment

def fetch_comment(story_data, comment_id):
    item_url = f'https://hacker-news.firebaseio.com/v0/item/{comment_id}.json?print=pretty'
    response = requests.get(item_url)
    if response.status_code == 200:
        comment_data = response.json()
        parent_story_instance, _ = Story.objects.get_or_create(
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

def fetch_story_and_comments(story_id):
    item_url = f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json?print=pretty'
    response = requests.get(item_url)
    if response.status_code == 200:
        story_data = response.json()
        Story.objects.update_or_create(
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
            for comment_id in story_data['kids'][:10]:
                fetch_comment(story_data, comment_id)

def fetch_top_stories_and_comments():
    top_stories_url = 'https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty'
    
    response = requests.get(top_stories_url)
    if response.status_code == 200:
        top_stories_ids = response.json()

        for story_id in top_stories_ids[:100]:
            fetch_story_and_comments(story_id)








            # news_base_detail_url = "https://hacker-news.firebaseio.com/v0/item/"
# news_urls = {
#     "top": "https://hacker-news.firebaseio.com/v0/topstories.json",
#     "show": "https://hacker-news.firebaseio.com/v0/showstories.json",
#     "ask": "https://hacker-news.firebaseio.com/v0/askstories.json",
#     "job": "https://hacker-news.firebaseio.com/v0/jobstories.json"
# }

# def fetch_news(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()

# def get_results_keys(news_detail):
#     type = news_detail.get("type")
#     story_id = str(news_detail.get("id"))
#     by = news_detail.get("by")
#     time = make_aware(dt.datetime.fromtimestamp(news_detail.get("time")))
#     url = news_detail.get("url")
#     title = news_detail.get("title")
#     text = news_detail.get("text")
#     score = news_detail.get("score", 0)
#     kids = list(reversed(sorted(news_detail.get("kids", []))))
#     parent = news_detail.get("parent")
#     parts = news_detail.get("parts", [])
#     vals = {
#         "type": type,
#         "story_id": story_id,
#         "by": by,
#         "time": time,
#         "url": url,
#         "title": title,
#         "text": text,
#         "score": score,
#         "fetched": True
#     }
#     return vals, (kids, parent, parts)

# def fetch_children(type, kids, par, obj, sm_n=5, gch=False):
#     if not kids:
#         return

#     for com_id in kids:
#         sing_com = fetch_news(f"{news_base_detail_url}{com_id}.json")
#         com_lte = get_results_keys(sing_com)
#         real_com = com_lte[0]
#         s_type = real_com["type"]
#         s_kids = com_lte[-1][0]
#         s_par = None
#         if type == "story":
#             s_par = obj.objects.create(**real_com, parent_story=par)
#         if gch:
#             pass

# def save_to_db(news_ids, num=100):
#     news_ids = list(reversed(sorted(news_ids)))[:num]
#     if news_ids:
#         exists = Story.objects.filter(story_id=news_ids[0]).exists()
#         if exists:
#             return
#     else:
#         return

#     for i in news_ids:
#         news_detail = fetch_news(f"{news_base_detail_url}{i}.json")
#         ite = get_results_keys(news_detail)
#         news_vals = ite[0]
#         kids = ite[-1][0]
#         parts = ite[-1][-1]
#         type = news_vals["type"]
#         try:
#             par = Story.objects.create(**news_vals)
#             if kids and type == "story":
#                 fetch_children(type, kids, par, Comment)
#         except Exception as e:
#             print(e, "failed to fetch")
#             pass

# def scheduled_tasks1():
#     print("Task started")
#     all_news_ids = []
#     for category, url in news_urls.items():
#         news_ids = fetch_news(url)
#         all_news_ids.extend(news_ids)

#     print(f'len(all_news_ids) = {len(all_news_ids)}')
#     all_news_ids = set(all_news_ids)
#     print(f'after len(all_news_ids) = {len(all_news_ids)}')

#     save_to_db(all_news_ids)
#     print("Task ran")




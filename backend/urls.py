
from django.contrib import admin
from django.urls import path
from backend import views
from .views import FetchStoriesCommentsView
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('task-status/', views.task_status),
# ]




urlpatterns = [
    path('admin/', admin.site.urls),
    path('fetch-stories-comments/', FetchStoriesCommentsView.as_view(), name='fetch-stories-comments'),
    # Other URL patterns...#
]
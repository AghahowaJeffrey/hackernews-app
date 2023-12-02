
from django.contrib import admin
from django.urls import path, include
from backend import views
from .views import FetchStoriesCommentsView, LatestStoriesView, FilteredStoriesView, StorySearchView, StoryDetailView


urlpatterns = [
    path('fetch-stories-comments/', FetchStoriesCommentsView.as_view(), name='fetch-stories-comments'),
    path('admin/', admin.site.urls),
    # path('fetch-stories-comments/', views.task_status, name='fetch-stories-comments'),
    path('api-auth/', include('rest_framework.urls')),
    path('latest-stories/', LatestStoriesView.as_view(), name='latest-stories'),
    path('filtered-stories/', FilteredStoriesView.as_view(), name='filtered-stories'),
    path('story-search/', StorySearchView.as_view(), name='story-search'),
    path('stories/<int:pk>/', StoryDetailView.as_view(), name='story-detail'),
    # Other URL patterns...#
]



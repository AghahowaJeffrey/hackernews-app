
from django.contrib import admin
from django.urls import path, include
from .views import (
    LatestStoriesView, 
    TopStoriesView, 
    FilteredStoriesView, 
    StorySearchView, 
    StoryDetailView )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('latest-stories/', LatestStoriesView.as_view(), name='latest-stories'), #/latest-stories/
    path('top-stories/', TopStoriesView.as_view(), name='top-stories'), #/top-stories/
    path('filtered-stories/', FilteredStoriesView.as_view(), name='filtered-stories'), #/filtered-stories/?filter=
    path('story-search/', StorySearchView.as_view(), name='story-search'), #/story-search/?search=
    path('stories/<int:pk>/', StoryDetailView.as_view(), name='story-detail'), #/stories/12/
    # Other URL patterns...#
]



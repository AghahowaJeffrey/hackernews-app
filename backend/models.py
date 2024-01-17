from django.db import models
from django.contrib.auth import get_user_model

TYPE_OPTIONS = {
    ('s', 'story'),
    ('c', 'comment'),
}
class Story(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True, related_name='story')
    fetched = models.BooleanField(default=True)
    title = models.CharField(max_length=255)
    by = models.CharField(max_length=255, null=True)
    descendants = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    text = models.TextField()
    type = models.CharField(max_length=20, default='story', choices=TYPE_OPTIONS)
    time = models.DateTimeField(editable=False, auto_now_add=True)
    url = models.URLField(max_length=200, null=True)

    def __str__(self):
        return f"{self.by} - {self.title}"

class Comment(models.Model):
    comment_id = models.IntegerField(unique=True)
    parent_story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='comments')
    by = models.CharField(max_length=255)
    text = models.TextField()
    type = models.CharField(max_length=20, default='comment')
    time = models.DateTimeField()

    def __str__(self):
        return f"{self.by} - {self.parent_story}"
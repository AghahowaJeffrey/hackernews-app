from django.db import models

class Story(models.Model):
    story_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    by = models.CharField(max_length=255)
    descendants = models.IntegerField()
    score = models.IntegerField()
    text = models.TextField()
    type = models.CharField(max_length=20, default='story')
    time = models.DateTimeField()
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
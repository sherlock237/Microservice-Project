from django.db import models

class Content(models.Model):
    title = models.CharField(max_length=255)
    story = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField()

    def __str__(self):
        return self.title
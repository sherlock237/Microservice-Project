# user_interaction_service/models.py
from django.db import models

class UserInteraction(models.Model):
    LIKE = 'LIKE'
    READ = 'READ'
    INTERACTION_TYPES = [
        (LIKE, 'Like'),
        (READ, 'Read'),
    ]

    user_id = models.IntegerField()
    content_id = models.IntegerField()
    interaction_type = models.CharField(
        max_length=4, choices=INTERACTION_TYPES, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id} - {self.content_id} - {self.interaction_type}"

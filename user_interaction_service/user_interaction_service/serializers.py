# user_interaction_service/serializers.py
from rest_framework import serializers
from .models import UserInteraction

class UserInteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInteraction
        fields = ('id', 'user_id', 'content_id', 'interaction_type', 'created_at')

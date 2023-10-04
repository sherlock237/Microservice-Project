# user_interaction_service/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from .models import UserInteraction
from .serializers import UserInteractionSerializer
from django.db.models import Count
from rest_framework.views import APIView
import pdb

class UserInteractionCreateView(generics.CreateAPIView):
    serializer_class = UserInteractionSerializer

    def create(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        content_id = request.data.get('content_id')
        interaction_type = request.data.get('interaction_type')

        # try:
        #     user = User.objects.get(id=user_id)
        #     content = Content.objects.get(id=content_id)
        # except User.DoesNotExist:
        #     return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        # except Content.DoesNotExist:
        #     return Response({'error': 'Content not found.'}, status=status.HTTP_404_NOT_FOUND)

        data = {
            'user_id': user_id,
            'content_id': content_id,
            'interaction_type': interaction_type
        }

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserInteractionDetailView(generics.ListAPIView):
    serializer_class = UserInteractionSerializer
    lookup_field = 'user_id'

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return UserInteraction.objects.filter(user_id=user_id)

class UserInteractionUpdateView(generics.RetrieveUpdateAPIView):
    queryset = UserInteraction.objects.all()
    serializer_class = UserInteractionSerializer


class TopReadContents(APIView):
    def get(self, request, *args, **kwargs):
        top_read_contents = UserInteraction.objects \
            .filter(interaction_type='READ') \
            .values('content_id') \
            .annotate(read_count=Count('content_id')) \
            .order_by('-read_count') \
            .values_list('content_id', flat=True)
        
        return Response({'contents_id': list(top_read_contents)})

class TopLikeContents(APIView):
    def get(self, request, *args, **kwargs):
        top_like_contents = UserInteraction.objects \
            .filter(interaction_type='LIKE') \
            .values('content_id') \
            .annotate(like_count=Count('content_id')) \
            .order_by('-like_count') \
            .values_list('content_id', flat=True)
        
        return Response({'contents_id': list(top_like_contents)})

class TopContents(APIView):
    def get(self, request, *args, **kwargs):
        content_counts = UserInteraction.objects.values('content_id') \
            .annotate(content_count=Count('content_id')) \
            .order_by('-content_count') \
            .values_list('content_id', flat=True)

        return Response({'contents_id': list(content_counts)})
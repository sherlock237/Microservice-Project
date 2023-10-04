import csv
from django.shortcuts import render
from rest_framework import generics, status
from .models import Content
from .serializers import ContentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from django.db.models import Case, When
import requests
import json
# from user_interaction_service.user_interaction_service.models import UserInteraction

class ContentCreateView(generics.CreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class ContentListView(generics.ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class ContentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class SortedByDateList(generics.ListAPIView):
    queryset = Content.objects.all().order_by('-date_published')
    serializer_class = ContentSerializer

class CSVIngestionView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request):
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith('.csv'):
            return Response({'error': 'File is not a CSV'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            for row in reader:
                # Assuming CSV columns are 'title', 'story', 'date_published', 'user_id'
                serializer = ContentSerializer(data=row)
                if serializer.is_valid():
                    serializer.save()
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'CSV data ingested successfully'}, status=status.HTTP_201_CREATED)

class TopContentsListView(ListAPIView):
    serializer_class = ContentSerializer

    def get_queryset(self):
        sort = json.loads(self.request.body).get('sort')
        if sort == 'LIKE':
            url = 'http://localhost:8002/top-like-contents/'
        elif sort == 'READ':
            url = 'http://localhost:8002/top-read-contents/'
        else:
            url = 'http://localhost:8002/top-contents/'
        
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            content_ids = data.get('contents_id')
            preserved_order_whens = [When(pk=pk, then=pos) for pos, pk in enumerate(content_ids)]
            sorted_content = Content.objects.filter(id__in=content_ids).order_by(Case(*preserved_order_whens))
            return sorted_content

        return Content.objects.none()


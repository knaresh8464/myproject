from django.shortcuts import render
from rest_framework import viewsets
from .models import languages
from .serializers import languagesserializer

class languageview(viewsets.ModelViewSet):
    queryset = languages.objects.all()
    serializer_class = languagesserializer

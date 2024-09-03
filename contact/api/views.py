from django.shortcuts import render
from rest_framework import viewsets
from api.models import Contact_Enquriy
from api.serializers import ContactSerializer
# Create your views here.
class ContectViewSet(viewsets.ModelViewSet):
    queryset=Contact_Enquriy.objects.all()
    serializer_class=ContactSerializer

    
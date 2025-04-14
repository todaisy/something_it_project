from django.shortcuts import render

from rest_framework import viewsets
from TestForAbit.models import UserPasses, UserProgress
from .serializers import UserPassesSerializer, UserProgressSerializer
# Create your views here.

class UserProgressSerializerViewSet(viewsets.ModelViewSet):
    queryset = UserProgress.objects.all()
    serializer_class = UserProgressSerializer

class UserPassesSerializerViewSet(viewsets.ModelViewSet):
    queryset = UserPasses.objects.all()
    serializer_class = UserPassesSerializer
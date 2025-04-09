from django.shortcuts import render

from rest_framework import viewsets
from TestForAbit.models import Question
from .serializers import QuestionSerializer
# Create your views here.

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
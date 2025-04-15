from django.shortcuts import render

from rest_framework import viewsets
from TestForAbit.models import UserPasses, UserProgress, TestAnswers, Questions, Weight, ListProf
from .serializers import UserPassesSerializer, UserProgressSerializer, TestAnswersSerializer, QuestionsSerializer, WeightSerializer, ListProfSerializer
# Create your views here.

def create_model_vewset(model_class, Serializer_class):
    class DynamicViewSet(viewsets.ModelViewSet):
        queryset = model_class.objects.all()
        serializer_class = Serializer_class
    return DynamicViewSet

UserPassesSerializerViewSet = create_model_vewset(UserPasses, UserPassesSerializer)
UserProgressSerializerViewSet = create_model_vewset(UserProgress,UserProgressSerializer)
TestAnswersSerializerViewSet = create_model_vewset(TestAnswers, TestAnswersSerializer)
QuestionsSerializerViewSet = create_model_vewset(Questions, QuestionsSerializer)
WeightSerializerViewSet = create_model_vewset(Weight, WeightSerializer)
ListProfSerializerViewSet = create_model_vewset(ListProf, ListProfSerializer)


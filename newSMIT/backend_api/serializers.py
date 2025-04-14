from rest_framework import serializers
from TestForAbit.models import UserPasses, UserProgress, TestAnswers, Questions, Weight, ListProf

def create_model_serializer(model_class, fields='__all__'):
    class DynamicModelSerializer(serializers.ModelSerializer):
        class Meta:
            model = model_class
            fields = '__all__'
    return DynamicModelSerializer

UserPassesSerializer = create_model_serializer(UserPasses)
UserProgressSerializer = create_model_serializer(UserProgress)
TestAnswersSerializer = create_model_serializer(TestAnswers)
QuestionsSerializer = create_model_serializer(Questions)
WeightSerializer = create_model_serializer(Weight)
ListProfSerializer = create_model_serializer(ListProf)

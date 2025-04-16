from rest_framework import serializers
from TestForAbit.models import UserPasses, UserProgress, TestSession, TestAnswers, Questions, Weight, ListProf


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestSession
        fields = ['session_id']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestAnswers
        fields = ['id_test', 'id_ques', 'id_answ', 'answer_text']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['id', 'id_test', 'id_ques', 'question_text', 'answer_text']


class AnswerOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestAnswers
        fields = ['id_answ', 'answer_text', 'id_weights', 'id_group']


def create_model_serializer(model_class, fields='__all__'):
    class DynamicModelSerializer(serializers.ModelSerializer):
        class Meta:
            model = model_class
            fields = '__all__'
    return DynamicModelSerializer

UserPassesSerializer = create_model_serializer(UserPasses)
UserProgressSerializer = create_model_serializer(UserProgress)
TestAnswersSerializer = create_model_serializer(TestAnswers)
# QuestionsSerializer = create_model_serializer(Questions)
WeightSerializer = create_model_serializer(Weight)
ListProfSerializer = create_model_serializer(ListProf)

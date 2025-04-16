from rest_framework import serializers
from TestForAbit.models import UserPasses, UserProgress, TestSession, TestAnswers, Questions, Weight, ListProf

def create_model_serializer(model_class, fieldss='__all__'):
    class DynamicModelSerializer(serializers.ModelSerializer):
        class Meta:
            model = model_class
            fields = fieldss
    return DynamicModelSerializer

SessionSerializer = create_model_serializer(TestSession, ['session_id'])
AnswerOptionSerializer = create_model_serializer(TestAnswers,['id_answ', 'answer_text', 'id_weights', 'id_group'] )
UserPassesSerializer = create_model_serializer(UserPasses)
UserProgressSerializer = create_model_serializer(UserProgress)
QuestionSerializer = create_model_serializer(Questions, ['id', 'id_test', 'id_ques', 'answer_text'])
WeightSerializer = create_model_serializer(Weight)
ListProfSerializer = create_model_serializer(ListProf)

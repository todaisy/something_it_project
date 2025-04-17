from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Questions, TestAnswers
from backend_api.serializers import *
from .models import TestSession


@api_view(['POST'])
def start_test_session(request):
    try:
        test_id = 1  # Или получить из запроса
        new_session = TestSession.objects.create(test_id=test_id)

        return Response({
            'session_id': str(new_session.session_id),
            'created_at': new_session.created_at
        }, status=201)

    except Exception as e:
        return Response({"error": str(e)}, status=500)


@api_view(['GET'])
def get_question(request, session_id, t_id, q_id):
    try:
        session = TestSession.objects.get(session_id=session_id)
    except TestSession.DoesNotExist:
        return Response({"error": "Invalid session"}, status=status.HTTP_404_NOT_FOUND)

    questions = Questions.objects.filter(id_test=t_id).order_by('id_ques')

    try:
        question = questions[q_id - 1]  # Получаем вопрос по порядковому номеру
    except IndexError:
        return Response({"error": "Question not found"}, status=404)

    answer_options = TestAnswers.objects.filter(
        session=session,
        id_test=t_id,
        id_ques=question.id_ques  # Используем реальный ID вопроса
    )

    # Сериализуем данные
    question_serializer = QuestionSerializer(question)
    options_serializer = AnswerOptionSerializer(answer_options, many=True)

    # Определяем общее количество вопросов в тесте
    total_questions = Questions.objects.filter(id_test=t_id).count()

    # Формируем данные для навигации
    navigation = {
        'previous': q_id - 1 if q_id > 1 else None,
        'next': q_id + 1 if q_id < total_questions else None,
        'total': total_questions,
        'current': q_id
    }

    # Собираем полный ответ
    response_data = {
        'question': question_serializer.data,
        'options': options_serializer.data,
        'navigation': navigation
    }

    return Response(response_data)
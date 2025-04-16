from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Questions, TestAnswers
from backend_api.serializers import *
from .models import TestSession


@api_view(['POST'])
def start_test_session(request):
    # Создаем новую сессию
    new_session = TestSession.objects.create()

    # Возвращаем клиенту session_id
    return Response({
        'session_id': str(new_session.session_id),
        'created_at': new_session.created_at
    })

@api_view(['GET'])
def get_question(request, t_id, q_id):
    session_id = request.headers.get('X-Session-Id')
    if not session_id:
        return Response({"error": "Session ID required"}, status=400)

    try:
        session = TestSession.objects.get(session_id=session_id)
    except TestSession.DoesNotExist:
        return Response({"error": "Invalid session"}, status=400)

    # Получаем вопрос из базы данных
    question = get_object_or_404(Questions, id_test=t_id, id_ques=q_id)

    # Получаем варианты ответов для этого вопроса
    answer_options = TestAnswers.objects.filter(
        id_test=t_id,
        id_ques=q_id
    ).order_by('id_answ')

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


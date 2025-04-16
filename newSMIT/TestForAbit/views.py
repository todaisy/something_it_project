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

''' 
@api_view(['GET', 'POST'])
def question_detail(request, t_id, q_id):
    # Получаем вопрос из модели Questions
    question = get_object_or_404(Questions, id_test=t_id, id_ques=q_id)

    # Получаем варианты ответов из TestAnswers
    answer_options = TestAnswers.objects.filter(
        id_test=t_id,
        id_ques=q_id
    ).order_by('id_answ')

    # Сериализуем данные
    question_data = {
        'question': QuestionSerializer(question).data,
        'options': AnswerOptionSerializer(answer_options, many=True).data
    }

    if request.method == 'GET':
        # Логика для получения текущего ответа пользователя
        try:
            user_answer = TestAnswers.objects.get(
                id_test=t_id,
                id_ques=q_id,
                user=request.user if request.user.is_authenticated else None
            )
            question_data['current_answer'] = user_answer.answer_text
        except TestAnswers.DoesNotExist:
            question_data['current_answer'] = ''

        # Информация для навигации
        total_questions = Questions.objects.filter(id_test=t_id).count()
        question_data['navigation'] = {
            'next': q_id + 1 if q_id < total_questions else None,
            'previous': q_id - 1 if q_id > 1 else None,
            'total': total_questions
        }

        return Response(question_data)

    elif request.method == 'POST':
        # Обработка сохранения ответа
        serializer = AnswerOptionSerializer(data=request.data)
        if serializer.is_valid():
            # Сохраняем или обновляем ответ
            answer, created = TestAnswers.objects.update_or_create(
                id_test=t_id,
                id_ques=q_id,
                user=request.user if request.user.is_authenticated else None,
                defaults={
                    'answer_text': serializer.validated_data['answer_text'],
                    'id_weights': serializer.validated_data.get('id_weights', 1),
                    'id_group': serializer.validated_data.get('id_group', 1)
                }
            )
            return Response({'status': 'Answer saved'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''

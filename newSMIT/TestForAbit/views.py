from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .forms import MyRadioForm
from .models import TestAnswers, Questions

# Create your views here.

def index(request):
    data = {'title': 'Главная','txt':''}
    return render(request, 'TestForAbit/index.html', context=data)

def radio_test(request, t_id, q_id):
    question = get_object_or_404(Questions, id_test=t_id, id_ques=q_id)
    answers_qs = TestAnswers.objects.filter(id_test=t_id, id_ques=q_id)
    answers_data = [(a.id, a.answer_text) for a in answers_qs]
    if request.method == 'POST':
        form = MyRadioForm(answers_data, 'Ваш ответ сохранен',request.POST)
        if form.is_valid():
            print(form.cleaned_data['option'])
            # Здесь можно выполнить дальнейшую  обработку данных
    else:
        form = MyRadioForm(answers_data, question.answer_text)
        txt = 'Обычный текст'
    data = {
        'title': 'вопросы',
        'form': form,
        't_id': t_id,
        'q_id': q_id,
        'next': q_id + 1,
        'last': q_id - 1,
        'last_q_id':len(Questions.objects.filter(id_test=t_id)),
            }
    return render(request, 'TestForAbit/qwest_template.html', context=data)
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .forms import MyRadioForm
from .models import TestAnswers, Questions

# Create your views here.

def index(request):
    data = {'title': 'Главная','txt':''}
    return render(request, 'TestForAbit/index.html', context=data)

vaes = [[('1', 'Вариант 1.1'), ('2', 'Вариант 1.2'),('3', 'Вариант 1.3'),],
        [('1', 'Вариант 2.1'), ('2', 'Вариант 2.2'),('3', 'Вариант 2.3'),],
        [('1', 'Вариант 3.1'), ('2', 'Вариант 3.2'),('3', 'Вариант 3.3'),],
        [('1', 'Вариант 4.1'), ('2', 'Вариант 4.2'),('3', 'Вариант 4.4'),]]
def radio_test(request, t_id, q_id):
    question = get_object_or_404(Questions, id_test=t_id, id_ques=q_id)
    question_data = vaes[q_id - 1]
    if request.method == 'POST':
        form = MyRadioForm(vaes[q_id-1], 'Ваш ответ сохранен',request.POST)
        if form.is_valid():
            print(form.cleaned_data['option'])
            # Здесь можно выполнить дальнейшую  обработку данных
    else:
        form = MyRadioForm(question_data, question.answer_text)
        txt = 'Обычный текст'
    data = {
        'title': 'вопросы',
        'form': form,
        't_id': t_id,
        'q_id': q_id,
        'next': q_id + 1,
        'last': q_id - 1,
        'last_q_id':len(vaes),
            }
    return render(request, 'TestForAbit/qwest_template.html', context=data)
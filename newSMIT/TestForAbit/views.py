from django.shortcuts import render
from django.http import Http404
from .forms import MyRadioForm

# Create your views here.

def index(request):
    data = {'title': 'Главная','txt':''}
    return render(request, 'TestForAbit/index.html', context=data)

vaes = [[('1', 'Вариант 1.1'), ('2', 'Вариант 1.2'),('3', 'Вариант 1.3'),],
        [('1', 'Вариант 2.1'), ('2', 'Вариант 2.2'),('3', 'Вариант 2.3'),],
        [('1', 'Вариант 3.1'), ('2', 'Вариант 3.2'),('3', 'Вариант 3.3'),],
        [('1', 'Вариант 4.1'), ('2', 'Вариант 4.2'),('3', 'Вариант 4.4'),]]
def radio_test(request, q_id):
    if q_id - 1 >= len(vaes):
        raise Http404
    question_data = vaes[q_id - 1]
    if request.method == 'POST':
        form = MyRadioForm(vaes[q_id-1], 'Ваш ответ сохранен',request.POST)
        if form.is_valid():
            print(form.cleaned_data['option'])
            # Здесь можно выполнить дальнейшую  обработку данных
    else:
        form = MyRadioForm(question_data, 'Выбирете ответ')
        txt = 'Обычный текст'
    data = {
        'title': 'вопросы',
        'form': form,
        'q_id': q_id,
        'next': q_id + 1,
        'last': q_id - 1,
        'last_q_id':len(vaes),
            }
    return render(request, 'TestForAbit/qwest_template.html', context=data)
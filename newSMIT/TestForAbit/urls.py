from django.urls import path
from . import views


urlpatterns = [
    path('', views.start_test_session, name='start-session'),
    path('api/question/<int:t_id>/<int:q_id>/', views.get_question, name='qwsts'),
    # path('api/save-answer/<int:t_id>/<int:q_id>/', views.save_answer)
    # ... другие URL ...
]


'''
urlpatterns = [
    path('',views.index, name='home'),
    path('qwest/<int:t_id>/<int:q_id>/', views.radio_test, name='qwsts')]
    path('api/question/<int:t_id>/<int:q_id>/', views.get_question, name='qwsts'),
    path('api/save-answer/<int:t_id>/<int:q_id>/', views.save_answer),
    path('api/start-session/', views.start_session),
    path('api/questions/<uuid:session_id>/<int:t_id>/<int:q_id>/', views.question_handler),
'''
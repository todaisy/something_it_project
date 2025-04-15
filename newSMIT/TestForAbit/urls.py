from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('qwest/<int:t_id>/<int:q_id>/', views.radio_test, name='qwsts')]
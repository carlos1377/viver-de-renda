from django.urls import path, include
from vrenda import views

app_name = 'vrenda'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),

]

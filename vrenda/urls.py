from django.urls import path
from vrenda import views

app_name = 'vrenda'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout, name='logout'),
    path('despesas/', views.despesas, name='despesas'),
]

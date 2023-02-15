from django.urls import path
from .views import main, login

app_name = 'application'

urlpatterns = [
    path('', main, name='index'),
    path('main/', main, name='main'),
    path('login/', login, name='login'),
]



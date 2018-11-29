from django.urls import path
from .views import log_in, index, sign_up, welcome
from django.contrib.auth import views as auth_views

app_name = 'users'
urlpatterns = [
    path('',  welcome, name = 'welcome'),
    path('log_in/', log_in, name='log_in'),
    path('sign_up/', sign_up, name='sign_up'),
]
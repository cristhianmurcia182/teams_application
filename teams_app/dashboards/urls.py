from django.urls import path
from .views import dashboards, create_board, sort_by_name, sort_by_date, search_board, edit_board, create_column, create_task, delete_board
from django.contrib.auth import views as auth_views

app_name = 'dashboards'
urlpatterns = [
    path('',  dashboards, name = 'dashboards'),
    path('create_board/',  create_board, name = 'create_board'),
    path('sort_by_name/', sort_by_name, name='sort_by_name'),
    path('sort_by_date/', sort_by_date, name='sort_by_date'),
    path('search_board', search_board, name = 'search_board'),
    path('edit_board/<int:board_pk>', edit_board, name='edit_board'),
    path('delete_board/<int:board_pk>', delete_board, name='delete_board'),
    path('create_column/<int:board_pk>', create_column, name='create_column'),
    path('create_task/<int:board_pk>/<int:column_pk>', create_task, name='create_task'),
]
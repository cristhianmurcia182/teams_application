from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Board, Column


def dashboards(request):
    user_starting_letter = str(request.user)[0].capitalize()
    all_boards = Board.objects.all()
    context = {'user_starting_letter':user_starting_letter, 'all_boards': all_boards}
    print('sl', user_starting_letter,'user', str(request.user), 'auth', str(request.user.is_authenticated), 'id', str(request.user.pk))
    return render(request, 'dashboards/dashboards.html', context)

def create_board(request):
    user_starting_letter = str(request.user)[0].capitalize()
    if request.method == 'POST':
        print("I am in post!")
        try:
            print("Creating Board!")
            board_name = request.POST['board_name']
            board = Board(name = board_name)
            board.save()
        except (KeyError):
            return render(request, 'dashboards/dashboard_form.html', {
                'error_message': "You did not type a board name!!",
                'user_starting_letter':user_starting_letter,
            })
        else:
            all_boards = Board.objects.all()
            context = {'user_starting_letter': user_starting_letter, 'all_boards': all_boards}
            return HttpResponseRedirect(reverse('dashboards:dashboards'))
    else :
        print("I am in get!")
        return render(request, 'dashboards/dashboard_form.html', {
            'user_starting_letter': user_starting_letter,
        })

def sort_by_name(request):
    all_boards = Board.objects.order_by('name')
    user_starting_letter = str(request.user)[0].capitalize()
    context = {'user_starting_letter': user_starting_letter, 'all_boards': all_boards}
    return render(request, 'dashboards/dashboards.html', context)

def sort_by_date(request):
    all_boards = Board.objects.order_by('create_date')
    user_starting_letter = str(request.user)[0].capitalize()
    context = {'user_starting_letter': user_starting_letter, 'all_boards': all_boards}
    return render(request, 'dashboards/dashboards.html', context)

def search_board(request):
    user_starting_letter = str(request.user)[0].capitalize()
    all_boards = Board.objects.all()
    try:
        board_name = request.POST['board_name']
        board = Board(name=board_name)
        all_boards = Board.objects.filter(name__icontains = board_name)
        context = {'user_starting_letter': user_starting_letter, 'all_boards': all_boards}
        print(str(all_boards[0].pk), str(type(all_boards[0].pk)))
        return render(request, 'dashboards/dashboards.html', context)
    except (KeyError):
        context = {'user_starting_letter': user_starting_letter, 'all_boards': all_boards}
        return render(request, 'dashboards/dashboards.html', context)

def edit_board(request, board_pk):
    board = Board.objects.filter(pk = str(board_pk))[0]
    all_columns = board.column_set.all()
    user_starting_letter = str(request.user)[0].capitalize()
    print(board.name)
    context = {'board': board, 'user_starting_letter':user_starting_letter, 'all_columns': all_columns}
    return render(request, 'dashboards/board.html', context)

def create_column(request, board_pk):
    print("in create column")
    board = Board.objects.filter(pk=str(board_pk))[0]
    user_starting_letter = str(request.user)[0].capitalize()
    try:
        column_name = request.POST['column_name']
        board.column_set.create(index=board_pk, name=column_name)
        board.save()
        all_columns = board.column_set.all()
        context = {'user_starting_letter': user_starting_letter, 'all_columns': all_columns, 'board': board}
        return render(request, 'dashboards/board.html', context)
    except (KeyError):
        all_columns = Column.objects.all()
        context = {'user_starting_letter': user_starting_letter, 'all_columns': all_columns, 'board': board}
        return render(request, 'dashboards/board.html', context)


def create_task(request, board_pk, column_pk):
    board = Board.objects.filter(pk = str(board_pk))[0]
    column = Column.objects.filter(pk=str(column_pk))[0]
    user_starting_letter = str(request.user)[0].capitalize()
    try:
        task_title = request.POST['task_title']
        task_description = request.POST['task_description']
        column.task_set.create(title=task_title, description=task_description)
        column.save()
        all_columns = board.column_set.all()
        context = {'user_starting_letter': user_starting_letter, 'all_columns': all_columns, 'board': board}
        return render(request, 'dashboards/board.html', context)
    except (KeyError):
        all_columns = board.column_set.all()
        context = {'user_starting_letter': user_starting_letter, 'all_columns': all_columns, 'board': board}
        return render(request, 'dashboards/board.html', context)

def delete_board(request, board_pk):
    user_starting_letter = str(request.user)[0].capitalize()
    board = Board(pk = str(board_pk))
    board.delete()
    all_boards = Board.objects.all()
    context = {'user_starting_letter': user_starting_letter, 'all_boards': all_boards}
    return render(request, 'dashboards/dashboards.html', context)


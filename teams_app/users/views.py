from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SignUpForm
from django.urls import reverse



def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return HttpResponseRedirect(reverse('users:log_in'))
        else:
            return render(request, 'users/sign_up.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'users/sign_up.html', {'form': form})

def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            print('username', user.username)

            # ask
            request.user = user

            print('USER->', str(request.user))
            # return HttpResponseRedirect(reverse('dashboards:dashboards'))
            user_starting_letter = str(request.user)[0].capitalize()

            context = {'user_starting_letter': user_starting_letter}
            # return render(request, 'dashboards/dashboards.html', context)
            #Does not work with authenticated user
            return HttpResponseRedirect(reverse('dashboards:dashboards'))
        else:
            context = {'error_message': 'The user does not exists!'}
            return render(request, 'users/log_in.html', context)
    else:
        return render(request, 'users/log_in.html')


def index(request):
    return HttpResponse("Hello, world. You created an user.")

def welcome(request):
    return render(request, 'users/welcome.html')

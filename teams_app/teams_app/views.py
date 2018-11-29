from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect



def index(request):
    return HttpResponseRedirect(reverse('users:welcome'))

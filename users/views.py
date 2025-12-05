from django.shortcuts import render, redirect
from django.contrib.auth import login as login_func, logout as logout_func

from .forms import LoginForm, RegisterForm

def login(request):

    form = LoginForm(request)

    if request.method == 'POST':
        form = LoginForm(request, request.POST)

        if form.is_valid():
            login_func(request, form.get_user())

            return redirect('/')

    context = {'form': form}

    return render(request, 'users/login.html', context)


def logout(request):

    logout_func(request)
    return redirect('/')


def register(request):

    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            # создание пользователя и профиля

            return redirect('/')

    context = {'form': form}
    return render(request, 'users/register.html', context)

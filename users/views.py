from django.shortcuts import render

from .forms import LoginForm

def login(request):

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(form)

        if form.is_valid():
            print('успех')

    context = {'form': form}

    return render(request, 'users/login.html', context)

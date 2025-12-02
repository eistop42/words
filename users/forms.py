from django import forms
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    login = forms.CharField(label='логин')
    password = forms.CharField(label='пароль', widget=forms.PasswordInput())


    def clean(self):
        login = self.cleaned_data['login']
        password = self.cleaned_data['password']

        user = authenticate()


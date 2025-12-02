from django import forms

from .models import Word, Zametka


class AddWordForm(forms.ModelForm):

    class Meta:
        model = Word
        fields = ['slovo', 'perevod']

class AddZametkaForm(forms.ModelForm):
    class Meta:
        model = Zametka
        fields = ['text']
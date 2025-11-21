from django.shortcuts import render
from django.http import HttpResponse

from .models import Word

def main(request):

    words = Word.objects.all() # select * from word

    context = {'words': words}
    return render(request, 'main.html', context)

def word(request, word_id):

    word = Word.objects.get(id=word_id)

    context = {'word': word}
    return render(request, 'word.html', context)


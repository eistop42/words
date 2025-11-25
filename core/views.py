from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Word
from .forms import AddWordForm

def main(request):

    form = AddWordForm()
    status = request.GET.get('status')

    if status:
        words = Word.objects.filter(status=status)
    else:
        words = Word.objects.all() # select * from word



    context = {'words': words, 'status': status, 'form': form}
    return render(request, 'main.html', context)

def word(request, word_id):

    word = Word.objects.get(id=word_id)

    context = {'word': word}
    return render(request, 'word.html', context)


def izucheno(request, word_id):
    word = Word.objects.get(id=word_id)

    word.status = Word.IZUCHENO
    word.save()
    return redirect('word_detail', word.id)

def na_izuchenii(request, word_id):
    word = Word.objects.get(id=word_id)

    word.status = Word.NA_IZUCHENII
    word.save()
    return redirect('word_detail', word.id)

def delete_word(reqeust, word_id):
    word = Word.objects.get(id=word_id)
    word.delete()
    return redirect('/')
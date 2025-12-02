from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

from .models import Word, Zametka
from .forms import AddWordForm, AddZametkaForm

def main(request):

    form = AddWordForm()

    if request.method == 'POST':
        form = AddWordForm(request.POST)
        if form.is_valid():
            form.save()

            # обновляем форму
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
    zametki = word.zametki.all()
    zametki2 = Zametka.objecsts.filter(word_id=word_id)

    form = AddZametkaForm()

    if request.method == 'POST':
        form = AddZametkaForm(request.POST)
        if form.is_valid():
            zametka = form.save(commit=False)
            zametka.word = word
            zametka.save()

            return redirect('word_detail', word.id)

    context = {'word': word, 'zametki': zametki, 'form': form}
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


class HelloView(View):

    def get_words(self):
        words = Word.objects.all()
        return words

    def get(self, request):
        words = self.get_words()
        context = {'words': words}

        return render(request, 'class.html', context)

    def post(self, request):
        form = AddZametkaForm(request.POST)
        if form.is_valid():
            zametka = form.save(commit=False)
            zametka.word = word
            zametka.save()

            return redirect('word_detail', word.id)


class MyTemplateView(TemplateView):
    template_name = 'class.html'

    def get_context_data(self, **kwargs):
        # a = 4 / 0
        return {'name': 'Alisa'}
from django.shortcuts import render, redirect, Http404
from django.contrib.auth.decorators import login_required

from django.views import View
from django.views.generic import TemplateView

from .models import Word, Zametka
from .forms import AddWordForm, AddZametkaForm

def main(request):

    form = AddWordForm()

    if request.method == 'POST' and request.user.is_authenticated:
        form = AddWordForm(request.POST)
        if form.is_valid():

            # привязываем слово к пользователю
            word = form.save(commit=False)
            word.profile = request.user.profile
            word.save()

            # обновляем форму
            form = AddWordForm()


    status = request.GET.get('status')

    words = []
    if request.user.is_authenticated:
        profile = request.user.profile

        words = Word.objects.filter(profile=profile)

        if status:
            words = words.filter(status=status)

    context = {'words': words, 'status': status, 'form': form}
    return render(request, 'main.html', context)


@login_required
def word(request, word_id):

    profile = request.user.profile
    word = Word.objects.get(id=word_id)

    if profile.id != word.profile.id:
        raise Http404

    zametki = word.zametki.all()
    zametki2 = Zametka.objects.filter(word_id=word_id)

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
from django.db import models

from users.models import Profile

class Word(models.Model):

    NA_IZUCHENII = 'na_izuchenii'
    IZUCHENO = 'izucheno'

    STATUS = [(NA_IZUCHENII, 'На изуечнии'), (IZUCHENO, 'Изучено')]

    slovo = models.CharField(max_length=200, verbose_name='слово')
    perevod = models.CharField(max_length=200, verbose_name='перевод')
    status = models.CharField(max_length=20, choices=STATUS, default=NA_IZUCHENII, verbose_name='статус')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='профиль пользователя')

    def __str__(self):
        return self.slovo

    def unique_error_message(self, model_class, unique_check):
        if unique_check == ('slovo', 'perevod'):
            return "Такая пара слов уже есть"
        return super().unique_error_message(model_class, unique_check)

    class Meta:
        verbose_name = 'слово'
        verbose_name_plural = 'слова'
        unique_together = (('slovo', 'perevod'), )



class Zametka(models.Model):
    text = models.TextField(verbose_name='текст заметки', max_length=1000)
    word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='zametki', verbose_name='слово')


    def __str__(self):
        return self.text[:10]

    class Meta:
        verbose_name = 'заметка'
        verbose_name_plural = 'заметки'


class LikesCounter(models.Model):
    name = models.CharField(verbose_name='имя', max_length=255)
    slug = models.SlugField(unique=True, verbose_name='кодовое название')
    count = models.IntegerField(default=0, verbose_name='количество спасибок')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'счетчик спасибок'
        verbose_name_plural = 'счетчики спасибок'


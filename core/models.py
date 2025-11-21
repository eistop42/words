from django.db import models


class Word(models.Model):
    slovo = models.CharField(max_length=200, verbose_name='слово')
    perevod = models.CharField(max_length=200, verbose_name='перевод')

    def __str__(self):
        return self.slovo

    class Meta:
        verbose_name = 'слово'
        verbose_name_plural = 'слова'



from django.db import models


class Word(models.Model):

    NA_IZUCHENII = 'na_izuchenii'
    IZUCHENO = 'izucheno'

    STATUS = [(NA_IZUCHENII, 'На изуечнии'), (IZUCHENO, 'Изучено')]

    slovo = models.CharField(max_length=200, verbose_name='слово')
    perevod = models.CharField(max_length=200, verbose_name='перевод')
    status = models.CharField(max_length=20, choices=STATUS, default=NA_IZUCHENII, verbose_name='статус')

    def __str__(self):
        return self.slovo

    class Meta:
        verbose_name = 'слово'
        verbose_name_plural = 'слова'



from django.contrib import admin

from .models import Word, Zametka, LikesCounter

class MyWord(admin.ModelAdmin):
    list_display = ['slovo', 'perevod', 'status']


admin.site.register(Word, MyWord)
admin.site.register(Zametka)
admin.site.register(LikesCounter)

from django.contrib import admin

from .models import Word

class MyWord(admin.ModelAdmin):
    list_display = ['slovo', 'perevod', 'status']


admin.site.register(Word, MyWord)

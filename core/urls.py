from django.urls import path

from .views import main, word

urlpatterns = [
    path('', main),
    path('words/<int:word_id>', word),
]

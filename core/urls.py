from django.urls import path

from .views import main, word, izucheno, na_izuchenii, delete_word, HelloView, MyTemplateView

urlpatterns = [
    path('', main, name='main'),
    path('words/<int:word_id>', word, name='word_detail'),
    path('words/<int:word_id>/izucheno', izucheno, name='word_izucheno'),
    path('words/<int:word_id>/na_izuchenii', na_izuchenii, name='word_na_izuchenii'),
    path('words/<int:word_id>/delete', delete_word, name='delete_word'),
    path('hello', HelloView.as_view()),
    path('template', MyTemplateView.as_view())
]

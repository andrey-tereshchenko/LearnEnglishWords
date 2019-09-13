from django.urls import path
from learn_words.views import index

urlpatterns = [
    path('', index),
]
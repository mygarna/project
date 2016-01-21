from django.conf.urls import patterns, url
from dictionary.views import words

urlpatterns = [
    url(r'words/$', words, name='words'),
]
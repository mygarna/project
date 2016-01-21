from django.shortcuts import render
from dictionary.models import Dictionary

# Create your views here.

def words(request):
   objects = Dictionary.objects.all()
   return render(request, 'words.tpl', {'objects':objects})
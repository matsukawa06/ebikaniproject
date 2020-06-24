from django.shortcuts import render
from .models import Monster

# Create your views here.
def monster_list(request):
    monster = Monster.objects.all()
    return render(request, 'MonHan/monster_list.html', {'monster': monster})
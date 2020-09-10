from django.shortcuts import render
from .models import Monster

from django.db.models import Q
from .forms import MyModelForm
from django.views.generic import CreateView

# Create your views here.
"""
def monster_list(request):
    monster = Monster.objects.all()
    return render(request, 'MonHan/monster_list.html', {'monster': monster})"""

def is_valid_q(q):
    return q != '' and q is not None

def index(request):
    CreateMyModelView.as_view()

    monster = Monster.objects.all().order_by('name')
    name = request.GET.get('name')
    race = request.GET.get('race')

    if is_valid_q(name):
        monster = monster.filter(name__icontains=name)

    if is_valid_q(race):
        monster = monster.filter(race__icontains=race)

    return render(request, 'MonHan/monster_list.html', {'monster': monster, 'name': name})

class CreateMyModelView(CreateView):
    model = Monster
    form_class = MyModelForm
    template_name = 'MonHan/filter.html'
    success_url = "/"   # 成功時にリダイレクトするURL

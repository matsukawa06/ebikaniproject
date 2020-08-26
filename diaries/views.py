from django.shortcuts import render
from .models import Diary

# Create your views here.
def top(request):
    context = {
        # モデル名.objects.all()で日記のすべてを取得
        'diary_list': Diary.objects.all(),
    }
    return render(request,'diaries/diary_list.html', context)

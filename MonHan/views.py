from django.shortcuts import render, get_object_or_404, redirect
from .models import Monster
from django.views import generic
from django.db.models import Q
from .forms import MonsterSearchForm


class monster_list(generic.ListView):
    model = Monster
    ordering = 'name'

    def get_queryset(self):
        queryset = super().get_queryset()
        form = MonsterSearchForm(self.request.GET or None)
        if form.is_valid():
            # 名前で検索
            key_word = form.cleaned_data.get('key_word')
            if key_word:
                queryset = queryset.filter(Q(name__icontains=key_word))
            # 種別で検索
            race = form.cleaned_data.get('race')
            if race:
                queryset = queryset.filter(race=race)
        
        return queryset

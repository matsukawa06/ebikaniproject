from django import template
from MonHan.forms import MonsterSearchForm

register = template.Library()

@register.inclusion_tag('MonHan/search_form.html')
def create_search_form(request):
    form = MonsterSearchForm(request.GET or None)
    return {'form': form}
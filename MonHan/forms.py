from django import forms
from .models import Monster

class MonsterSearchForm(forms.Form):
    key_word = forms.CharField(
        label='モンスター名', required=False,
        widget=forms.TextInput(attrs={'class': 'input'})
    )

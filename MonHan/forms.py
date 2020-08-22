from django.forms import ModelForm
from .models import Monster

class MyModelForm(ModelForm):
    class Meta:
        model = Monster 
        fields = ['series','race']
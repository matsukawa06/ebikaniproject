from django.contrib import admin
from .models import Monster, Series, Symbol

# Register your models here.
admin.site.register(Series)
admin.site.register(Symbol)
admin.site.register(Monster)
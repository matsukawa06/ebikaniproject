from django.contrib import admin
from .models import Monster, Series, Symbol
from .models import Fuatsu, Vibration, Yarare, JyotaiIjyo

# Register your models here.
admin.site.register(Series)
admin.site.register(Symbol)
admin.site.register(Fuatsu)
admin.site.register(Vibration)
admin.site.register(Yarare)
admin.site.register(JyotaiIjyo)
admin.site.register(Monster)

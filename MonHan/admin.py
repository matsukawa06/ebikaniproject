from django.contrib import admin
#from import_export.admin import ImportExportModelAdmin
#from .adminResources import MonsterResource
from .models import Monster

# Register your models here.
admin.site.register(Monster)

"""
class MonsterAdmin(ImportExportModelAdmin):
    ordering = ['id']
    list_display = ('id', 'title', 'author')

    resource_class = MonsterResource
"""
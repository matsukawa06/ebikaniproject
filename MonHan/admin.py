from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Monster

# Register your models here.
#admin.site.register(Monster)

# CSVでモンスター情報をインポートするための定義
class MonsterResource(resources.ModelResource):

    class Meta:
        model = Monster
        skip_unchanged = True
        report_skipped = False
        import_id_fields = ('name',)

@admin.register(Monster)
class MonsterAdmin(ImportExportModelAdmin):
    # importExportModelAdmin を利用するようにする
    ordering = ['id']
    list_display = ('id','name')

    # django-import-exports の設定
    resource_class = MonsterResource

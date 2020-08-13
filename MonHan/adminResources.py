from import_export import resources
from .models import Monster

# CSVでモンスター情報をインポートするための定義
class MonsterResource(resources.ModelResource):

    class Meta:
        model = Monster
        skip_unchanged = True
        report_skipped = False
        import_id_fields = ('name',)

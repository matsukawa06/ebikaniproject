from django.db import models
from django.utils import timezone

# Create your models here.

# モンスター
class Monster(models.Model):
    class Meta:
        verbose_name = "モンスター"
        verbose_name_plural = "モンスター"

    # シリーズ
    SERIES = ((1, 'IB'), (2, 'MHW'))

    # 種族名
    RACE = (
        (1, "鳥竜種"),
        (2, "牙竜種"),
        (3, "魚竜種"),
        (4, "遺存種"),
        (5, "飛竜種"),
        (6, "古龍種"),
        (7, "獣竜種")
    )

    # 選択項目
    DAISYO = ((1, "大"), (2, "小"), (3, "なし"))

    # やられ
    YARARE = ((1, '火'), (2, '水'), (3, '雷'), (4, '氷'), (5, '龍'), (6, 'なし'))

    # 状態異常
    JYOTAIIJYO = (
        (1, '毒'),
        (2, '猛毒'),
        (3, '麻痺'),
        (4, '睡眠'),
        (5, '裂傷'),
        (6, '爆破'),
        (7, '気絶'),
        (8, '防御力DOWN'),
        (9, '瘴気浸食状態'),
        (10, '泥'),
        (11, '凍結やられ'),
        (12, '火'),
        (13, 'なし')
    )

    # 基本情報
    name = models.CharField("モンスター名", max_length=200)
    series = models.IntegerField("シリーズ", choices=SERIES, null=True, blank=True)
    race = models.IntegerField("種族", choices=RACE, null=True, blank=True)
    roar = models.IntegerField("咆哮", choices=DAISYO, null=True, blank=True)
    fuatsu1 = models.IntegerField("風圧１", choices=DAISYO, null=True, blank=True)
    fuatsu2 = models.IntegerField("風圧２", choices=YARARE, null=True, blank=True)
    vibration = models.IntegerField("震動", choices=DAISYO, null=True, blank=True)
    yarare1 = models.IntegerField("やられ１", choices=YARARE, null=True, blank=True)
    yarare2 = models.IntegerField("やられ２", choices=YARARE, null=True, blank=True)
    jyotaiijyo = models.IntegerField("状態異常", choices=JYOTAIIJYO, null=True, blank=True)

    # シンボル
    SYMBOL = (
        (1, '◎'),
        (2, '〇'),
        (3, '△'),
        (4, '×'),
        (5, '？')
    )

    # 弱点属性
    jyaku_hi = models.IntegerField("弱点属性_火", choices=SYMBOL, null=True, blank=True)
    jyaku_mizu = models.IntegerField("弱点属性_水", choices=SYMBOL, null=True, blank=True)
    jyaku_kami = models.IntegerField("弱点属性_雷", choices=SYMBOL, null=True, blank=True)
    jyaku_kori = models.IntegerField("弱点属性_氷", choices=SYMBOL, null=True, blank=True)
    jyaku_ryu = models.IntegerField("弱点属性_龍", choices=SYMBOL, null=True, blank=True)

    # 状態異常耐性
    ijyo_doku = models.IntegerField("状態異常耐性_毒", choices=SYMBOL, null=True, blank=True)
    ijyo_suimin = models.IntegerField("状態異常耐性_睡眠", choices=SYMBOL, null=True, blank=True)
    ijyo_mahi = models.IntegerField("状態異常耐性_麻痺", choices=SYMBOL, null=True, blank=True)
    ijyo_kizetsu = models.IntegerField("状態異常耐性_気絶", choices=SYMBOL, null=True, blank=True)
    ijyo_meki = models.IntegerField("状態異常耐性_滅気", choices=SYMBOL, null=True, blank=True)
    ijyo_bakuha = models.IntegerField("状態異常耐性_爆破", choices=SYMBOL, null=True, blank=True)
    ijyo_nori = models.IntegerField("状態異常耐性_乗り", choices=SYMBOL, null=True, blank=True)

    # アイテム耐性
    item_senko = models.IntegerField("アイテム耐性_閃光", choices=SYMBOL, null=True, blank=True)
    item_otobaku = models.IntegerField("アイテム耐性_音爆", choices=SYMBOL, null=True, blank=True)
    item_koyashi = models.IntegerField("アイテム耐性_こやし玉", choices=SYMBOL, null=True, blank=True)
    item_shibire = models.IntegerField("アイテム耐性_シビレ罠", choices=SYMBOL, null=True, blank=True)
    item_otoshi = models.IntegerField("アイテム耐性_落し穴", choices=SYMBOL, null=True, blank=True)
    item_tsuta = models.IntegerField("アイテム耐性_ツタ", choices=SYMBOL, null=True, blank=True)
    item_wananiku = models.IntegerField("アイテム耐性_罠肉", choices=SYMBOL, null=True, blank=True)

    def __str__(self):
        return self.name

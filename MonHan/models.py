from django.db import models
from django.utils import timezone

# Create your models here.
# シリーズ
class Series(models.Model):
    name = models.CharField('シリーズ名', max_length=5)

    def __str__(self):
        return self.name

# シンボル（◎、〇、△など）
class Symbol(models.Model):
    symbolType = models.CharField('記号種類', max_length=5)

    def __str__(self):
        return self.symbolType

# 種族
class Race(models.Model):
    name = models.CharField('種族名', max_length=6)

# 咆哮
class Roar(models.Model):
    name = models.CharField('咆哮名', max_length=4)

# 風圧
class Fuatsu(models.Model):
    name = models.CharField('風圧名', max_length=4)

# 震動
class Vibration(models.Model):
    name = models.CharField('震動名', max_length=4)

# やられ
class Yarare(models.Model):
    name = models.CharField('やられ名', max_length=8)

# 状態異常
class JyotaiIjyo(models.Model):
    name = models.CharField('状態異常名', max_length=8)

# モンスター
class Monster(models.Model):
    # 基本情報
    name = models.CharField('モンスター名', max_length=200)
    series = models.ForeignKey(Series, verbose_name='シリーズ' ,on_delete=models.PROTECT)
    erce = models.ForeignKey(Race, verbose_name='種族' ,on_delete=models.PROTECT, null=True)
    roar = models.ForeignKey(Roar, verbose_name='咆哮', on_delete=models.PROTECT, null=True)
    fuatsu = models.ForeignKey(Fuatsu, verbose_name='風圧', on_delete=models.PROTECT, null=True)
    vibration = models.ForeignKey(Vibration, verbose_name='震動', on_delete=models.PROTECT, null=True)
    yarare = models.ForeignKey(Yarare, verbose_name='やられ', on_delete=models.PROTECT, null=True)
    jyotaiijyo = models.ForeignKey(JyotaiIjyo, verbose_name='状態異常', on_delete=models.PROTECT, null=True)

    # 弱点属性
    jyaku_hi = models.ForeignKey(Symbol, verbose_name='弱点属性_火' ,related_name='jyaku_hi' ,on_delete=models.PROTECT ,null=True)
    jyaku_mizu = models.ForeignKey(Symbol, verbose_name='弱点属性_水' ,related_name='jyaku_mizu' ,on_delete=models.PROTECT ,null=True)
    jyaku_kami = models.ForeignKey(Symbol, verbose_name='弱点属性_雷' ,related_name='jyaku_kami' ,on_delete=models.PROTECT ,null=True)
    jyaku_kori = models.ForeignKey(Symbol, verbose_name='弱点属性_氷' ,related_name='jyaku_kori' ,on_delete=models.PROTECT ,null=True)
    jyaku_ryu = models.ForeignKey(Symbol, verbose_name='弱点属性_龍' ,related_name='jyaku_ryu' ,on_delete=models.PROTECT ,null=True)
    # 状態異常耐性
    ijyo_doku = models.ForeignKey(Symbol, verbose_name='状態異常耐性_毒' ,related_name='ijyo_doku' ,on_delete=models.PROTECT ,null=True)
    ijyo_suimin = models.ForeignKey(Symbol, verbose_name='状態異常耐性_睡眠' ,related_name='ijyo_suimin' ,on_delete=models.PROTECT ,null=True)
    ijyo_mahi = models.ForeignKey(Symbol, verbose_name='状態異常耐性_麻痺' ,related_name='ijyo_mahi' ,on_delete=models.PROTECT ,null=True)
    ijyo_kizetsu = models.ForeignKey(Symbol, verbose_name='状態異常耐性_気絶' ,related_name='ijyo_kizetsu' ,on_delete=models.PROTECT ,null=True)
    ijyo_meki = models.ForeignKey(Symbol, verbose_name='状態異常耐性_滅気' ,related_name='ijyo_meki' ,on_delete=models.PROTECT ,null=True)
    ijyo_bakuha = models.ForeignKey(Symbol, verbose_name='状態異常耐性_爆破' ,related_name='ijyo_bakuha' ,on_delete=models.PROTECT ,null=True)
    ijyo_nori = models.ForeignKey(Symbol, verbose_name='状態異常耐性_乗り' ,related_name='ijyo_nori' ,on_delete=models.PROTECT ,null=True)
    # アイテム耐性
    item_senko = models.ForeignKey(Symbol, verbose_name='アイテム耐性_閃光' ,related_name='item_senko' ,on_delete=models.PROTECT ,null=True)
    item_otobaku = models.ForeignKey(Symbol, verbose_name='アイテム耐性_音爆' ,related_name='item_otobaku' ,on_delete=models.PROTECT ,null=True)
    item_koyashi = models.ForeignKey(Symbol, verbose_name='アイテム耐性_こやし玉' ,related_name='item_koyashi' ,on_delete=models.PROTECT ,null=True)
    item_shibire = models.ForeignKey(Symbol, verbose_name='アイテム耐性_シビレ罠' ,related_name='item_shibire' ,on_delete=models.PROTECT ,null=True)
    item_otoshi = models.ForeignKey(Symbol, verbose_name='アイテム耐性_落し穴' ,related_name='item_otoshi' ,on_delete=models.PROTECT ,null=True)
    item_tsuta = models.ForeignKey(Symbol, verbose_name='アイテム耐性_ツタ' ,related_name='item_tsuta' ,on_delete=models.PROTECT ,null=True)
    item_wananiku = models.ForeignKey(Symbol, verbose_name='アイテム耐性_罠肉' ,related_name='item_wananiku' ,on_delete=models.PROTECT ,null=True)

    def __str__(self):
        return self.name

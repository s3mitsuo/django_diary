from django.db import models
from mst_code.models import MstCode


class MstShikaku(models.Model):
    id = models.IntegerField(
        verbose_name = '自動キー'
    )
    sikaku_cd = models.CharField(
        max_length = 16,
        verbose_name = '資格コード'
    )
    sikaku_bunrui_cd1 = models.CharField(
        max_length = 3,
        verbose_name = '資格分類コード１'
    )
    sikaku_bunrui_cd2 = models.CharField(
        max_length = 3,
        verbose_name = '資格分類コード２'
    )
    sikaku_nm = models.CharField(
        max_length = 128,
        verbose_name = '資格名称（正式）'
    )
    sikaku_nm_syanai = models.CharField(
        max_length = 128,
        verbose_name = '資格名称（社内）'
    )
    sikaku_bunrui_nm1 = models.CharField(
        max_length = 128,
        verbose_name = '資格分類名称１'
    )
    syusai = models.CharField(
        max_length = 32,
        verbose_name = '主催'
    )
    sikaku_taisyo_kbn = models.CharField(
        max_length = 2,
        verbose_name = '対象職種区分',
        default = 10,
        choice = MstCode.TAISYO_SYOKUSYU_KBN_CHOICES,
    )
    point = models.IntegerField(
        verbose_name = '資格ポイント'
    )
    gijyutu_point = models.IntegerField(
        verbose_name = '技術ポイント'
    )
    gijyutu_flg = models.IntegerField(
        verbose_name = '技術フラグ',
        default = 0,
        choice = MstCode.TECH_FLG_CHOICES,
    )
    sikaku_bunrui_cd = models.CharField(
        max_length = 16,
        verbose_name = '資格分類コード',
        default = 'S999',
        choice = MstCode.SHIKAKU_BUNRUI_CD_CHOICES,
    )
    yuko_nensu = models.IntegerField(
        verbose_name = '有効年数'
    )
    hojyo_cmmt = models.CharField(
        max_length = 64,
        verbose_name = '受験料補助（コメント）'
    )
    siharai_cmmt = models.CharField(
        max_length = 64,
        verbose_name = '祝金支払（コメント）'
    )
    old_sikaku_cd = models.CharField(
        max_length = 16,
        verbose_name = '旧資格コード',
        default = 'S001',
        choice = MstCode.SHIKAKU_CD_CHOICES,
    )
    old_sikaku_bunrui_cd1 = models.CharField(
        max_length = 16,
        verbose_name = '旧資格分類コード１'
    )
    old_sikaku_bunrui_cd2 = models.CharField(
        max_length = 16,
        verbose_name = '旧資格分類コード２'
    )
    old_sikaku_nm_syanai = models.CharField(
        max_length = 128,
        verbose_name = '旧資格名称（社内）'
    )
    old_sikaku_bunrui_nm1 = models.CharField(
        max_length = 128,
        verbose_name = '旧資格分類名称１'
    )
    old_sikaku_syokusyu_kbn = models.CharField(
        max_length = 32,
        verbose_name = '旧資格対象職種区分'
    )
    old2_sikaku_cd = models.CharField(
        max_length = 16,
        verbose_name = '旧旧資格コード'
    )
    old2_sikaku_bunrui_cd1 = models.CharField(
        max_length = 16,
        verbose_name = '旧旧資格分類コード１'
    )
    biko = models.CharField(
        max_length = 128,
        verbose_name = '備考'
    )
    kakunin_user = models.CharField(
        max_length = 64,
        verbose_name = '確認者'
    )
    kakunin_date = models.DateTimeField(
        verbose_name = '確認日'
    )
    del_flg = models.IntegerField(
        verbose_name = '削除フラグ',
        default = 0,
        choice = MstCode.ONOFF_CHOICES,
    )
    create_user = models.CharField(
        max_length = 64,
        verbose_name = '作成者'
    )
    create_machine = models.CharField(
        max_length = 32,
        verbose_name = '作成端末'
    )
    create_date = models.DateTimeField(
        verbose_name = '作成日',
        default = now(),
    )
    update_program = models.CharField(
        max_length = 32,
        verbose_name = '更新プログラム'
    )
    update_user = models.CharField(
        max_length = 64,
        verbose_name = '更新者'
    )
    update_machine = models.CharField(
        max_length = 32,
        verbose_name = '更新端末'
    )
    update_date = models.DateTimeField(
        verbose_name = '更新日',
        default = now(),
    )
    def __str__(self):
        return MstShikaku


    class Meta:
        verbose_name = '資格マスタ'
        verbose_name_plural = '資格マスタ'


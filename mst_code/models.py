from django.db import models
from django.core import validators


# Create your models here.
class MstCode(models.Model):

    SEX_CHOICES = (
        (1, '男性'),
        (2, '女性'),
    )
    ONOFF_CHOICES = (
        (0, 'OFF'),
        (1, 'ON'),
    )
    GAKUREKI_KBN_CHOICES = (
        (1, '高校卒'),
        (2, '高専卒'),
        (3, '専門卒'),
        (4, '短大卒'),
        (5, '大学卒'),
        (6, '修士卒'),
        (7, '博士卒'),
    )
    SENKO_CHOICES = (
        (1, '理系'),
        (2, '文系'),
    )
    SYAIN_KBN_CHOICES = (
        (1, '取締役・監査役'),
        (2, '顧問・相談役'),
        (3, '正社員'),
        (4, '継続社員'),
        (5, '継続社内役員'),
        (6, '有期雇用社員'),
        (7, '無期雇用社員'),
        (8, '嘱託社員'),
        (9, 'その他社員'),
    )
    SAIYO_KBN_CHOICES = (
        (1, '新卒'),
        (2, '中途'),
        (3, '継続'),
        (4, '再雇用'),
        (5, '委任'),
    )
    SYOKUSYU_KBN_CHOICES = (
        (1, '技術'),
        (2, '営業'),
        (3, '事務'),
    )
    RANK_CHOICES = (
        (1, '１等級'),
        (2, '２等級'),
        (3, '３等級'),
        (4, '４等級'),
        (5, '５等級'),
        (6, '６等級'),
        (7, '７等級'),
        (8, '８等級'),
        (9, '９等級'),
        (10, 'Ａ等級'),
    )

    TAISYOKU_KBN_CHOICES = (
        (10, ''),
        (20, '自己都合（待遇不満）'),
        (21, '自己都合（他業界へ）'),
        (22, '自己都合（家族介護）'),
        (23, '自己都合（その他）'),
        (60, '休職期間満了'),
        (70, '移籍'),
        (80, '退職勧奨'),
        (90, '定年退職'),
    )

    KINMU_KBN_CHOICES = (
        (0, '通常勤務'),
        (1, '特定勤務'),
        (2, '特定勤務２'),
        (4, '時短４'),
        (5, '時短５'),
        (6, '時短６'),
        (7, '時短７'),
        (9, '休職'),
    )

    KINMUJOTAI_KBN_CHOICES = (
        (0, '通常勤務'),
        (1, '在宅勤務'),
        (2, '常駐勤務'),
        (3, '出張勤務'),
        (4, 'シフト勤務'),
        (5, '有給休暇'),
        (6, '半休'),
    )

    SYOBATSU_CHOICES = (
        (0, '罰'),
        (1, '賞'),
    )

    GOHI_CHOICES = (
        (0, '不合格'),
        (1, '合格'),
    )

    NAIGAI_CHOICES = (
        (0, '内'),
        (1, '外'),
    )

    HISSU_CHOICES = (
        (0, '不要'),
        (1, '必須'),
    )

    SOTSUGYO_CHOICES = (
        (0, '中退'),
        (1, '卒業'),
    )

    YAKUSYOKU_KBN_CHOICES = (
        (000, ''),
        (100, '統括'),
        (110, '社長'),
        (100, '副社長'),
        (100, '常務取締役'),
        (100, '取締役'),
        (100, '執行役員'),
        (100, '相談役'),
        (100, '監査役'),
        (200, '事業統括'),
        (210, '事業部長'),
        (220, '副事業部長'),
        (250, '事業部長付'),
        (300, '本部長'),
        (310, '副本部長'),
        (350, '本部長付'),
        (400, '室長'),
        (410, '副室長'),
        (500, '部長'),
        (100, '副部長'),
        (540, '担当部長'),
        (550, '部長付'),
        (600, '支社長'),
        (700, '所長'),
        (800, 'センター長'),
        (900, '課長'),
        (910, '副課長'),
        (920, '課長代行'),
        (930, '課長代理'),
        (1000, '上級高度技術者'),
        (1100, '高度技術者'),
        (1200, '高度営業者'),
        (1300, '高度事務者'),
        (1500, 'ＵＬ'),
    )

    KESSAI_KBN_CHOICES = (
        (00, ''),
        (10, 'ＵＬ'),
        (20, '課長'),
        (30, '部長'),
        (40, '事業部長'),
        (50, '統括'),
        (60, '社長'),
        (70, '役会'),
        (80, '取会'),
    )

    BUSYO_LVL_CHOICES = (
        (1, 'ユニット'),
        (2, '課・事業所'),
        (3, '部・支社'),
        (4, '事業部・本部'),
        (5, '統括'),
        (6, '全社'),
    )

    BUSYO_KBN_CHOICES = (
        (1, '事業部門'),
        (2, '管理部門'),
        (3, '研究部門'),
    )


    # 管理サイト上の表示設定
    def __str__(self):
        return self.cd


    class Meta:
        verbose_name = 'コードマスタ'

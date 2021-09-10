from django.contrib import admin
from .models import CustomUser


# カスタムユーザモデルを管理サイトに登録する
admin.site.register(CustomUser)

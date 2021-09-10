from django_filters import FilterSet
from django_filters import filters
from .models import MstShikaku


class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt ='%s 降順）'


class MstShikakuFilter(FilterSet):

    order_by = MyOrderingFilter(
        fields=('id' ,'sikaku_cd'         ),
        field_labels={'id': '自動キー','sikaku_cd': '資格コード'
                },
        label='並び順'
    )
    class Meta:
        model = MstShikaku
        fields = ('sikaku_cd' ,'sikaku_bunrui_cd1' ,'sikaku_nm'         )

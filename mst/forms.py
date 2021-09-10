from django import forms
from .models import MstBusyo


class MstShikakuForm(forms.ModelForm):

    class Meta:
        model = 'MstShikaku'
        fields = ('id'    ,'sikaku_cd'    ,'sikaku_bunrui_cd1'    
            ,'sikaku_bunrui_cd2'    ,'sikaku_nm'    ,'sikaku_nm_syanai'    
            ,'sikaku_bunrui_nm1'    ,'syusai'    ,'sikaku_taisyo_kbn'    
            ,'point'    ,'gijyutu_point'    ,'gijyutu_flg'    
            ,'sikaku_bunrui_cd'    ,'yuko_nensu'    ,'hojyo_cmmt'    
            ,'siharai_cmmt'    ,'del_flg'    )

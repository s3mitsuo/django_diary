from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = 'mst'
urlpatterns = [
    path('', views.MstShikakuIndexView.as_view(TemplateView), name='mstshikaku_index'),
    path('mstshikakusearch/', views.MstShikakuSearchView.as_view(), name='mstshikaku_search'),
    path('mstshikakufilter/', views.MstShikakuFilterView.as_view(), name='mstshikaku_filter'),
    path('mstshikakulist/', views.MstShikakuListView.as_view(), name='mstshikaku_list'),
    path('mstshikakucreat/', views.MstShikakuCreateView.as_view(), name='mstshikaku_create'),
    path('mstshikakuupdate/', views.MstShikakuUpdateView.as_view(), name='mstshikaku_update'),
    path('mstshikakudelete/', views.MstShikakuDeleteView.as_view(), name='mstshikaku_delete'),

]

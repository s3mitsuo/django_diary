from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView

from .models import MstShikaku
from .filters import MstShikakuFilter
from .forms import MstShikakuForm


class MstShikakuIndexView(TemplateView):
    template_name = 'mst/mstshikaku_index.html'


class MstShikakuSearchView(LoginRequiredMixin, FilterView):
    model = MstShikaku
    queryset = MstShikaku.objects.all().order_by('id')
    filterset_class = MstShikakuFilter
    strict = False
    template_name = 'mst/mstshikaku_search.html'
    paginate_by =10


    def get_queryset(self):
        items = MstShikaku.objects.all().order_by('id')
        return items


class MstShikakuFilterView(LoginRequiredMixin, FilterView):
    model = MstShikaku
    queryset = MstShikaku.objects.all().order_by('id')
    filterset_class = MstShikakuFilter
    strict = False
    template_name = 'mst/mstshikaku_filter.html'
    paginate_by =10


    def get(self, request, **kwargs):
        if request.GET:
            request.session['query'] = request.GET
        else:
            request.GET = request.GET.copy()
            if 'query' in request.session.keys():
                for key in request.session['query'].keys():
                    request.GET[key] = request.session['query'][key]

        super().get(request, **kwargs)


class MstShikakuListView(LoginRequiredMixin, ListView):
    model = MstShikaku
    queryset = MstShikaku.objects.all().order_by('id')
    filterset_class = MstShikakuFilter
    strict = False
    template_name = 'mst/mstshikaku_list.html'
    paginate_by =10


    def get_queryset(self):
        items = MstShikaku.objects.all().order_by('id')
        return items


class MstShikakuCreateView(LoginRequiredMixin, CreateView):
    model = MstShikaku
    form_class = MstShikakuForm
    success_url = reverse_lazy('mst:mstshikaku_search')


class MstShikakuUpdateView(LoginRequiredMixin, UpdateView):
    model = MstShikaku
    form_class = MstShikakuForm
    success_url = reverse_lazy('mst:mstshikaku_search')


class MstShikakuDeleteView(LoginRequiredMixin, DeleteView):
    model = MstShikaku
    success_url = reverse_lazy('mst:mstshikaku_search')

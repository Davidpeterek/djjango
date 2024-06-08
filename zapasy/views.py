from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Hrac, Zapas, Klub


def index(request):
    context = {
        'nadpis': 'Fotbal',
        'fotbaliste': Hrac.objects.order_by('-narozeni')[:4]
    }
    return render(request, 'index.html', context=context)


class KlubListView(ListView):
    model = Klub
    template_name ='kluby/list.html'
    context_object_name ='kluby'
    queryset = Klub.objects.order_by('nazev')


class KlubDetailView(DetailView):
    model = Klub
    template_name ='kluby/detail.html'
    context_object_name ='klub'

class ZapasListView(DetailView):
    model = Zapas
    template_name = 'zapas/zapas_list.html'
    context_object_name = 'zapas'
    ordering = ['-datum']
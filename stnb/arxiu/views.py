# -*- coding: utf-8 -*-
import datetime

from django.views.generic import ListView, DetailView, TemplateView

from stnb.seminaris.models import Seminari
from stnb.publicacions.models import Publicacio

class ArxiuListView(TemplateView):
    template_name = 'arxiu/llista.html'

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)

        seminaris = Seminari.objects.filter(data_finalizacio__lt=datetime.datetime.now)
        publicacions = Publicacio.objects.all()

        context.update({ 'seminaris': seminaris,
                         'publicacions': publicacions })

        return context


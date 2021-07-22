import sys
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, HttpResponseRedirect
from datetime import datetime, timedelta
from django.http import request
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import TemplateView

import yeast.forms.yeast_forms
from yeast.models.master_data_yeast import YeastLab
from yeast.models.master_data_yeast import Yeast
from yeast.models.master_data_yeast import YeastPitch
from yeast.models.master_data_yeast import Brink

class YeastLabListView(ListView):
    model = YeastLab
    template_name = 'yeast/lab/lab-list.html'
    context_object_name = 'yeast_lab_list'

    def get_queryset(self):
        return YeastLab.objects.order_by('yeast_lab_name')


class YeastLabCreateView(CreateView):
    model = YeastLab
    template_name = 'yeast/lab/lab-create.html'
    form_class = yeast.forms.yeast_forms.LabForm
    success_url = '/yeast/lab/list/'
    def get_context_data(self, **kwargs):
        context = super(YeastLabCreateView, self).get_context_data(**kwargs)
        context['page_name'] = 'Create Yeast Lab'
        return context
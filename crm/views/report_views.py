from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import TemplateView

from datetime import datetime, timedelta

import crm.forms.account_forms
from crm.models.crm_models import Account
from crm.models.crm_models import Call
from crm.forms.account_forms import AccountForm


class SalesWeeklyStatusView(TemplateView):
    model = Account
    template_name= 'crm/reports/sales-weekly-status.html'
    context_object_name = 'rpt'

    def get_context_data(self, **kwargs):
        context = super(SalesWeeklyStatusView, self).get_context_data(**kwargs)
        today = datetime.today()
        this_week_monday = today + timedelta(days=-today.weekday())
        context['page_name'] = 'All Accounts List'
        return context


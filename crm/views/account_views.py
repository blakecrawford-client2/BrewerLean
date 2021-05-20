from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import TemplateView

import crm.forms.account_forms
from crm.models.crm_models import Account
from crm.models.crm_models import Call
from crm.forms.account_forms import AccountForm


class AccountListView(ListView, LoginRequiredMixin):
    model = Account
    template_name= 'crm/accounts/account-list.html'
    context_object_name = 'accounts'

    def get_context_data(self, **kwargs):
        context = super(AccountListView, self).get_context_data(**kwargs)
        context['page_name'] = 'All Accounts List'
        return context


class AccountListsView(ListView, LoginRequiredMixin):
    model = Account
    template_name = 'crm/accounts/account-lists.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        accounts = Account.objects.all()
        context['accounts'] = accounts
        return context


class FindAccountForCallView(LoginRequiredMixin, ListView):
    model = Account
    template_name = 'crm/accounts/account_call_search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        accounts = Account.objects.all()
        context['accounts'] = accounts
        return context


class AccountDetailView(LoginRequiredMixin, DetailView):
    model = Account
    template_name = 'crm/accounts/account-detail.html'
    context_object_name = 'account'

    def get_context_data(self, **kwargs):
        context = super(AccountDetailView, self).get_context_data(**kwargs)
        try:
            calls = Call.objects.filter(account=self.kwargs.get('pk')).order_by('-schedule_week_monday', '-last_modified_on')
        except:
            calls = None
        context['page_name'] = 'Account Detail'
        context['calls'] = calls
        return context

class AccountUpdateView(LoginRequiredMixin, UpdateView):
    model = Account
    template_name = 'crm/accounts/account-create.html'
    form_class = AccountForm
    success_url = '/'

class AccountListOnPremView(AccountListView):

    def get_queryset(self):
        return Account.objects.filter(account_group='ON').order_by('account_name')

    def get_context_data(self, **kwargs):
        context = super(AccountListOnPremView, self).get_context_data(**kwargs)
        context['page_name'] = 'On-Prem, All'
        return context


class AccountListOnPremMaintenanceView(AccountListView):

    def get_queryset(self):
        return Account.objects.filter(account_group='ON', account_type='M').order_by('account_name')

    def get_context_data(self, **kwargs):
        context = super(AccountListOnPremMaintenanceView, self).get_context_data(**kwargs)
        context['page_name'] = 'On-Prem, Maintenance'
        return context


class AccountListOnPremAcquisitionView(AccountListView):

    def get_queryset(self):
        return Account.objects.filter(account_group='ON', account_type='A').order_by('account_name')

    def get_context_data(self, **kwargs):
        context = super(AccountListOnPremAcquisitionView, self).get_context_data(**kwargs)
        context['page_name'] = 'On-Prem, Acquisition'
        return context


class AccountListOnPremProspectView(AccountListView):

    def get_queryset(self):
        return Account.objects.filter(account_group='ON', account_type='P').order_by('account_name')

    def get_context_data(self, **kwargs):
        context = super(AccountListOnPremProspectView, self).get_context_data(**kwargs)
        context['page_name'] = 'On-Prem, Prospect'
        return context


class AccountListOnPremDeadView(AccountListView):

    def get_queryset(self):
        return Account.objects.filter(account_group='ON', account_type='D').order_by('account_name')

    def get_context_data(self, **kwargs):
        context = super(AccountListOnPremDeadView, self).get_context_data(**kwargs)
        context['page_name'] = 'On-Prem, Dead'
        return context


class AccountListOffPremView(AccountListView):

    def get_queryset(self):
        return Account.objects.filter(account_group='OF').order_by('account_name')

    def get_context_data(self, **kwargs):
        context = super(AccountListOffPremView, self).get_context_data(**kwargs)
        context['page_name'] = 'Off-Prem, All'
        return context


class AccountListOffPremMaintenanceView(AccountListView):

    def get_queryset(self):
        return Account.objects.filter(account_group='OF', account_type='M').order_by('account_name')

    def get_context_data(self, **kwargs):
        context = super(AccountListOffPremMaintenanceView, self).get_context_data(**kwargs)
        context['page_name'] = 'Off-Prem, Maintenance'
        return context


class AccountListOffPremAcquisitionView(AccountListView):

    def get_queryset(self):
        return Account.objects.filter(account_group='OF', account_type='A').order_by('account_name')

    def get_context_data(self, **kwargs):
        context = super(AccountListOffPremAcquisitionView, self).get_context_data(**kwargs)
        context['page_name'] = 'Off-Prem, Acquisition'
        return context


class AccountListOffPremProspectView(AccountListView):

    def get_queryset(self):
        return Account.objects.filter(account_group='OF', account_type='P').order_by('account_name')

    def get_context_data(self, **kwargs):
        context = super(AccountListOffPremProspectView, self).get_context_data(**kwargs)
        context['page_name'] = 'Off-Prem, Prospect'
        return context


class AccountListOffPremDeadView(AccountListView):

    def get_queryset(self):
        return Account.objects.filter(account_group='OF', account_type='D').order_by('account_name')

    def get_context_data(self, **kwargs):
        context = super(AccountListOffPremDeadView, self).get_context_data(**kwargs)
        context['page_name'] = 'Off-Prem, Dead'
        return context


class CreateAccountView(CreateView):
    model = Account
    template_name= 'crm/accounts/account-create.html'
    context_object_name = 'accounts'
    form_class = AccountForm
    success_url ='/'
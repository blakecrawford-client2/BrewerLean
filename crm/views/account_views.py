from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from common.views.BLViews import BLListView, BLCreateView, BLUpdateView, BLDetailView
from common.views.BLViews import IndexTemplateView
from crm.forms.account_forms import AccountForm
from crm.models.crm_models import Account
from crm.models.crm_models import Call
from crm.models.crm_models import Tasting


class CRMIndexView(IndexTemplateView):
    template_name = 'crm/home.html'


class AccountListView(BLListView, LoginRequiredMixin):
    model = Account
    template_name = 'crm/accounts/account-list.html'
    context_object_name = 'accounts'

    def get_context_data(self, **kwargs):
        context = super(AccountListView, self).get_context_data(**kwargs)
        context['page_name'] = 'All Accounts List'
        return context


class AccountListsView(BLListView, LoginRequiredMixin):
    model = Account
    template_name = 'crm/accounts/account-lists.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        accounts = Account.objects.all()
        context['accounts'] = accounts
        return context


class FindAccountForCallView(BLListView, LoginRequiredMixin):
    model = Account
    template_name = 'crm/accounts/account_call_search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        accounts = Account.objects.all()
        context['accounts'] = accounts
        return context


class AccountDetailView(BLDetailView, LoginRequiredMixin):
    model = Account
    template_name = 'crm/accounts/account-detail.html'
    context_object_name = 'account'

    def get_context_data(self, **kwargs):
        context = super(AccountDetailView, self).get_context_data(**kwargs)
        try:
            # bugfix
            # re-ordering calls w/ most recent at top, original call all the way at the bottom
            # sorting this by ID is wrong, but it seems as though the lack of a schedule week
            # on original calls is interpreted as the
            calls = Call.objects.filter(account=self.kwargs.get('pk')).order_by('-last_modified_on', '-id')
            for call in calls:
                if call.type is None and call.method is None and call.outcome is None:
                    context['open_call_exists'] = True
        except:
            calls = None
        tastings = Tasting.objects.filter(at_account=self.kwargs.get('pk')).order_by('-last_modified_on', '-id')

        context['page_name'] = 'Account Detail'
        context['calls'] = calls
        context['tastings'] = tastings
        return context


class AccountUpdateView(BLUpdateView, LoginRequiredMixin):
    model = Account
    template_name = 'crm/accounts/account-create.html'
    form_class = AccountForm
    success_url = '/crm/account-lists/'


class AccountListInTerritory(BLListView, LoginRequiredMixin):
    model = Account
    template_name = 'crm/accounts/account-lists.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        accounts = Account.objects.all()
        context['accounts'] = accounts
        return context


class AccountListOnPremView(AccountListView, LoginRequiredMixin):

    def get_queryset(self):
        return Account.objects.filter(account_group='ON').order_by('account_name')

    def get_context_data(self, **kwargs):
        context = super(AccountListOnPremView, self).get_context_data(**kwargs)
        context['page_name'] = 'On-Prem, All'
        return context


class AccountListOnPremMaintenanceView(AccountListView, LoginRequiredMixin):

    def get_queryset(self):
        return Account.objects.filter(account_group='ON', account_type='M').order_by('account_name')

    def get_context_data(self, **kwargs):
        context = super(AccountListOnPremMaintenanceView, self).get_context_data(**kwargs)
        context['page_name'] = 'On-Prem, Maintenance'
        return context


class AccountListOnPremAcquisitionView(AccountListView, LoginRequiredMixin):

    def get_queryset(self):
        return Account.objects.filter(account_group='ON', account_type='A').order_by('account_name')

    def get_context_data(self, **kwargs):
        context = super(AccountListOnPremAcquisitionView, self).get_context_data(**kwargs)
        context['page_name'] = 'On-Prem, Acquisition'
        return context


class AccountListOnPremProspectView(AccountListView, LoginRequiredMixin):

    def get_queryset(self):
        return Account.objects.filter(account_group='ON', account_type='P').order_by('account_name')

    def get_context_data(self, **kwargs):
        context = super(AccountListOnPremProspectView, self).get_context_data(**kwargs)
        context['page_name'] = 'On-Prem, Prospect'
        return context


class AccountListOnPremDeadView(AccountListView, LoginRequiredMixin):

    def get_queryset(self):
        return Account.objects.filter(account_group='ON', account_type='D').order_by('account_name')

    def get_context_data(self, **kwargs):
        context = super(AccountListOnPremDeadView, self).get_context_data(**kwargs)
        context['page_name'] = 'On-Prem, Dead'
        return context


class AccountListOffPremView(AccountListView, LoginRequiredMixin):

    def get_queryset(self):
        return Account.objects.filter(account_group='OF').order_by('account_name')

    def get_context_data(self, **kwargs):
        context = super(AccountListOffPremView, self).get_context_data(**kwargs)
        context['page_name'] = 'Off-Prem, All'
        return context


class AccountListOffPremMaintenanceView(AccountListView, LoginRequiredMixin):

    def get_queryset(self):
        return Account.objects.filter(account_group='OF', account_type='M').order_by('account_name')

    def get_context_data(self, **kwargs):
        context = super(AccountListOffPremMaintenanceView, self).get_context_data(**kwargs)
        context['page_name'] = 'Off-Prem, Maintenance'
        return context


class AccountListOffPremAcquisitionView(AccountListView, LoginRequiredMixin):

    def get_queryset(self):
        return Account.objects.filter(account_group='OF', account_type='A').order_by('account_name')

    def get_context_data(self, **kwargs):
        context = super(AccountListOffPremAcquisitionView, self).get_context_data(**kwargs)
        context['page_name'] = 'Off-Prem, Acquisition'
        return context


class AccountListOffPremProspectView(AccountListView, LoginRequiredMixin):

    def get_queryset(self):
        return Account.objects.filter(account_group='OF', account_type='P').order_by('account_name')

    def get_context_data(self, **kwargs):
        context = super(AccountListOffPremProspectView, self).get_context_data(**kwargs)
        context['page_name'] = 'Off-Prem, Prospect'
        return context


class AccountListOffPremDeadView(AccountListView, LoginRequiredMixin):

    def get_queryset(self):
        return Account.objects.filter(account_group='OF', account_type='D').order_by('account_name')

    def get_context_data(self, **kwargs):
        context = super(AccountListOffPremDeadView, self).get_context_data(**kwargs)
        context['page_name'] = 'Off-Prem, Dead'
        return context


class CreateAccountView(BLCreateView, LoginRequiredMixin):
    model = Account
    template_name = 'crm/accounts/account-create.html'
    context_object_name = 'accounts'
    form_class = AccountForm
    success_url = '/crm/account-lists/'

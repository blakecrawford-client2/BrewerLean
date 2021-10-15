import sys
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, HttpResponseRedirect
from datetime import datetime, timedelta
from django.http import request
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import TemplateView
from crm.models.crm_models import Call
from crm.models.crm_models import Account
from crm.forms.call_forms import CallForm
from crm.forms.call_forms import CallWizardForm


class CallsForAccountListView(LoginRequiredMixin, ListView):
    model = Call
    template_name = 'crm/calls/calls-for-account-list.html'
    context_object_name = 'calls'


class CreateCallView(LoginRequiredMixin, CreateView):
    model = Call
    template_name = 'crm/calls/call-generic-create.html'
    context_object_name = 'calls'
    form_class = CallForm
    success_url = '/'


class CreateCallWizardStep1View(LoginRequiredMixin, DetailView):
    model = Account
    template_name = 'crm/calls/wizard/1-call-type.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account'] = self.kwargs.get('pk')
        context['call'] = self.kwargs.get('cpk')
        return context

class CreateCallWizardStep2View(LoginRequiredMixin, DetailView):
    model = Account
    template_name = 'crm/calls/wizard/2-call-method.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = self.kwargs.get('type')
        context['account'] = self.kwargs.get('pk')
        context['call'] = self.kwargs.get('cpk')
        return context


class CreateCallWizardStep3View(LoginRequiredMixin, DetailView):
    model = Account
    template_name = 'crm/calls/wizard/3-call-outcome.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = self.kwargs.get('type')
        context['account'] = self.kwargs.get('pk')
        context['call'] = self.kwargs.get('cpk')
        context['method'] = self.kwargs.get('method')
        return context


class CreateCallWizardStep4View(LoginRequiredMixin, DetailView):
    model = Account
    template_name = 'crm/calls/wizard/4-call-followup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = self.kwargs.get('type')
        context['account'] = self.kwargs.get('pk')
        context['call'] = self.kwargs.get('cpk')
        context['method'] = self.kwargs.get('method')
        context['outcome'] = self.kwargs.get('outcome')
        return context


class CreateOpenCallExitAwaitResponse(LoginRequiredMixin, TemplateView):
    template_name = 'crm/accounts/account-detail.html'

    def dispatch(self, request, *args, **kwargs):
        if self.kwargs.get('cpk') is None:
            call = Call.objects.create_call(self.kwargs.get('pk'),
                                            self.kwargs.get('type'),
                                            self.kwargs.get('method'))
            return HttpResponseRedirect(reverse_lazy('call_list'))
        else:
            call = Call.objects.get(id=self.kwargs.get('cpk'))
            account = Account.objects.get(id=self.kwargs.get('pk'))
            call.account = account
            call.type = self.kwargs.get('type')
            call.method = self.kwargs.get('method')
            call.save()
            return HttpResponseRedirect(reverse_lazy('call_list'))


class CreateCallWizardStep5View(LoginRequiredMixin, CreateView):
    model = Call
    template_name = 'crm/calls/wizard/5-call-note.html'
    form_class = CallWizardForm

    def form_valid(self, form):
        account = Account.objects.get(id=self.kwargs.get('pk'))
        if self.kwargs.get('cpk') is None:
            if form.is_valid():
                instance = form.save(commit=False)
                instance.type = self.kwargs.get('type')
                instance.account = account
                instance.method = self.kwargs.get('method')
                instance.outcome = self.kwargs.get('outcome')
                instance.follow_up_delay = self.kwargs.get('fupweeks')
                instance.note = form.cleaned_data['note']
                instance.samples = form.cleaned_data['samples']
                instance.save()
        else:
            instance = Call.objects.get(id=self.kwargs.get('cpk'))
            if form.is_valid():
                instance.account = account
                instance.type = self.kwargs.get('type')
                instance.method = self.kwargs.get('method')
                instance.outcome = self.kwargs.get('outcome')
                instance.follow_up_delay = self.kwargs.get('fupweeks')
                instance.note = form.cleaned_data['note']
                instance.samples = form.cleaned_data['samples']
                instance.save()

        if self.kwargs.get('fupweeks') is not None:
            fupweeks = self.kwargs.get('fupweeks')
            parent_call = Call.objects.get(id=instance.id)
            today = datetime.today()
            this_week_monday = today + timedelta(days=-today.weekday())
            follow_up_monday = this_week_monday + timedelta(weeks=fupweeks)
            fup_call = Call.objects.create_fup_call(account.id, follow_up_monday, parent_call)

        return super().form_valid(instance)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = self.kwargs.get('type')
        context['account'] = self.kwargs.get('pk')
        context['call'] = self.kwargs.get('cpk')
        context['method'] = self.kwargs.get('method')
        context['outcome'] = self.kwargs.get('outcome')
        context['fupweeks'] = self.kwargs.get('fupweeks')
        return context

    def get_success_url(self):
        return '/crm/calls/list/'


class CallsListView(LoginRequiredMixin, ListView):
    model = Call
    template_name= 'crm/calls/call-lists.html'
    context_object_name = 'calls'

    def get_context_data(self, **kwargs):
        current_user = self.request.user

        today = datetime.today()
        this_week_monday = today + timedelta(days=-today.weekday())
        next_week_monday = this_week_monday + timedelta(weeks=1)

        context = super(CallsListView, self).get_context_data(**kwargs)
        context['page_name'] = 'Calls List'
        #open_calls = Call.objects.filter(account__ale_owner=current_user, type__isnull=False, outcome__isnull=True)
        overdue_calls = Call.objects.filter(account__ale_owner=current_user, schedule_week_monday__lt=this_week_monday, outcome__isnull=True).order_by('account__account_name')
        original_calls = Call.objects.filter(account__ale_owner=current_user, type__isnull=False, outcome__isnull=True).order_by('account__account_name')
        follow_up_this_week_calls = Call.objects.filter(account__ale_owner=current_user, schedule_week_monday=this_week_monday, type__isnull=True,  outcome__isnull=True).order_by('account__account_name')
        follow_up_next_week_calls = Call.objects.filter(account__ale_owner=current_user, schedule_week_monday=next_week_monday, type__isnull=True, outcome__isnull=True).order_by('account__account_name')
        #context['open_calls'] = open_calls
        context['overdue_calls'] = overdue_calls
        context['original_calls'] = original_calls
        context['fup_this_week'] = follow_up_this_week_calls
        context['fup_next_week'] = follow_up_next_week_calls
        return context


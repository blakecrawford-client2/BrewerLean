from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime, timedelta
from django.views.generic import ListView
from common.views.BLViews import BLCreateView, BLUpdateView
from ebs.models.brew_sheets import Batch
from ebs.models.brew_sheets import BatchPlanDates, BatchActualDates
from ebs.forms.batch_upcoming_forms import MakeUpcomingBatchForm
from ebs.forms.batch_upcoming_forms import StartUpcomingBatchForm


class UpcomingBatchList(LoginRequiredMixin, ListView):
    model = Batch
    template_name = 'ebs/batch/upcoming-batch-list.html'
    context_object_name = 'upcoming_batch_list'

    def get_queryset(self):
        return Batch.objects.filter(status='PL').order_by('plan_start_day')


class UpcomingBatchCreateView(LoginRequiredMixin, BLCreateView):
    model = Batch
    template_name = 'ebs/batch/upcoming-batch-create-or-update.html'
    form_class = MakeUpcomingBatchForm
    success_url = '/ebs/upcoming/'

    def form_valid(self, form):
        form.fields['last_modified_by'] = self.request.user.id
        m = form.save(self)
        return HttpResponseRedirect(self.success_url)


class UpcomingBatchUpdateView(LoginRequiredMixin, BLUpdateView):
    model = Batch
    template_name = "ebs/batch/upcoming-batch-create-or-update.html"
    form_class = MakeUpcomingBatchForm
    success_url = '/ebs/upcoming/'
    context_object_name = 'upcoming_batch_list'

    def form_valid(self, form):
        form.fields['last_modified_by'] = self.request.user.id
        m = form.save(self)
        return HttpResponseRedirect(self.success_url)


class UpcomingBatchStartView(LoginRequiredMixin, BLUpdateView):
    model = Batch
    template_name = "ebs/batch/upcoming-batch-start.html"
    form_class = StartUpcomingBatchForm
    success_url = '/ebs/inprocess/'

    def form_valid(self, form):
        if form.is_valid():
            instance = form.save(commit=False)
            instance.status = 'IP'
            instance.last_modified_by = self.request.user.id
            instance.save()
        spattern = form.cleaned_data['schedule_pattern']
        self.calculate_plan_days(instance, spattern)
        self.set_actual_start_day(instance, spattern)

        return HttpResponseRedirect(self.success_url)

    def calculate_plan_days(self, instance, spattern):
        start_date = datetime.today()
        plan_dates = BatchPlanDates.create(instance)
        plan_dates.brew_date = start_date
        plan_dates.yeast_crash_date = start_date + timedelta(days=spattern.offset_yeast_crash)
        plan_dates.yeast_harvest_date = start_date + timedelta(days=spattern.offset_yeast_harvest)
        plan_dates.dryhop_date = start_date + timedelta(days=spattern.offset_dryhop)
        plan_dates.final_crash_date = start_date + timedelta(days=spattern.offset_final_crash)
        plan_dates.transfer_date = start_date + timedelta(days=spattern.offset_transfer)
        plan_dates.package_date = start_date + timedelta(days=spattern.offset_package)
        plan_dates.save()
        return

    def set_actual_start_day(self, instance, spattern):
        act_dates = BatchActualDates.create(instance)
        act_dates.brew_date = datetime.today()
        act_dates.save()
        return

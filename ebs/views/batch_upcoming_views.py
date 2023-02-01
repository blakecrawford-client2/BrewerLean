import logging
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime, timedelta
from django.views.generic import ListView
from common.views.BLViews import BLCreateView, BLUpdateView, BLDetailView
from common.views.BLViews import BLDeleteWithoutConfirmationView
from ebs.models.brew_sheets import Batch
from ebs.models.brew_sheets import BatchPlanDates, BatchActualDates
from ebs.models.brew_sheets import BatchPackagePlan
from ebs.forms.batch_upcoming_forms import MakeUpcomingBatchForm
from ebs.forms.batch_upcoming_forms import StartUpcomingBatchForm
from ebs.forms.batch_upcoming_forms import UpcomingBatchPkgPlanForm

###
# See a list of upcoming (not started) batches
class UpcomingBatchList(LoginRequiredMixin, ListView):
    model = Batch
    template_name = 'ebs/batch/upcoming-batch-list.html'
    context_object_name = 'upcoming_batch_list'

    def get_queryset(self):
        return Batch.objects.filter(status='PL').order_by('plan_start_day')


###
# Create a new upcoming batch
class UpcomingBatchCreateView(LoginRequiredMixin, BLCreateView):
    model = Batch
    template_name = 'ebs/batch/upcoming-batch-create-or-update.html'
    form_class = MakeUpcomingBatchForm
    success_url = '/ebs/upcoming/'

    def form_valid(self, form):
        form.fields['last_modified_by'] = self.request.user.id
        m = form.save(self)
        return HttpResponseRedirect(self.success_url)


###
# Update the batch-level data for an upcoming batch
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


###
# Wholly delete an upcoming batch
class UpcomingBatchDeleteView(LoginRequiredMixin, BLDeleteWithoutConfirmationView):
    model = Batch
    success_url = '/ebs/upcoming/'

    template_name = "common/common_confirm_delete.html"


###
# Upcoming batch detail
class UpcomingBatchDetailView(LoginRequiredMixin, BLDetailView):
    model = Batch
    template_name = 'ebs/batch/upcoming_batch_detail.html'

    def get_context_data(self, **kwargs):
        context = super(UpcomingBatchDetailView, self).get_context_data(**kwargs)
        try:
            package_plan = BatchPackagePlan.objects.get(batch__id=self.kwargs.get('pk'))
        except:
            package_plan = None
        if package_plan:
            total_kegs = package_plan.kg_half_owned \
                + package_plan.kg_half_oneway \
                + package_plan.kg_sixth_owned \
                + package_plan.kg_sixth_oneway \
                + package_plan.kg_half_client \
                + package_plan.kg_half_client_oneway \
                + package_plan.kg_sixth_client \
                + package_plan.kg_sixth_client_oneway
            total_half = package_plan.kg_half_owned + package_plan.kg_half_oneway + package_plan.kg_half_client + package_plan.kg_half_client_oneway
            total_sixth = package_plan.kg_sixth_owned + package_plan.kg_sixth_oneway + package_plan.kg_sixth_client + package_plan.kg_sixth_client_oneway
            total_ale_half = package_plan.kg_half_owned + package_plan.kg_half_oneway
            total_client_half = package_plan.kg_half_client + package_plan.kg_half_client_oneway
            total_ale_sixth = package_plan.kg_sixth_owned + package_plan.kg_sixth_oneway
            total_client_sixth = package_plan.kg_sixth_client + package_plan.kg_sixth_client_oneway

            total_pkg_vol = ((total_half * 15.5) \
                + (total_sixth * 5.2) \
                + (package_plan.cs_12oz * 2.25) \
                + (package_plan.cs_16oz * 3) \
                + (package_plan.cs_500ml * 1.58) \
                + (package_plan.cs_750ml * 2.38))/31

            context['total_kegs'] = total_kegs
            context['total_half'] = total_half
            context['total_sixth'] = total_sixth
            context['total_ale_half'] = total_ale_half
            context['total_client_half'] = total_client_half
            context['total_ale_sixth'] = total_ale_sixth
            context['total_client_sixth'] = total_client_sixth
            context['total_pkg_vol'] = total_pkg_vol


        batch = self.get_object()
        product = batch.batch_product

        try:
            base_yield = product.ops_info.first().default_package_yield
        except:
            base_yield = 80.0

        logging.info("INFORMATION")
        logging.info(base_yield)

        base_vol = float(batch.total_batch_size.batch_size_name) * (float(base_yield) / 100.0)
        context['base_yield'] = base_yield
        context['base_vol'] = base_vol
        if package_plan:
            context['total_plan_yield'] = (float(total_pkg_vol) / float(batch.total_batch_size.batch_size_name))*100
        else:
            context['total_plan_yield'] = 'NaN'
        context['package_plan'] = package_plan
        return context


###
# Start an upcoming batch, which is to say--change the status
# to in-process, calculate the plan days, and set the ACTUAL
# start day
class UpcomingBatchStartView(LoginRequiredMixin, BLUpdateView):
    model = Batch
    template_name = "ebs/batch/upcoming-batch-start.html"
    form_class = StartUpcomingBatchForm
    success_url = '/ebs/inprocess/'

    def form_valid(self, form):
        form.fields['last_modified_by'] = self.request.user.id
        if form.is_valid():
            instance = form.save(commit=False)
            instance.status = 'IP'
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


class UpcomingBatchPkgPlanCreateView(LoginRequiredMixin, BLCreateView):
    model = BatchPackagePlan
    template_name = 'ebs/batch/upcoming_batch_pkgplan_create.html'
    form_class = UpcomingBatchPkgPlanForm

    def get_success_url(self):
        if ('/detail/' in self.request.get_full_path()):
            success_url = '/ebs/upcoming/detail/' + str(self.kwargs.get('bpk'))
        else:
            success_url = '/ebs/upcoming/'
        return success_url

    def form_valid(self, form):
        form.instance.batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        return super(UpcomingBatchPkgPlanCreateView, self).form_valid(form)


class UpcomingBatchPkgPlanUpdateView(LoginRequiredMixin, BLUpdateView):
    model = BatchPackagePlan
    template_name = 'ebs/batch/upcoming_batch_pkgplan_create.html'
    form_class = UpcomingBatchPkgPlanForm

    def get_success_url(self):
        if ('/detail/' in self.request.get_full_path()):
            success_url = '/ebs/upcoming/detail/' + str(self.kwargs.get('bpk'))
        else:
            success_url = '/ebs/upcoming/'
        return success_url

    def form_valid(self, form):
        form.instance.batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        return super(UpcomingBatchPkgPlanUpdateView, self).form_valid(form)
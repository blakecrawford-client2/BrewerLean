from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView
from common.views.BLViews import BLCreateView, BLUpdateView
from ebs.models.brew_sheets import Batch
from ebs.models.brew_sheets import BatchPlanDates
from ebs.models.brew_sheets import BatchActualDates
from ebs.models.brew_sheets import BatchYeastPitch
from ebs.models.brew_sheets import BatchDOEntry
from ebs.models.brew_sheets import BatchTransfer
from ebs.models.brew_sheets import CarbonationQCEntry
from ebs.models.brew_sheets import PackagingRun
from ebs.models.brew_sheets import BatchPackagePlan
from ebs.forms.batch_upcoming_forms import MakeUpcomingBatchForm
from ebs.forms.batch_maintenance_detail_forms import InProcessBatchPkgPlanForm

###
# See a full list of in-process batches
class InprocessBatchList(LoginRequiredMixin, ListView):
    model = Batch
    template_name = 'ebs/batch/inprocess-batch-list.html'
    context_object_name = 'inprocess_batch_list'

    def get_queryset(self):
        #return Batch.objects.filter(status='IP').order_by('-plan_start_day').select_related(BatchActualDates)
        #return Batch.objects.filter(status='IP').select_related(BatchActualDates).order_by('-plan_start_day')
        return Batch.objects.filter(status='IP', batchactualdates__isnull=False).order_by('-plan_start_day')


##
# Start a batch, meaning take an upcoming batch and change
# the status
class InprocessBatchCreateView(LoginRequiredMixin, BLCreateView):
    model = Batch
    template_name = 'ebs/batch/inprocess-batch-create-or-update.html'
    form_class = MakeUpcomingBatchForm
    success_url = '/inprocess-batch-list/'
    context_object_name = 'inprocess_batch_list'

###
# Update the batch-level information on an in-process batch
class InprocessBatchUpdateView(LoginRequiredMixin, BLUpdateView):
    model = Batch
    template_name = "ebs/inprocess-batch-create-or-update.html"
    form_class = MakeUpcomingBatchForm
    success_url = '/inprocess-batch-list/'
    context_object_name = 'inprocess_batch_list'

###
# Detail view to show the full batch screen with all of the
# current information and process buttons
class InprocessBatchDetailView(LoginRequiredMixin, TemplateView):
    template_name = "ebs/batch/inprocess/inprocess-beer-main.html"

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('pk'))
        plan_dates = BatchPlanDates.objects.get(batch=batch.id)
        act_dates = BatchActualDates.objects.get(batch=batch.id)
        try:
            yeast = BatchYeastPitch.objects.get(batch=batch.id)
        except BatchYeastPitch.DoesNotExist:
            yeast = None
        try:
            xfer = BatchTransfer.objects.get(batch=batch.id)
        except BatchTransfer.DoesNotExist:
            xfer = None
        try:
            carb = CarbonationQCEntry.objects.get(batch=batch.id)
        except CarbonationQCEntry.DoesNotExist:
            carb = None
        try:
            packaging = PackagingRun.objects.get(batch=batch.id)
        except PackagingRun.DoesNotExist:
            packaging = None
        try:
            package_plan = BatchPackagePlan.objects.get(batch=batch.id)
        except BatchPackagePlan.DoesNotExist:
            package_plan = None

        context = super(InprocessBatchDetailView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['plan_dates'] = plan_dates
        context['act_dates'] = act_dates
        context['yeast'] = yeast
        context['xfer'] = xfer
        context['carb'] = carb
        context['packaging'] = packaging
        context['package_plan'] = package_plan
        return context


class InProcessBatchPkgPlanCreateView(LoginRequiredMixin, BLCreateView):
    model = BatchPackagePlan
    template_name = 'ebs/batch/inprocess/detail/inprocess_batch_pkgplan_adjust.html'
    form_class = InProcessBatchPkgPlanForm

    def get_success_url(self):
        if ('/detail/' in self.request.get_full_path()):
            success_url = '/ebs/inprocess/detail/' + str(self.kwargs.get('bpk')) + '/pkgplanline/'
        else:
            success_url = '/ebs/inprocess/'
        return success_url

    def form_valid(self, form):
        form.instance.batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        return super(InProcessBatchPkgPlanCreateView, self).form_valid(form)


class InProcessBatchPkgPlanUpdateView(LoginRequiredMixin, BLUpdateView):
    model = BatchPackagePlan
    template_name = 'ebs/batch/inprocess/detail/inprocess_batch_pkgplan_adjust.html'
    form_class = InProcessBatchPkgPlanForm

    def get_success_url(self):
        if ('/detail/' in self.request.get_full_path()):
            success_url = '/ebs/inprocess/detail/' + str(self.kwargs.get('bpk')) + '/pkgplanline/'
        else:
            success_url = '/ebs/inprocess/'
        return success_url

    def form_valid(self, form):
        form.instance.batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        return super(InProcessBatchPkgPlanUpdateView, self).form_valid(form)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic import TemplateView
from common.views.BLViews import BLUpdateView
from ebs.models.brew_sheets import Batch
from ebs.models.brew_sheets import BatchPlanDates
from ebs.models.brew_sheets import BatchActualDates
from ebs.models.brew_sheets import BatchYeastPitch
from ebs.models.brew_sheets import BatchDOEntry
from ebs.models.brew_sheets import BatchTransfer
from ebs.models.brew_sheets import CarbonationQCEntry
from ebs.models.brew_sheets import PackagingRun
from ebs.forms.batch_close_forms import CloseBatchForm

###
# Convenience view for listing archived batches.
class ArchiveBatchListView(LoginRequiredMixin, ListView):
    model = Batch
    template_name = 'ebs/batch/archive-batch-list.html'
    context_object_name = 'archive_batch_list'

    def get_queryset(self):
        return Batch.objects.filter(status='AR').order_by('-plan_start_day')

###
# See an archived batch
class ArchiveBatchView(LoginRequiredMixin, BLUpdateView):
    model = Batch
    template_name = "ebs/batch/inprocess/detail/inprocess-add-subitem.html"
    form_class = CloseBatchForm
    success_url = '/ebs/archive/'

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('pk'))
        context = super(ArchiveBatchView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['name'] = 'Close Batch'
        return context

###
# Archived batch with all the deets.
class ArchiveBatchFullView(LoginRequiredMixin, TemplateView):
    template_name = "ebs/batch/archive-beer-main.html"

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

        context = super(ArchiveBatchFullView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['plan_dates'] = plan_dates
        context['act_dates'] = act_dates
        context['yeast'] = yeast
        context['xfer'] = xfer
        context['carb'] = carb
        context['packaging'] = packaging

        return context
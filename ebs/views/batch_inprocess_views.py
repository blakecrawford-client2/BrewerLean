from django.views.generic import ListView, TemplateView
from common.views.BLViews import BLCreateView, BLUpdateView
from ebs.models.master_data_products import Product
from ebs.models.brew_sheets import Batch
from ebs.models.brew_sheets import BatchPlanDates
from ebs.models.brew_sheets import BatchActualDates
from ebs.models.brew_sheets import BatchYeastPitch
from ebs.models.brew_sheets import BatchDOEntry
from ebs.models.brew_sheets import BatchTransfer
from ebs.models.brew_sheets import CarbonationQCEntry
from ebs.models.brew_sheets import PackagingRun
from ebs.forms.batch_upcoming_forms import MakeUpcomingBatchForm

class InprocessBatchList(ListView):
    model = Batch
    template_name = 'ebs/batch/inprocess-batch-list.html'
    context_object_name = 'inprocess_batch_list'

    def get_queryset(self):
        return Batch.objects.filter(status='IP')

class InprocessBatchCreateView(BLCreateView):
    model = Batch
    template_name = 'ebs/batch/inprocess-batch-create-or-update.html'
    form_class = MakeUpcomingBatchForm
    success_url = '/inprocess-batch-list/'
    context_object_name = 'inprocess_batch_list'

class InprocessBatchUpdateView(BLUpdateView):
    model = Batch
    template_name = "ebs/inprocess-batch-create-or-update.html"
    form_class = MakeUpcomingBatchForm
    success_url = '/inprocess-batch-list/'
    context_object_name = 'inprocess_batch_list'

class InprocessBatchDetailView(TemplateView):
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

        context = super(InprocessBatchDetailView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['plan_dates'] = plan_dates
        context['act_dates'] = act_dates
        context['yeast'] = yeast
        context['xfer'] = xfer
        context['carb'] = carb
        context['packaging'] = packaging

        return context
from django.views.generic import DetailView
from django.views.generic import TemplateView
from django.views.generic import ListView
from ebs.models.brew_sheets import Batch
from ebs.models.brew_sheets import BatchRawMaterialsLog
from ebs.models.brew_sheets import BatchWortQC
from ebs.models.brew_sheets import BatchYeastPitch
from ebs.models.brew_sheets import BatchPlanDates
from ebs.models.brew_sheets import BatchActualDates
from ebs.models.brew_sheets import BatchFermentationQC
from ebs.models.brew_sheets import BatchDOEntry
from ebs.models.brew_sheets import BatchTransfer
from ebs.models.brew_sheets import CarbonationQCEntry
from ebs.models.brew_sheets import CanningQC
from ebs.models.brew_sheets import PackagingRun
from ebs.models.brew_sheets import BatchNote


class BigTVStatusReport(ListView):
    model = Batch
    context_object_name = 'batches'
    template_name = 'ebs/batch/reports/big-tv-status-report.html'

    def get_queryset(self):
        return Batch.objects.filter(status='IP').order_by('target_fv')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plan_dates'] = BatchPlanDates.objects.filter(batch__status='IP')
        context['act_dates'] = BatchActualDates.objects.filter(batch__status='IP')
        return context


class BatchWortProductionRecord(DetailView):
    model = Batch
    context_object_name = 'batch'
    template_name = 'ebs/batch/reports/batch-wort-production-record.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        batch_id = self.kwargs.get('pk')
        context['plan_dates'] = BatchPlanDates.objects.get(batch=batch_id)
        context['act_dates'] = BatchActualDates.objects.get(batch=batch_id)
        context['wort_qc'] = BatchWortQC.objects.filter(batch=batch_id)
        context['yeast'] = BatchYeastPitch.objects.get(batch=batch_id)
        return context


class BatchRawMaterialsRecord(DetailView):
    model = Batch
    context_object_name = 'batch'
    template_name = 'ebs/batch/reports/batch-raw-materials-record.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        batch_id = self.kwargs.get('pk')
        context['materials'] = BatchRawMaterialsLog.objects.filter(batch=batch_id)
        context['grain'] = BatchRawMaterialsLog.objects.filter(batch=batch_id, material__material_type='GR')
        context['hops'] = BatchRawMaterialsLog.objects.filter(batch=batch_id, material__material_type='HP')
        context['other'] = BatchRawMaterialsLog.objects.filter(batch=batch_id, material__material_type='OT')
        return context


class BatchFermentationQCRecord(DetailView):
    model = Batch
    context_object_name = 'batch'
    template_name = 'ebs/batch/reports/batch-ferm-qc-record.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        batch_id = self.kwargs.get('pk')
        context['fermqcs'] = BatchFermentationQC.objects.filter(batch=batch_id)
        return context


class OldSchoolBrewSheet(DetailView):
    model = Batch
    context_object_name = 'batch'
    template_name = 'ebs/batch/reports/old-school-brew-sheet.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        batch_id = self.kwargs.get('pk')
        context['plan_dates'] = BatchPlanDates.objects.get(batch=batch_id)
        context['act_dates'] = BatchActualDates.objects.get(batch=batch_id)
        context['wort_qc'] = BatchWortQC.objects.filter(batch=batch_id)
        context['yeast'] = BatchYeastPitch.objects.filter(batch=batch_id)
        context['ferm'] = BatchFermentationQC.objects.filter(batch=batch_id)
        context['notes'] = BatchNote.objects.filter(batch=batch_id)
        return context


class TankStatusReport(ListView):
    model = Batch
    context_object_name = 'batches'
    template_name = 'ebs/batch/reports/tank-status-report.html'

    def get_queryset(self):
        return Batch.objects.filter(status='IP').order_by('target_fv')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['upcoming_batches'] = Batch.objects.filter(status='PL')
        context['batch_transfers'] = BatchTransfer.objects.filter(batch__status='IP')
        return context


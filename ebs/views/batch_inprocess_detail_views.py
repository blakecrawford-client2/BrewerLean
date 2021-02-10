from django.urls import reverse_lazy
from common.views.BLViews import BLCreateView, BLUpdateView
from ebs.models.brew_sheets import Batch
from ebs.models.brew_sheets import BatchRawMaterialsLog
from ebs.models.brew_sheets import BatchWortQC
from ebs.models.brew_sheets import BatchYeastPitch
from ebs.models.brew_sheets import BatchPlanDates
from ebs.models.brew_sheets import BatchActualDates
from ebs.models.brew_sheets import BatchFermentationQC
from ebs.forms.batch_maintenance_detail_forms import AddObeerDataForm
from ebs.forms.batch_maintenance_detail_forms import AddRawMaterialsForm
from ebs.forms.batch_maintenance_detail_forms import AddWortQCEntryForm
from ebs.forms.batch_maintenance_detail_forms import AddYeastPitchEntryForm
from ebs.forms.batch_maintenance_detail_forms import UpdateActualDatesForm
from ebs.forms.batch_maintenance_detail_forms import BatchFermentationQCForm

class AddObeerDataView(BLUpdateView):
    model = Batch
    template_name = 'ebs/batch/inprocess/maintenance_create_or_update.html'
    form_class = AddObeerDataForm
    context_object_name = 'current_batch'

    def get_success_url(self):
        return reverse_lazy('maintenance', kwargs={'pk': self.object.pk})

class RawMaterialsLogView(BLUpdateView):
    model = Batch
    template_name = 'ebs/batch/inprocess/detail/inprocess-rawmaterialslog.html'
    form_class = AddRawMaterialsForm
    context_object_name = 'current_batch'

    def get_success_url(self):
        return reverse_lazy('maintenance', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('pk'))
        materials = BatchRawMaterialsLog.objects.filter(batch=batch.id)
        context = super(RawMaterialsLogView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['materials'] = materials
        return context


class AddRawMaterialsLogView(BLCreateView):
    model = BatchRawMaterialsLog
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = AddRawMaterialsForm
    context_object_name = 'current_material'

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('pk'))
        context = super(AddRawMaterialsLogView, self).get_context_data(**kwargs)
        context['batch'] = batch
        return context

    def get_success_url(self):
        return reverse_lazy('rawmaterials', kwargs={'pk': self.kwargs.get('pk')})

    def form_valid(self, form):
        form.instance.batch = Batch.objects.get(pk=self.kwargs.get('pk'))
        return super(AddRawMaterialsLogView, self).form_valid(form)

class WortQCEntriesView(BLUpdateView):
    model = Batch
    template_name = 'ebs/batch/inprocess/detail/inprocess-wortqcentry.html'
    form_class = AddWortQCEntryForm
    context_object_name = 'batch'

    def get_success_url(self):
        return reverse_lazy('maintenance', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        batch_id = self.kwargs.get('pk')
        batch = Batch.objects.get(pk=batch_id)
        wortQCEntries = BatchWortQC.objects.filter(batch=batch.id)
        context = super(WortQCEntriesView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['wortqcentries'] = wortQCEntries
        return context

class AddWortQCEntryView(BLCreateView):
    model = BatchWortQC
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = AddWortQCEntryForm
    context_object_name = 'current_wortqc'

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        context = super(AddWortQCEntryView, self).get_context_data(**kwargs)
        context['batch'] = batch
        return context

    def get_success_url(self):
        return reverse_lazy('wortqcentries', kwargs={'pk': self.kwargs.get('bpk')})

    def form_valid(self, form):
        form.instance.batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        return super(AddWortQCEntryView, self).form_valid(form)

class UpdateWortQCEntryView(BLUpdateView):
    model = BatchWortQC
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = AddWortQCEntryForm
    context_object_name = 'current_wortqc'

    def get_success_url(self):
        return reverse_lazy('wortqcentries', kwargs={'pk': self.kwargs.get('bpk')})

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        context = super(UpdateWortQCEntryView, self).get_context_data(**kwargs)
        context['batch'] = batch
        return context

class CreateYeastPitchView(BLCreateView):
    model = BatchYeastPitch
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = AddYeastPitchEntryForm
    context_object_name = 'current_wortqc'

    def get_success_url(self):
        return reverse_lazy('maintenance', kwargs={'pk': self.kwargs.get('bpk')})

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        context = super(CreateYeastPitchView, self).get_context_data(**kwargs)
        context['batch'] = batch
        return context

    def form_valid(self, form):
        form.instance.batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        return super(CreateYeastPitchView, self).form_valid(form)

class UpdateYeastPitchView(BLUpdateView):
    model = BatchYeastPitch
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = AddYeastPitchEntryForm
    context_object_name = 'current_wortqc'

    def get_success_url(self):
        return reverse_lazy('maintenance', kwargs={'pk': self.kwargs.get('bpk')})

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        context = super(UpdateYeastPitchView, self).get_context_data(**kwargs)
        context['batch'] = batch
        return context

    def form_valid(self, form):
        form.instance.batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        return super(UpdateYeastPitchView, self).form_valid(form)

class UpdateActualDatesView(BLUpdateView):
    model = BatchActualDates
    template_name = 'ebs/batch/inprocess/detail/inprocess-update-actdates.html'
    form_class = UpdateActualDatesForm
    context_object_name = 'current_actdates'

    def get_success_url(self):
        return reverse_lazy('maintenance', kwargs={'pk': self.kwargs.get('bpk')})

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        plan_dates = BatchPlanDates.objects.get(batch=batch)
        context = super(UpdateActualDatesView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['plan_dates'] = plan_dates
        return context

    def form_valid(self, form):
        form.instance.batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        return super(UpdateActualDatesView, self).form_valid(form)

class FermQCEntriesView(BLUpdateView):
    model = Batch
    template_name = 'ebs/batch/inprocess/detail/inprocess-fermqcentry.html'
    form_class = BatchFermentationQCForm
    context_object_name = 'batch'

    def get_success_url(self):
        return reverse_lazy('maintenance', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        batch_id = self.kwargs.get('pk')
        batch = Batch.objects.get(pk=batch_id)
        try:
            fermQCEntries = BatchFermentationQC.objects.filter(batch=batch.id)
        except BatchFermentationQC.DoesNotExist:
            fermQCEntries = None
        context = super(FermQCEntriesView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['fermqcentries'] = fermQCEntries
        return context

class AddFermQCEntryView(BLCreateView):
    model = BatchFermentationQC
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = BatchFermentationQCForm
    context_object_name = 'current_wortqc'

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        context = super(AddFermQCEntryView, self).get_context_data(**kwargs)
        context['batch'] = batch
        return context

    def get_success_url(self):
        return reverse_lazy('fermqcentries', kwargs={'pk': self.kwargs.get('bpk')})

    def form_valid(self, form):
        form.instance.batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        return super(AddFermQCEntryView, self).form_valid(form)

class UpdateFermQCEntryView(BLUpdateView):
    model = BatchFermentationQC
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = BatchFermentationQCForm
    context_object_name = 'current_fermqc'

    def get_success_url(self):
        return reverse_lazy('fermqcentries', kwargs={'pk': self.kwargs.get('bpk')})

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        context = super(UpdateFermQCEntryView, self).get_context_data(**kwargs)
        context['batch'] = batch
        return context
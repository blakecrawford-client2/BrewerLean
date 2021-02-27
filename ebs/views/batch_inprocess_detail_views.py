from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from common.views.BLViews import BLCreateView, BLUpdateView
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
from ebs.forms.batch_maintenance_detail_forms import AddObeerDataForm
from ebs.forms.batch_maintenance_detail_forms import AddRawMaterialsForm
from ebs.forms.batch_maintenance_detail_forms import AddWortQCEntryForm
from ebs.forms.batch_maintenance_detail_forms import AddYeastPitchEntryForm
from ebs.forms.batch_maintenance_detail_forms import UpdateActualDatesForm
from ebs.forms.batch_maintenance_detail_forms import BatchFermentationQCForm
from ebs.forms.batch_maintenance_detail_forms import BatchDOEntryForm
from ebs.forms.batch_maintenance_detail_forms import BatchTransferForm
from ebs.forms.batch_maintenance_detail_forms import CarbonationQCEntryForm
from ebs.forms.batch_maintenance_detail_forms import CanningQCForm
from ebs.forms.batch_maintenance_detail_forms import PackagingRunForm
from ebs.forms.batch_maintenance_detail_forms import BatchNoteForm


class AddObeerDataView(LoginRequiredMixin, BLUpdateView):
    model = Batch
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = AddObeerDataForm
    context_object_name = 'batch'

    def get_success_url(self):
        return reverse('maintenance', kwargs={'pk': self.kwargs['pk']})


class RawMaterialsLogView(LoginRequiredMixin, BLUpdateView):
    model = Batch
    template_name = 'ebs/batch/inprocess/detail/inprocess-rawmaterialslog.html'
    form_class = AddRawMaterialsForm
    context_object_name = 'current_batch'

    def get_success_url(self):
        return reverse_lazy('maintenance', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('pk'))
        materials = BatchRawMaterialsLog.objects.filter(batch=batch.id).order_by('material__material_type')
        context = super(RawMaterialsLogView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['materials'] = materials
        return context


class AddRawMaterialsLogView(LoginRequiredMixin, BLCreateView):
    model = BatchRawMaterialsLog
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = AddRawMaterialsForm
    context_object_name = 'current_material'

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        context = super(AddRawMaterialsLogView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['name'] = 'Add Material'
        return context

    def get_success_url(self):
        return reverse_lazy('rawmaterials', kwargs={'pk': self.kwargs.get('bpk')})

    def form_valid(self, form):
        form.instance.batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        return super(AddRawMaterialsLogView, self).form_valid(form)


class UpdateRawMaterialsLogView(LoginRequiredMixin, BLUpdateView):
    model = BatchRawMaterialsLog
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = AddRawMaterialsForm
    context_object_name = 'current_material'

    def get_success_url(self):
        return reverse_lazy('rawmaterials', kwargs={'pk': self.kwargs.get('bpk')})

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        context = super(UpdateRawMaterialsLogView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['name'] = 'Edit Material'
        return context


class WortQCEntriesView(LoginRequiredMixin, BLUpdateView):
    model = Batch
    template_name = 'ebs/batch/inprocess/detail/inprocess-wortqcentry.html'
    form_class = AddWortQCEntryForm
    context_object_name = 'batch'

    def get_success_url(self):
        return reverse_lazy('maintenance', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        batch_id = self.kwargs.get('pk')
        batch = Batch.objects.get(pk=batch_id)
        wort_qc_entries = BatchWortQC.objects.filter(batch=batch.id)
        context = super(WortQCEntriesView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['wortqcentries'] = wort_qc_entries
        return context


class AddWortQCEntryView(LoginRequiredMixin, BLCreateView):
    model = BatchWortQC
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = AddWortQCEntryForm
    context_object_name = 'current_wortqc'

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        context = super(AddWortQCEntryView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['name'] = 'Add Wort QC'
        return context

    def get_success_url(self):
        return reverse_lazy('wortqcentries', kwargs={'pk': self.kwargs.get('bpk')})

    def form_valid(self, form):
        form.instance.batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        return super(AddWortQCEntryView, self).form_valid(form)


class UpdateWortQCEntryView(LoginRequiredMixin, BLUpdateView):
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
        context['name'] = 'Edit Wort QC'
        return context


class CreateYeastPitchView(LoginRequiredMixin, BLCreateView):
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
        context['name'] = 'Yeast Pitch'
        return context

    def form_valid(self, form):
        form.instance.batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        return super(CreateYeastPitchView, self).form_valid(form)


class UpdateYeastPitchView(LoginRequiredMixin, BLUpdateView):
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
        context['name'] = 'Yeast Pitch'
        return context

    def form_valid(self, form):
        form.instance.batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        return super(UpdateYeastPitchView, self).form_valid(form)


class UpdateActualDatesView(LoginRequiredMixin, BLUpdateView):
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
        context['name'] = 'Update Dates'
        return context

    def form_valid(self, form):
        form.instance.batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        return super(UpdateActualDatesView, self).form_valid(form)


class FermQCEntriesView(LoginRequiredMixin, BLUpdateView):
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
            ferm_qc_entries = BatchFermentationQC.objects.filter(batch=batch.id)
        except BatchFermentationQC.DoesNotExist:
            ferm_qc_entries = None
        context = super(FermQCEntriesView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['fermqcentries'] = ferm_qc_entries
        return context


class AddFermQCEntryView(LoginRequiredMixin, BLCreateView):
    model = BatchFermentationQC
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = BatchFermentationQCForm
    context_object_name = 'current_wortqc'

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        context = super(AddFermQCEntryView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['name'] = 'Add Ferm QC'
        return context

    def get_success_url(self):
        return reverse_lazy('fermqcentries', kwargs={'pk': self.kwargs.get('bpk')})

    def form_valid(self, form):
        form.instance.batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        return super(AddFermQCEntryView, self).form_valid(form)


class UpdateFermQCEntryView(LoginRequiredMixin, BLUpdateView):
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
        context['name'] = 'Update Ferm QC'
        return context


class BatchDOEntriesView(LoginRequiredMixin, BLUpdateView):
    model = Batch
    template_name = 'ebs/batch/inprocess/detail/inprocess-doentries.html'
    form_class = BatchDOEntryForm
    context_object_name = 'batch'

    def get_success_url(self):
        return reverse_lazy('maintenance', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        batch_id = self.kwargs.get('pk')
        batch = Batch.objects.get(pk=batch_id)
        try:
            do_entries = BatchDOEntry.objects.filter(batch=batch.id)
        except BatchDOEntry.DoesNotExist:
            do_entries = None
        context = super(BatchDOEntriesView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['doentries'] = do_entries
        return context


class AddBatchDOEntryView(LoginRequiredMixin, BLCreateView):
    model = BatchDOEntry
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = BatchDOEntryForm
    context_object_name = 'current_doentry'

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        context = super(AddBatchDOEntryView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['name'] = 'Add D.O Entry'
        return context

    def get_success_url(self):
        return reverse_lazy('doentries', kwargs={'pk': self.kwargs.get('bpk')})

    def form_valid(self, form):
        form.instance.batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        return super(AddBatchDOEntryView, self).form_valid(form)


class UpdateBatchDOEntryView(LoginRequiredMixin, BLUpdateView):
    model = BatchDOEntry
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = BatchDOEntryForm
    context_object_name = 'current_doentry'

    def get_success_url(self):
        return reverse_lazy('doentries', kwargs={'pk': self.kwargs.get('bpk')})

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        context = super(UpdateBatchDOEntryView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['name'] = 'Update D.O. Entry'
        return context


class CreateTransferView(LoginRequiredMixin, BLCreateView):
    model = BatchTransfer
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = BatchTransferForm
    context_object_name = 'current_transfer'

    def get_success_url(self):
        return reverse_lazy('maintenance', kwargs={'pk': self.kwargs.get('bpk')})

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        context = super(CreateTransferView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['name'] = 'Transfer Entry'
        return context

    def form_valid(self, form):
        form.instance.batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        return super(CreateTransferView, self).form_valid(form)


class UpdateTransferView(LoginRequiredMixin, BLUpdateView):
    model = BatchTransfer
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = BatchTransferForm
    context_object_name = 'current_transfer'

    def get_success_url(self):
        return reverse_lazy('maintenance', kwargs={'pk': self.kwargs.get('bpk')})

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        context = super(UpdateTransferView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['name'] = 'Transfer Entry'
        return context

    def form_valid(self, form):
        form.instance.batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        return super(UpdateTransferView, self).form_valid(form)


class CreateCarbonationQCView(LoginRequiredMixin, BLCreateView):
    model = CarbonationQCEntry
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = CarbonationQCEntryForm
    context_object_name = 'current_carbqc'

    def get_success_url(self):
        return reverse_lazy('maintenance', kwargs={'pk': self.kwargs.get('bpk')})

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        context = super(CreateCarbonationQCView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['name'] = 'Carbonation Entry'
        return context

    def form_valid(self, form):
        form.instance.batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        return super(CreateCarbonationQCView, self).form_valid(form)


class UpdateCarbonationQCView(LoginRequiredMixin, BLUpdateView):
    model = CarbonationQCEntry
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = CarbonationQCEntryForm
    context_object_name = 'current_carbqc'

    def get_success_url(self):
        return reverse_lazy('maintenance', kwargs={'pk': self.kwargs.get('bpk')})

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        context = super(UpdateCarbonationQCView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['name'] = 'Carbonation Entry'
        return context

    def form_valid(self, form):
        form.instance.batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        return super(UpdateCarbonationQCView, self).form_valid(form)


class CanningQCView(LoginRequiredMixin, BLUpdateView):
    model = Batch
    template_name = 'ebs/batch/inprocess/detail/inprocess-canqcentries.html'
    form_class = BatchDOEntryForm
    context_object_name = 'batch'

    def get_success_url(self):
        return reverse_lazy('maintenance', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        batch_id = self.kwargs.get('pk')
        batch = Batch.objects.get(pk=batch_id)
        try:
            can_qc_entries = CanningQC.objects.filter(batch=batch.id)
        except BatchDOEntry.DoesNotExist:
            can_qc_entries = None
        context = super(CanningQCView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['canqcentries'] = can_qc_entries
        return context


class AddCanningQCView(LoginRequiredMixin, BLCreateView):
    model = CanningQC
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = CanningQCForm
    context_object_name = 'current_canqcentry'

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        context = super(AddCanningQCView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['name'] = 'Add Can QC'
        return context

    def get_success_url(self):
        return reverse_lazy('canqcentries', kwargs={'pk': self.kwargs.get('bpk')})

    def form_valid(self, form):
        form.instance.batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        return super(AddCanningQCView, self).form_valid(form)


class UpdateCanningQCView(LoginRequiredMixin, BLUpdateView):
    model = CanningQC
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = CanningQCForm
    context_object_name = 'current_canqcentry'

    def get_success_url(self):
        return reverse_lazy('canqcentries', kwargs={'pk': self.kwargs.get('bpk')})

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        context = super(UpdateCanningQCView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['name'] = 'Update Can QC'
        return context


class CreatePackagingRunView(LoginRequiredMixin, BLCreateView):
    model = PackagingRun
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = PackagingRunForm
    context_object_name = 'current_packagingrun'

    def get_success_url(self):
        return reverse_lazy('maintenance', kwargs={'pk': self.kwargs.get('bpk')})

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        context = super(CreatePackagingRunView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['name'] = 'Final Pack-Off'
        return context

    def form_valid(self, form):
        form.instance.batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        return super(CreatePackagingRunView, self).form_valid(form)


class UpdatePackagingRunView(LoginRequiredMixin, BLUpdateView):
    model = PackagingRun
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = PackagingRunForm
    context_object_name = 'current_packagingrun'

    def get_success_url(self):
        return reverse_lazy('maintenance', kwargs={'pk': self.kwargs.get('bpk')})

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        context = super(UpdatePackagingRunView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['name'] = 'Final Pack-Off'
        return context

    def form_valid(self, form):
        form.instance.batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        return super(UpdatePackagingRunView, self).form_valid(form)


class BatchNoteView(LoginRequiredMixin, BLUpdateView):
    model = Batch
    template_name = 'ebs/batch/inprocess/detail/inprocess-batchnotes.html'
    form_class = BatchNoteForm
    context_object_name = 'batch'

    def get_success_url(self):
        return reverse_lazy('maintenance', kwargs={'pk': self.kwargs.get('pk')})

    def get_context_data(self, **kwargs):
        batch_id = self.kwargs.get('pk')
        batch = Batch.objects.get(pk=batch_id)
        try:
            batch_notes = BatchNote.objects.filter(batch=batch.id)
        except BatchNote.DoesNotExist:
            batch_notes = None
        context = super(BatchNoteView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['batchnotes'] = batch_notes
        return context


class AddBatchNoteView(LoginRequiredMixin, BLCreateView):
    model = BatchNote
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = BatchNoteForm
    context_object_name = 'current_batchnote'

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        context = super(AddBatchNoteView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['name'] = 'Add Batch Note'
        return context

    def get_success_url(self):
        return reverse_lazy('batchnotes', kwargs={'pk': self.kwargs.get('bpk')})

    def form_valid(self, form):
        form.instance.batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        return super(AddBatchNoteView, self).form_valid(form)


class UpdateBatchNoteView(LoginRequiredMixin, BLUpdateView):
    model = BatchNote
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = BatchNoteForm
    context_object_name = 'current_batchnote'

    def get_success_url(self):
        return reverse_lazy('batchnotes', kwargs={'pk': self.kwargs.get('bpk')})

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        context = super(UpdateBatchNoteView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['name'] = 'Update Batch Note'
        return context
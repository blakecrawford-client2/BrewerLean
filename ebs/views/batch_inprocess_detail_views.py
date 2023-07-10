from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from common.views.BLViews import BLCreateView, BLUpdateView, BLDeleteWithoutConfirmationView
from ebs.forms.batch_maintenance_detail_forms import *
from ebs.models.brew_sheets import *
from product.views import ProductMaterialsAbstract


###
# View to handle changing the FV for a batch
class ChangeFVView(LoginRequiredMixin, BLUpdateView):
    model = Batch
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = ChangeFVForm
    context_object_name = 'batch'

    def get_success_url(self):
        request_path = self.request.get_full_path()
        if '/archive' in request_path:
            return reverse_lazy('maintenance-archive', kwargs={'pk': self.kwargs.get('pk')})
        else:
            return reverse_lazy('maintenance', kwargs={'pk': self.kwargs.get('pk')})

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('pk'))
        context = super(ChangeFVView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['name'] = 'Change FV'
        return context


###
# Detail view for adding OBeer data, which is silly
# to be that specific.  it's the batch ID, along with
# whatever other internal ID your other sytems may or
# may not use.  Please note that this system does NOT
# generate batch ID's for you
class AddObeerDataView(LoginRequiredMixin, BLUpdateView):
    model = Batch
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = AddObeerDataForm
    context_object_name = 'batch'

    def get_success_url(self):
        request_path = self.request.get_full_path()
        if '/archive' in request_path:
            return reverse_lazy('maintenance-archive', kwargs={'pk': self.kwargs.get('pk')})
        else:
            return reverse_lazy('maintenance', kwargs={'pk': self.kwargs.get('pk')})

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('pk'))
        context = super(AddObeerDataView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['name'] = 'OBeer Data'
        return context


###
# Detail view to manage the raw materials log for a
# particular batch
class RawMaterialsLogView(LoginRequiredMixin, BLUpdateView):
    model = Batch
    template_name = 'ebs/batch/inprocess/detail/inprocess-rawmaterialslog.html'
    form_class = AddRawMaterialsForm
    context_object_name = 'current_batch'

    def get_success_url(self):
        request_path = self.request.get_full_path()
        if '/archive' in request_path:
            return reverse_lazy('maintenance-archive', kwargs={'pk': self.kwargs.get('bpk')})
        else:
            return reverse_lazy('maintenance', kwargs={'pk': self.kwargs.get('bpk')})

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('pk'))
        materials = BatchRawMaterialsLog.objects.filter(batch=batch.id).order_by('material__material_name')
        grain = BatchRawMaterialsLog.objects.filter(batch=batch.id, material__material_type='GR').order_by(
            'material__material_name')
        hops = BatchRawMaterialsLog.objects.filter(batch=batch.id, material__material_type='HP').order_by(
            'material__material_name')
        other = BatchRawMaterialsLog.objects.filter(batch=batch.id, material__material_type='OT').order_by(
            'material__material_name')
        not_listed = BatchNote.objects.filter(batch=batch.id, note_type='UM')

        try:
            abstract = ProductMaterialsAbstract.objects.filter(product=batch.batch_product.id)
        except:
            abstract = None

        context = super(RawMaterialsLogView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['grain'] = grain
        context['hops'] = hops
        context['other'] = other
        context['materials'] = materials
        context['not_listed'] = not_listed
        context['abstract'] = abstract
        return context


###
# Detail view to add a raw material to a batch
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
        request_path = self.request.get_full_path()
        if '/archive' in request_path:
            return reverse_lazy('rawmaterials-archive', kwargs={'pk': self.kwargs.get('bpk')})
        else:
            return reverse_lazy('rawmaterials', kwargs={'pk': self.kwargs.get('bpk')})

    def form_valid(self, form):
        form.instance.batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        return super(AddRawMaterialsLogView, self).form_valid(form)


###
# Detail view to update a raw materials line item for a batch
class UpdateRawMaterialsLogView(LoginRequiredMixin, BLUpdateView):
    model = BatchRawMaterialsLog
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = AddRawMaterialsForm
    context_object_name = 'current_material'

    def get_success_url(self):
        request_path = self.request.get_full_path()
        if '/archive' in request_path:
            return reverse_lazy('rawmaterials-archive', kwargs={'pk': self.kwargs.get('bpk')})
        else:
            return reverse_lazy('rawmaterials', kwargs={'pk': self.kwargs.get('bpk')})

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        context = super(UpdateRawMaterialsLogView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['name'] = 'Edit Material'
        return context


###
# Detail view for handling deletion of a raw materials line-item
class DeleteRawMaterialsLogView(LoginRequiredMixin, BLDeleteWithoutConfirmationView):
    model = BatchRawMaterialsLog
    context_object_name = 'current_material'
    template_name = "common/common_confirm_delete.html"

    def get_success_url(self):
        request_path = self.request.get_full_path()
        if '/archive' in request_path:
            return reverse_lazy('rawmaterials-archive', kwargs={'pk': self.kwargs.get('bpk')})
        else:
            return reverse_lazy('rawmaterials', kwargs={'pk': self.kwargs.get('bpk')})


###
# Detail view for wort QC entries, per turn.
class WortQCEntriesView(LoginRequiredMixin, BLUpdateView):
    model = Batch
    template_name = 'ebs/batch/inprocess/detail/inprocess-wortqcentry.html'
    form_class = AddWortQCEntryForm
    context_object_name = 'batch'

    def get_success_url(self):
        request_path = self.request.get_full_path()
        if '/archive' in request_path:
            return reverse_lazy('maintenance-archive', kwargs={'pk': self.kwargs.get('bpk')})
        else:
            return reverse_lazy('maintenance', kwargs={'pk': self.kwargs.get('bpk')})

    def get_context_data(self, **kwargs):
        batch_id = self.kwargs.get('pk')
        batch = Batch.objects.get(pk=batch_id)
        wort_qc_entries = BatchWortQC.objects.filter(batch=batch.id)
        context = super(WortQCEntriesView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['wortqcentries'] = wort_qc_entries
        return context


###
# Detail view for adding a new wort QC entry,
# per turn.
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
        request_path = self.request.get_full_path()
        if '/archive' in request_path:
            return reverse_lazy('wortqcentries-archive', kwargs={'pk': self.kwargs.get('bpk')})
        else:
            return reverse_lazy('wortqcentries', kwargs={'pk': self.kwargs.get('bpk')})

    def form_valid(self, form):
        form.instance.batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        return super(AddWortQCEntryView, self).form_valid(form)


###
# Detail view for updating a wort QC entry line item
class UpdateWortQCEntryView(LoginRequiredMixin, BLUpdateView):
    model = BatchWortQC
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = AddWortQCEntryForm
    context_object_name = 'current_wortqc'

    def get_success_url(self):
        request_path = self.request.get_full_path()
        if '/archive' in request_path:
            return reverse_lazy('wortqcentries-archive', kwargs={'pk': self.kwargs.get('bpk')})
        else:
            return reverse_lazy('wortqcentries', kwargs={'pk': self.kwargs.get('bpk')})

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        context = super(UpdateWortQCEntryView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['name'] = 'Edit Wort QC'
        return context


###
# Detail view for creating a new yeast pitch
class CreateYeastPitchView(LoginRequiredMixin, BLCreateView):
    model = BatchYeastPitch
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = AddYeastPitchEntryForm
    context_object_name = 'current_wortqc'

    def get_success_url(self):
        request_path = self.request.get_full_path()
        if '/archive' in request_path:
            return reverse_lazy('maintenance-archive', kwargs={'pk': self.kwargs.get('bpk')})
        else:
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


###
# Detail view for updating a yeast pitch
class UpdateYeastPitchView(LoginRequiredMixin, BLUpdateView):
    model = BatchYeastPitch
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = AddYeastPitchEntryForm
    context_object_name = 'current_wortqc'

    def get_success_url(self):
        request_path = self.request.get_full_path()
        if '/archive' in request_path:
            return reverse_lazy('maintenance-archive', kwargs={'pk': self.kwargs.get('bpk')})
        else:
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


###
# Detail view for updating an actual date
class UpdateActualDatesView(LoginRequiredMixin, BLUpdateView):
    model = BatchActualDates
    template_name = 'ebs/batch/inprocess/detail/inprocess-update-actdates.html'
    form_class = UpdateActualDatesForm
    context_object_name = 'current_actdates'

    def get_success_url(self):
        request_path = self.request.get_full_path()
        if '/archive' in request_path:
            return reverse_lazy('maintenance-archive', kwargs={'pk': self.kwargs.get('bpk')})
        else:
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


###
# Detail view for seeing the list of current ferm QC entries
class FermQCEntriesView(LoginRequiredMixin, BLUpdateView):
    model = Batch
    template_name = 'ebs/batch/inprocess/detail/inprocess-fermqcentry.html'
    form_class = BatchFermentationQCForm
    context_object_name = 'batch'

    def get_success_url(self):
        request_path = self.request.get_full_path()
        if '/archive' in request_path:
            return reverse_lazy('maintenance-archive', kwargs={'pk': self.kwargs.get('bpk')})
        else:
            return reverse_lazy('maintenance', kwargs={'pk': self.kwargs.get('bpk')})

    def get_context_data(self, **kwargs):
        batch_id = self.kwargs.get('pk')
        batch = Batch.objects.get(pk=batch_id)
        try:
            ferm_qc_entries = BatchFermentationQC.objects.filter(batch=batch.id)
        except BatchFermentationQC.DoesNotExist:
            ferm_qc_entries = None

        ###
        # Average all real gravities from existing wort QC entries
        # and use that to determine the starting extract that will
        # be used for calculations
        sum_og_entries = 0.0
        basis_og = 0.0
        basis_rdf = 0.80
        wort_qc_entries = BatchWortQC.objects.filter(batch=batch.id)
        if wort_qc_entries:
            for entry in wort_qc_entries:
                # need better error handling here.  case where there's no postboil for
                # second turn throws error
                sum_og_entries += float(entry.extract_postboil)
            basis_og = sum_og_entries / wort_qc_entries.count()
        #basis_fg = basis_og * (1.0 - basis_rdf)
        #real_rdf = (100 * (basis_og - basis_fg) / basis_og) * (1 / (1 - 0.005161 * basis_fg))

        ###
        # Calculate the RDF for all ferm qc entries.  This should probably
        # be calculated at save time and stored in the model, but for now
        # we're just calculating at display time out of an abundance of
        # caution to ensure we don't end up with piles of bad data in the DB
        fermqc_rdf_list = []
        for fermqc in ferm_qc_entries:
            if fermqc.extract_real:
                temp_rdf = (100 * (basis_og - float(fermqc.extract_real)) / basis_og) * (1 / (1 - 0.005161 * float(fermqc.extract_real)))
            fermqc_rdf_list.append([fermqc.date, fermqc.extract_real, fermqc.ph, fermqc.temp_pv, temp_rdf, fermqc.id])

        context = super(FermQCEntriesView, self).get_context_data(**kwargs)
        context['batch'] = batch
        #context['fermqcentries'] = ferm_qc_entries
        context['fermqcentries'] = fermqc_rdf_list
        context['basis_og'] = basis_og
        context['basis_rdf'] = basis_rdf
        return context


###
# detail view for adding a new ferm qc line item
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
        request_path = self.request.get_full_path()
        if '/archive' in request_path:
            return reverse_lazy('fermqcentries-archive', kwargs={'pk': self.kwargs.get('bpk')})
        else:
            return reverse_lazy('fermqcentries', kwargs={'pk': self.kwargs.get('bpk')})

    def form_valid(self, form):
        form.instance.batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        return super(AddFermQCEntryView, self).form_valid(form)


###
# Detail view for updating a ferm QC line item
class UpdateFermQCEntryView(LoginRequiredMixin, BLUpdateView):
    model = BatchFermentationQC
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = BatchFermentationQCForm
    context_object_name = 'current_fermqc'

    def get_success_url(self):
        request_path = self.request.get_full_path()
        if '/archive' in request_path:
            return reverse_lazy('fermqcentries-archive', kwargs={'pk': self.kwargs.get('bpk')})
        else:
            return reverse_lazy('fermqcentries', kwargs={'pk': self.kwargs.get('bpk')})

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        context = super(UpdateFermQCEntryView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['name'] = 'Update Ferm QC'
        return context


###
# Detail view for seeing the set of DO entries.
class BatchDOEntriesView(LoginRequiredMixin, BLUpdateView):
    model = Batch
    template_name = 'ebs/batch/inprocess/detail/inprocess-doentries.html'
    form_class = BatchDOEntryForm
    context_object_name = 'batch'

    def get_success_url(self):
        request_path = self.request.get_full_path()
        if '/archive' in request_path:
            return reverse_lazy('maintenance-archive', kwargs={'pk': self.kwargs.get('bpk')})
        else:
            return reverse_lazy('maintenance', kwargs={'pk': self.kwargs.get('bpk')})

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


###
# Detail view for adding a new DO line item
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
        request_path = self.request.get_full_path()
        if '/archive' in request_path:
            return reverse_lazy('doentries-archive', kwargs={'pk': self.kwargs.get('bpk')})
        else:
            return reverse_lazy('doentries', kwargs={'pk': self.kwargs.get('bpk')})

    def form_valid(self, form):
        form.instance.batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        return super(AddBatchDOEntryView, self).form_valid(form)


###
# Detail view for updating a DO entry view
class UpdateBatchDOEntryView(LoginRequiredMixin, BLUpdateView):
    model = BatchDOEntry
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = BatchDOEntryForm
    context_object_name = 'current_doentry'

    def get_success_url(self):
        request_path = self.request.get_full_path()
        if '/archive' in request_path:
            return reverse_lazy('doentries-archive', kwargs={'pk': self.kwargs.get('bpk')})
        else:
            return reverse_lazy('doentries', kwargs={'pk': self.kwargs.get('bpk')})

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        context = super(UpdateBatchDOEntryView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['name'] = 'Update D.O. Entry'
        return context


###
# Detail view for creating a new transfer entry
class CreateTransferView(LoginRequiredMixin, BLCreateView):
    model = BatchTransfer
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = BatchTransferForm
    context_object_name = 'current_transfer'

    def get_success_url(self):
        request_path = self.request.get_full_path()
        if '/archive' in request_path:
            return reverse_lazy('maintenance-archive', kwargs={'pk': self.kwargs.get('bpk')})
        else:
            return reverse_lazy('maintenance', kwargs={'pk': self.kwargs.get('bpk')})

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        context = super(CreateTransferView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['name'] = 'Transfer Entry'
        return context

    def form_valid(self, form):
        form.instance.batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        temp_form = form.save(commit=False)
        act_dates = BatchActualDates.objects.get(batch_id=form.instance.batch.id)
        act_dates.transfer_date = temp_form.date
        act_dates.save()
        temp_form.save()
        return super(CreateTransferView, self).form_valid(form)


###
# Detail view for updating a transfer record
class UpdateTransferView(LoginRequiredMixin, BLUpdateView):
    model = BatchTransfer
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = BatchTransferForm
    context_object_name = 'current_transfer'

    def get_success_url(self):
        request_path = self.request.get_full_path()
        if '/archive' in request_path:
            return reverse_lazy('maintenance-archive', kwargs={'pk': self.kwargs.get('bpk')})
        else:
            return reverse_lazy('maintenance', kwargs={'pk': self.kwargs.get('bpk')})

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        context = super(UpdateTransferView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['name'] = 'Transfer Entry'
        return context

    def form_valid(self, form):
        form.instance.batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        temp_form = form.save(commit=False)
        act_dates = BatchActualDates.objects.get(batch_id=form.instance.batch.id)
        act_dates.transfer_date = temp_form.date
        act_dates.save()
        temp_form.save()
        return super(UpdateTransferView, self).form_valid(form)


###
# Detail view for creating a carbonation entry
class CreateCarbonationQCView(LoginRequiredMixin, BLCreateView):
    model = CarbonationQCEntry
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = CarbonationQCEntryForm
    context_object_name = 'current_carbqc'

    def get_success_url(self):
        request_path = self.request.get_full_path()
        if '/archive' in request_path:
            return reverse_lazy('maintenance-archive', kwargs={'pk': self.kwargs.get('pk')})
        else:
            return reverse_lazy('maintenance', kwargs={'pk': self.kwargs.get('pk')})

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('pk'))
        context = super(CreateCarbonationQCView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['name'] = 'Carbonation Entry'
        return context

    def form_valid(self, form):
        form.instance.batch = Batch.objects.get(pk=self.kwargs.get('pk'))
        return super(CreateCarbonationQCView, self).form_valid(form)


###
# Detail view for updating a carbonation entry
class UpdateCarbonationQCView(LoginRequiredMixin, BLUpdateView):
    model = CarbonationQCEntry
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = CarbonationQCEntryForm
    context_object_name = 'current_carbqc'

    def get_success_url(self):
        request_path = self.request.get_full_path()
        if '/archive' in request_path:
            return reverse_lazy('maintenance-archive', kwargs={'pk': self.kwargs.get('bpk')})
        else:
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


###
# Detail view for seeing a list of current canning QC
# line items
class CanningQCView(LoginRequiredMixin, BLUpdateView):
    model = Batch
    template_name = 'ebs/batch/inprocess/detail/inprocess-canqcentries.html'
    form_class = BatchDOEntryForm
    context_object_name = 'batch'

    def get_success_url(self):
        request_path = self.request.get_full_path()
        if '/archive' in request_path:
            return reverse_lazy('maintenance-archive', kwargs={'pk': self.kwargs.get('bpk')})
        else:
            return reverse_lazy('maintenance', kwargs={'pk': self.kwargs.get('bpk')})

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


###
# Detail view for adding a new can QC line item
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
        request_path = self.request.get_full_path()
        if '/archive' in request_path:
            return reverse_lazy('canqcentries-archive', kwargs={'pk': self.kwargs.get('bpk')})
        else:
            return reverse_lazy('canqcentries', kwargs={'pk': self.kwargs.get('bpk')})

    def form_valid(self, form):
        form.instance.batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        return super(AddCanningQCView, self).form_valid(form)


###
# Detail view for updating an existing can QC line item
class UpdateCanningQCView(LoginRequiredMixin, BLUpdateView):
    model = CanningQC
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = CanningQCForm
    context_object_name = 'current_canqcentry'

    def get_success_url(self):
        request_path = self.request.get_full_path()
        if '/archive' in request_path:
            return reverse_lazy('canqcentries-archive', kwargs={'pk': self.kwargs.get('bpk')})
        else:
            return reverse_lazy('canqcentries', kwargs={'pk': self.kwargs.get('bpk')})

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        context = super(UpdateCanningQCView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['name'] = 'Update Can QC'
        return context


###
# Detail view for creating a new packaging run
class CreatePackagingRunView(LoginRequiredMixin, BLCreateView):
    model = PackagingRun
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = PackagingRunForm
    context_object_name = 'current_packagingrun'

    def get_success_url(self):
        request_path = self.request.get_full_path()
        if '/archive' in request_path:
            return reverse_lazy('maintenance-archive', kwargs={'pk': self.kwargs.get('bpk')})
        else:
            return reverse_lazy('maintenance', kwargs={'pk': self.kwargs.get('bpk')})

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        context = super(CreatePackagingRunView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['name'] = 'Final Pack-Off'
        return context

    def form_valid(self, form):
        form.instance.batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        temp_form = form.save(commit=False)
        act_dates = BatchActualDates.objects.get(batch_id=form.instance.batch.id)
        act_dates.package_date = temp_form.date
        act_dates.save()
        temp_form.save()
        return super(CreatePackagingRunView, self).form_valid(form)


###
# Detail view for updating an existing packaging run
class UpdatePackagingRunView(LoginRequiredMixin, BLUpdateView):
    model = PackagingRun
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = PackagingRunForm
    context_object_name = 'current_packagingrun'

    def get_success_url(self):
        request_path = self.request.get_full_path()
        if '/archive' in request_path:
            return reverse_lazy('maintenance-archive', kwargs={'pk': self.kwargs.get('bpk')})
        else:
            return reverse_lazy('maintenance', kwargs={'pk': self.kwargs.get('bpk')})

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        context = super(UpdatePackagingRunView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['name'] = 'Final Pack-Off'
        return context

    ###
    # Note: using form_valid to back-fill BatchActualDates
    def form_valid(self, form):
        form.instance.batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        temp_form = form.save(commit=False)
        act_dates = BatchActualDates.objects.get(batch_id=form.instance.batch.id)
        act_dates.package_date = temp_form.date
        act_dates.save()
        temp_form.save()
        return super(UpdatePackagingRunView, self).form_valid(form)


###
# Detail view for seeing a list of existing batch notes
class BatchNoteView(LoginRequiredMixin, BLUpdateView):
    model = Batch
    template_name = 'ebs/batch/inprocess/detail/inprocess-batchnotes.html'
    form_class = BatchNoteForm
    context_object_name = 'batch'

    def get_success_url(self):
        request_path = self.request.get_full_path()
        if '/archive' in request_path:
            return reverse_lazy('maintenance-archive', kwargs={'pk': self.kwargs.get('bpk')})
        else:
            return reverse_lazy('maintenance', kwargs={'pk': self.kwargs.get('bpk')})

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


###
# Detail view for adding a new batch note line item
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
        request_path = self.request.get_full_path()
        if '/archive' in request_path:
            return reverse_lazy('batchnotes-archive', kwargs={'pk': self.kwargs.get('bpk')})
        else:
            return reverse_lazy('batchnotes', kwargs={'pk': self.kwargs.get('bpk')})

    def form_valid(self, form):
        form.instance.batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        return super(AddBatchNoteView, self).form_valid(form)


###
# Detail view for updating an existing batch note line item
class UpdateBatchNoteView(LoginRequiredMixin, BLUpdateView):
    model = BatchNote
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = BatchNoteForm
    context_object_name = 'current_batchnote'

    def get_success_url(self):
        request_path = self.request.get_full_path()
        if '/archive' in request_path:
            return reverse_lazy('batchnotes-archive', kwargs={'pk': self.kwargs.get('bpk')})
        else:
            return reverse_lazy('batchnotes', kwargs={'pk': self.kwargs.get('bpk')})

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        context = super(UpdateBatchNoteView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['name'] = 'Update Batch Note'
        return context


##########
# I suppose this could just be a modelview that uses a model
# form specifically for these two fields on BatchActualDates,
# but for future integration w/ the Yeast module, I did it this
# way to provide an explicit framework for future work.  It
# probably makes no sense other than at the time I wrote it.
# -BJC
class CreateYeastCrashHarvestView(FormView, LoginRequiredMixin):
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = YeastCrashHarvestForm

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('pk'))
        context = super(CreateYeastCrashHarvestView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['name'] = 'Yeast Crash/Harvest'
        return context

    def get(self, request, *args, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('pk'))
        act_dates = BatchActualDates.objects.get(batch=batch)
        initial_dict = {
            "yeast_crash_date": act_dates.yeast_crash_date,
            "yeast_harvest_date": act_dates.yeast_harvest_date,
        }
        form = YeastCrashHarvestForm(request.POST or None, initial=initial_dict)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        request_path = self.request.get_full_path()
        if '/archive' in request_path:
            return reverse_lazy('maintenance-archive', kwargs={'pk': self.kwargs.get('pk')})
        else:
            return reverse_lazy('maintenance', kwargs={'pk': self.kwargs.get('pk')})

    def form_valid(self, form):
        self.save_data(form.cleaned_data)
        return super(CreateYeastCrashHarvestView, self).form_valid(form)

    def save_data(self, valid_data):
        batch = Batch.objects.get(pk=self.kwargs.get('pk'))
        act_dates = BatchActualDates.objects.get(batch=batch)
        act_dates.yeast_crash_date = valid_data['yeast_crash_date']
        act_dates.yeast_harvest_date = valid_data['yeast_harvest_date']
        act_dates.save()


###
# Similarly to the YeastCrashHarvestView, I separated this for
# future workflow concerns.  It may be a convolution that we don't
# really need.
class CreateFinalCrashDateView(LoginRequiredMixin, BLUpdateView):
    model = BatchActualDates
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = FinalCrashForm
    context_object_name = 'current_finalcrashdate'

    def get_success_url(self):
        request_path = self.request.get_full_path()
        if '/archive' in request_path:
            return reverse_lazy('maintenance-archive', kwargs={'pk': self.kwargs.get('pk')})
        else:
            return reverse_lazy('maintenance', kwargs={'pk': self.kwargs.get('pk')})

    def get_context_data(self, **kwargs):
        batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        context = super(CreateFinalCrashDateView, self).get_context_data(**kwargs)
        context['batch'] = batch
        context['name'] = 'Final Crash Date'
        return context

    def form_valid(self, form):
        form.instance.batch = Batch.objects.get(pk=self.kwargs.get('bpk'))
        return super(CreateFinalCrashDateView, self).form_valid(form)


class CreateDryhopDateView(LoginRequiredMixin, BLUpdateView):
        model = BatchActualDates
        template_name = 'ebs/batch/inprocess/detail/inprocess-add-subdate-raw-notes.html'
        form_class = DryHopForm

        def get_success_url(self):
            request_path = self.request.get_full_path()
            if '/archive' in request_path:
                return reverse_lazy('maintenance-archive', kwargs={'pk': self.kwargs.get('pk')})
            else:
                return reverse_lazy('maintenance', kwargs={'pk': self.kwargs.get('pk')})

        def get_context_data(self, **kwargs):
            batch = Batch.objects.get(pk=self.kwargs.get('pk'))
            materials = BatchRawMaterialsLog.objects.filter(batch=batch.id).order_by('material__material_name')
            grain = BatchRawMaterialsLog.objects.filter(batch=batch.id, material__material_type='GR').order_by(
                'material__material_name')
            hops = BatchRawMaterialsLog.objects.filter(batch=batch.id, material__material_type='HP').order_by(
                'material__material_name')
            other = BatchRawMaterialsLog.objects.filter(batch=batch.id, material__material_type='OT').order_by(
                'material__material_name')
            not_listed = BatchNote.objects.filter(batch=batch.id, note_type='UM')
            context = super(CreateDryhopDateView, self).get_context_data(**kwargs)
            context['batch'] = batch
            context['grain'] = grain
            context['hops'] = hops
            context['other'] = other
            context['materials'] = materials
            context['not_listed'] = not_listed
            context['name'] = 'Cold Side Addition Date'
            return context

        def form_valid(self, form):
            form.instance.batch = Batch.objects.get(pk=self.kwargs.get('pk'))
            return super(CreateDryhopDateView, self).form_valid(form)


###
# Detail view to manage the package plan for a
# particular batch
class PackagePlanView(LoginRequiredMixin, BLUpdateView):
    model = Batch
    template_name = 'ebs/batch/inprocess/detail/inprocess_batch_pkgplan.html'
    form_class = AddRawMaterialsForm
    context_object_name = 'current_batch'

    def get_success_url(self):
        request_path = self.request.get_full_path()
        if '/archive' in request_path:
            return reverse_lazy('maintenance-archive', kwargs={'pk': self.kwargs.get('bpk')})
        else:
            return reverse_lazy('maintenance', kwargs={'pk': self.kwargs.get('bpk')})

    def get_context_data(self, **kwargs):
        context = super(PackagePlanView, self).get_context_data(**kwargs)
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
                             + (package_plan.cs_750ml * 2.38)) / 31

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

        base_vol = float(batch.total_batch_size.batch_size_name) * (float(base_yield) / 100.0)
        context['base_yield'] = base_yield
        context['base_vol'] = base_vol
        if package_plan:
            context['total_plan_yield'] = (float(total_pkg_vol) / float(batch.total_batch_size.batch_size_name)) * 100
        else:
            context['total_plan_yield'] = 'NaN'
        context['package_plan'] = package_plan
        return context

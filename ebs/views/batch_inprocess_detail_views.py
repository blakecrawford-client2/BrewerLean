from django.urls import reverse_lazy
from common.views.BLViews import BLCreateView, BLUpdateView
from ebs.models.brew_sheets import Batch
from ebs.models.brew_sheets import BatchRawMaterialsLog
from ebs.forms.batch_maintenance_detail_forms import AddObeerDataForm
from ebs.forms.batch_maintenance_detail_forms import AddRawMaterialsForm

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

class AddRawMaterialsLog(BLCreateView):
    model = BatchRawMaterialsLog
    template_name = 'ebs/batch/inprocess/detail/inprocess-add-subitem.html'
    form_class = AddRawMaterialsForm
    context_object_name = 'current_material'
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from common.views.BLViews import BLUpdateView
from ebs.models.brew_sheets import Batch
from ebs.forms.batch_close_forms import CloseBatchForm


class ArchiveBatchListView(LoginRequiredMixin, ListView):
    model = Batch
    template_name = 'ebs/batch/archive-batch-list.html'
    context_object_name = 'archive_batch_list'

    def get_queryset(self):
        return Batch.objects.filter(status='AR').order_by('last_modified_on')


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
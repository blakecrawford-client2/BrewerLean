from django.views.generic import ListView
from common.views.BLViews import BLCreateView, BLUpdateView
from ebs.models.master_data_partners import PartnerType
from ebs.forms.master_data_partners_forms import PartnerTypeForm

class PartnerTypesList(ListView):
    model = PartnerType
    template_name = 'ebs/partner-type-list.html'
    context_object_name = 'partner_type_list'

class PartnerTypeCreateView(BLCreateView):
    template_name = 'ebs/partner-type-create-or-update.html'
    form_class = PartnerTypeForm
    success_url = '/partner-types/'
    context_object_name = 'partner_type_list'

class PartnerTypeUpdateView(BLUpdateView):
    model = PartnerType
    form_class = PartnerTypeForm
    template_name = "ebs/partner-type-create-or-update.html"
    success_url = '/partner-types/'
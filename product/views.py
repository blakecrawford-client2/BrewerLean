
from django.http import HttpResponseRedirect
from product.models import ProductServiceInfo
from product.forms import ProductServiceInfoForm
from ebs.models.master_data_products import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from common.views.BLViews import BLCreateView
from common.views.BLViews import BLListView
from common.views.BLViews import BLUpdateView
from common.views.BLViews import BLDetailView

# Create your views here.
class ProductServiceInfoCreateView(LoginRequiredMixin, BLCreateView):
    model = ProductServiceInfo
    template_name = 'product/productserviceinfo_create.html'
    form_class = ProductServiceInfoForm
    success_url = '/product/serviceinfo/list/'


class ProductServiceInfoUpdateView(LoginRequiredMixin, BLUpdateView):
    model = ProductServiceInfo
    template_name = 'product/productserviceinfo_create.html'
    form_class = ProductServiceInfoForm
    success_url = '/product/serviceinfo/list/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'Update Service Info'
        return context


class ProductServiceInfoListView(LoginRequiredMixin, BLListView):
    model = ProductServiceInfo
    template_name = 'product/productserviceinfo_list.html'
    context_object_name = 'psi_list'

    def get_queryset(self):
        return ProductServiceInfo.objects.all()


class ProductServiceInfoPrintView(LoginRequiredMixin, BLDetailView):
    model = ProductServiceInfo
    context_object_name = 'psi'
    template_name = 'product/productserviceinfo_print.html'


class ProductListView(LoginRequiredMixin, BLListView):
    model = Product
    context_object_name = 'prod_list'
    template_name = 'product/product_list.html'






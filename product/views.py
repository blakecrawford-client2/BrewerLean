import requests
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from ebs.models.master_data_products import Product
from product.models import ProductServiceInfo
from product.models import ProductOperationsInfo
from product.models import ProductMaterialsAbstract
from product.forms import ProductServiceInfoForm
from product.forms import ProductOpsInfoForm
from product.forms import ProductForm
from product.forms import ProductMaterialsAbstractItemForm
from ebs.models.master_data_products import Product
from ebs.models.master_data_partners import Partner
from django.contrib.auth.mixins import LoginRequiredMixin
from common.views.BLViews import BLCreateView
from common.views.BLViews import BLListView
from common.views.BLViews import BLUpdateView
from common.views.BLViews import BLDetailView
from common.views.BLViews import BLDeleteWithoutConfirmationView


class ProductCreateView(LoginRequiredMixin, BLCreateView):
    model = Product
    template_name = 'product/product_create.html'
    form_class = ProductForm
    success_url = '/product'

    def get_context_data(self, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        context['page_name'] = 'Create A New Product'
        return context


class ProductUpdateView(LoginRequiredMixin, BLUpdateView):
    model = Product
    template_name = 'product/product_create.html'
    form_class = ProductForm
    # success_url = '/product'

    def get_context_data(self, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        context['page_name'] = 'Update A Product'
        return context

    def get_success_url(self):
        if ('/fromdetail' in self.request.get_full_path()):
            success_url = '/product/detail/' + str(self.object.id)
        else:
            success_url = '/product'
        return success_url


class ProductOptionsPageView(LoginRequiredMixin, BLListView):
    model = Product
    template_name = 'product/product_options_page.html'
    # context_object_name = 'prd'

    def get_context_data(self, **kwargs):
        context = super(ProductOptionsPageView, self).get_context_data(**kwargs)
        context['page_name'] = 'Product Options'
        context['owner_list'] = Partner.objects.filter(partner_active=True).order_by('partner_short_code')
        context['product_list'] = Product.objects.order_by('ownership__partner_name', 'ownership__partner_active', 'product_name')
        # context['product_list'] = Product.objects.all()
        return context


class ProductDetailPageView(LoginRequiredMixin, BLDetailView):
    model = Product
    template_name = 'product/product_details_page.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailPageView, self).get_context_data(**kwargs)
        context['page_name'] = 'Product Detail'
        try:
            context['materials_abstract'] = ProductMaterialsAbstract.objects.filter(product__id=self.object.id)
        except:
            context['materials_abstract'] = None
        try:
            context['service_info'] = ProductServiceInfo.objects.get(product__id=self.object.id)
        except:
            context['service_info'] = None
        try:
            context['ops_info'] = ProductOperationsInfo.objects.get(product__id=self.object.id)
        except:
            context['ops_info'] = None
        return context


# Create your views here.
class ProductServiceInfoCreateView(LoginRequiredMixin, BLCreateView):
    model = ProductServiceInfo
    template_name = 'product/productserviceinfo_create.html'
    form_class = ProductServiceInfoForm

    def get_success_url(self):
        if ('/detail/' in self.request.get_full_path()):
            success_url = '/product/detail/' + str(self.kwargs.get('pk'))
        else:
            success_url = '/product'
        return success_url

    def form_valid(self, form):
        form.instance.product = Product.objects.get(pk=self.kwargs.get('pk'))
        return super(ProductServiceInfoCreateView, self).form_valid(form)


class ProductServiceInfoUpdateView(LoginRequiredMixin, BLUpdateView):
    model = ProductServiceInfo
    template_name = 'product/productserviceinfo_create.html'
    form_class = ProductServiceInfoForm
    success_url = '/product/serviceinfo/list/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'Update Service Info'
        return context

    def get_success_url(self):
        if ('/detail/' in self.request.get_full_path()):
            success_url = '/product/detail/' + str(self.kwargs.get('ppk'))
        else:
            success_url = '/product'
        return success_url

    def form_valid(self, form):
        form.instance.product = Product.objects.get(pk=self.kwargs.get('ppk'))
        return super(ProductServiceInfoUpdateView, self).form_valid(form)



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


class ProductOpsInfoCreateView(LoginRequiredMixin, BLCreateView):
    model = ProductOperationsInfo
    template_name = 'product/productopsinfo_create.html'
    form_class = ProductOpsInfoForm

    def get_success_url(self):
        if ('/detail/' in self.request.get_full_path()):
            success_url = '/product/detail/' + str(self.kwargs.get('pk'))
        else:
            success_url = '/product'
        return success_url

    def form_valid(self, form):
        form.instance.product = Product.objects.get(pk=self.kwargs.get('pk'))
        return super(ProductOpsInfoCreateView, self).form_valid(form)


class ProductOpsInfoUpdateView(LoginRequiredMixin, BLUpdateView):
    model = ProductOperationsInfo
    template_name = 'product/productopsinfo_create.html'
    form_class = ProductOpsInfoForm

    def get_success_url(self):
        if ('/detail/' in self.request.get_full_path()):
            success_url = '/product/detail/' + str(self.kwargs.get('ppk'))
        else:
            success_url = '/product'
        return success_url

    def form_valid(self, form):
        form.instance.product = Product.objects.get(pk=self.kwargs.get('ppk'))
        return super(ProductOpsInfoUpdateView, self).form_valid(form)


class ProductMaterialsAbstractItemCreateView(LoginRequiredMixin, BLCreateView):
    model=ProductMaterialsAbstract
    template_name = 'product/product_materials_abstract_item_create.html'
    form_class = ProductMaterialsAbstractItemForm

    def get_success_url(self):
        if ('/detail/' in self.request.get_full_path()):
            success_url = '/product/detail/' + str(self.kwargs.get('ppk'))
        else:
            success_url = '/product'
        return success_url

    def form_valid(self, form):
        form.instance.product = Product.objects.get(pk=self.kwargs.get('ppk'))
        return super(ProductMaterialsAbstractItemCreateView, self).form_valid(form)


class ProductMaterialsAbstractItemUpdateView(LoginRequiredMixin, BLUpdateView):
    model = ProductMaterialsAbstract
    template_name = 'product/product_materials_abstract_item_create.html'
    form_class = ProductMaterialsAbstractItemForm

    def get_success_url(self):
        if ('/detail/' in self.request.get_full_path()):
            success_url = '/product/detail/' + str(self.kwargs.get('ppk'))
        else:
            success_url = '/product'
        return success_url

    def form_valid(self, form):
        form.instance.product = Product.objects.get(pk=self.kwargs.get('ppk'))
        return super(ProductMaterialsAbstractItemUpdateView, self).form_valid(form)


class ProductMaterialsAbstractItemDeleteView(LoginRequiredMixin, BLDeleteWithoutConfirmationView):
    model = ProductMaterialsAbstract
    template_name = "common/common_confirm_delete.html"

    def get_success_url(self):
        if ('/detail/' in self.request.get_full_path()):
            success_url = '/product/detail/' + str(self.kwargs.get('ppk'))
        else:
            success_url = '/product'
        return success_url

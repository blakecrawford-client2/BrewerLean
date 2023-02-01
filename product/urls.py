from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from product.views import ProductOptionsPageView
from product.views import ProductServiceInfoCreateView
from product.views import ProductServiceInfoListView
from product.views import ProductServiceInfoUpdateView
from product.views import ProductServiceInfoPrintView
from product.views import ProductOpsInfoCreateView
from product.views import ProductOpsInfoUpdateView
from product.views import ProductMaterialsAbstractItemCreateView
from product.views import ProductMaterialsAbstractItemUpdateView
from product.views import ProductMaterialsAbstractItemDeleteView
from product.views import ProductListView
from product.views import ProductCreateView
from product.views import ProductUpdateView
from product.views import ProductDetailPageView

urlpatterns = [
    ##########
    ## Upcoming URLS
    path('', ProductOptionsPageView.as_view()),
    path('create/', ProductCreateView.as_view()),
    path('update/<int:pk>/', ProductUpdateView.as_view()),
    path('update/<int:pk>/fromdetail/', ProductUpdateView.as_view()),
    path('detail/<int:pk>/', ProductDetailPageView.as_view()),
    path('detail/<int:pk>/opsinfo/create/', ProductOpsInfoCreateView.as_view()),
    path('detail/<int:ppk>/opsinfo/update/<int:pk>/', ProductOpsInfoUpdateView.as_view()),
    path('detail/<int:pk>/serviceinfo/create/', ProductServiceInfoCreateView.as_view()),
    path('detail/<int:ppk>/serviceinfo/update/<int:pk>/', ProductServiceInfoUpdateView.as_view()),
    path('detail/<int:ppk>/materialsabstractitem/create/', ProductMaterialsAbstractItemCreateView.as_view()),
    path('detail/<int:ppk>/materialsabstractitem/update/<int:pk>/', ProductMaterialsAbstractItemUpdateView.as_view()),
    path('detail/<int:ppk>/materialsabstractitem/delete/<int:pk>/', ProductMaterialsAbstractItemDeleteView.as_view()),
    path('serviceinfo/create/', ProductServiceInfoCreateView.as_view()),
    path('serviceinfo/list/',ProductServiceInfoListView.as_view()),
    path('serviceinfo/update/<int:pk>/', ProductServiceInfoUpdateView.as_view()),
    path('serviceinfo/print/<int:pk>/', ProductServiceInfoPrintView.as_view()),
    path('list/', ProductListView.as_view()),
]


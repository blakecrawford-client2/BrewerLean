from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from product.views import ProductServiceInfoCreateView
from product.views import ProductServiceInfoListView
from product.views import ProductServiceInfoUpdateView
from product.views import ProductServiceInfoPrintView
from product.views import ProductListView

urlpatterns = [
    ##########
    ## Upcoming URLS
    path('serviceinfo/create/', ProductServiceInfoCreateView.as_view()),
    path('serviceinfo/list/',ProductServiceInfoListView.as_view()),
    path('serviceinfo/update/<int:pk>/', ProductServiceInfoUpdateView.as_view()),
    path('serviceinfo/print/<int:pk>/', ProductServiceInfoPrintView.as_view()),
    path('list/', ProductListView.as_view()),
]


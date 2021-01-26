from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from ebs.views import *
from ebs.views.master_data_partners_views import PartnerTypesList
from ebs.views.master_data_partners_views import PartnerTypeUpdateView,PartnerTypeCreateView

urlpatterns = [
    path('', PartnerTypesList.as_view()),
    path('create', PartnerTypeCreateView.as_view()),
    path('update/<int:pk>', PartnerTypeUpdateView.as_view()),
]
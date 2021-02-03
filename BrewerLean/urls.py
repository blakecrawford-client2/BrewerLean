"""BrewerLean URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from ebs.views import *
from ebs.views.master_data_partners_views import PartnerTypesList
from ebs.views.master_data_partners_views import PartnerTypeUpdateView,PartnerTypeCreateView

urlpatterns = [
    path('',TemplateView.as_view(template_name="ebs/index.html")),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    # path('partner-type/create', partner_type_create, name='partner_type_create'),
    # path('partner-type/list', partner_type_grid, name='partner_type_list'),
    # path('partner-type/update/<int:pk>', partner_type_edit, name='partner_type_edit'),
    path('ebs/', include ('ebs.urls')),
    #path('partner-types/', PartnerTypesList.as_view()),
    #path('partner-types/create', PartnerTypeCreateView.as_view()),
    #path('partner-types/update/<int:pk>', PartnerTypeUpdateView.as_view()),
]

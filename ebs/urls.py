from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from ebs.views import *
from ebs.views.master_data_partners_views import PartnerTypesList
from ebs.views.master_data_partners_views import PartnerTypeUpdateView,PartnerTypeCreateView
from ebs.views.batch_upcoming_views import UpcomingBatchList, UpcomingBatchCreateView
from ebs.views.batch_inprocess_views import InprocessBatchList, InprocessBatchCreateView

urlpatterns = [
    #path('', PartnerTypesList.as_view()),
    #path('create', PartnerTypeCreateView.as_view()),
    #path('update/<int:pk>', PartnerTypeUpdateView.as_view()),
    path('upcoming/', UpcomingBatchList.as_view()),
    path('upcoming/create/', UpcomingBatchCreateView.as_view()),
    path('inprocess/', InprocessBatchList.as_view()),
    path('inprocess/create/', InprocessBatchCreateView.as_view()),
]
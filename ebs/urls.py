from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from ebs.views import *
from ebs.views.master_data_partners_views import PartnerTypesList
from ebs.views.master_data_partners_views import PartnerTypeUpdateView,PartnerTypeCreateView
from ebs.views.batch_upcoming_views import UpcomingBatchList, \
    UpcomingBatchCreateView, \
    UpcomingBatchUpdateView, \
    UpcomingBatchStartView
from ebs.views.batch_inprocess_views import InprocessBatchList, \
    InprocessBatchCreateView, \
    InprocessBatchDetailView
from ebs.views.batch_inprocess_detail_views import AddObeerDataView
from ebs.views.batch_inprocess_detail_views import RawMaterialsLogView
from ebs.views.batch_inprocess_detail_views import AddRawMaterialsLogView
from ebs.views.batch_inprocess_detail_views import WortQCEntriesView
from ebs.views.batch_inprocess_detail_views import AddWortQCEntryView
from ebs.views.batch_inprocess_detail_views import UpdateWortQCEntryView
from ebs.views.batch_inprocess_detail_views import CreateYeastPitchView
from ebs.views.batch_inprocess_detail_views import UpdateYeastPitchView
from ebs.views.batch_inprocess_detail_views import UpdateActualDatesView
from ebs.views.batch_inprocess_detail_views import FermQCEntriesView
from ebs.views.batch_inprocess_detail_views import AddFermQCEntryView
from ebs.views.batch_inprocess_detail_views import UpdateFermQCEntryView

urlpatterns = [
    #path('', PartnerTypesList.as_view()),
    #path('create', PartnerTypeCreateView.as_view()),
    #path('update/<int:pk>', PartnerTypeUpdateView.as_view()),
    path('upcoming/', UpcomingBatchList.as_view()),
    path('upcoming/create/', UpcomingBatchCreateView.as_view()),
    path('upcoming/update/<int:pk>', UpcomingBatchUpdateView.as_view()),
    path('upcoming/start/<int:pk>', UpcomingBatchStartView.as_view()),
    path('inprocess/', InprocessBatchList.as_view()),
    path('inprocess/create/', InprocessBatchCreateView.as_view()),
    path('inprocess/detail/<int:pk>', InprocessBatchDetailView.as_view(), name='maintenance'),
    path('inprocess/detail/<int:pk>/obeer/', AddObeerDataView.as_view()),
    path('inprocess/detail/<int:pk>/rawmaterials/', RawMaterialsLogView.as_view(), name='rawmaterials'),
    path('inprocess/detail/<int:pk>/rawmaterials/add/', AddRawMaterialsLogView.as_view()),
    path('inprocess/detail/<int:pk>/wortqc/', WortQCEntriesView.as_view(), name='wortqcentries'),
    path('inprocess/detail/<int:bpk>/wortqc/add/', AddWortQCEntryView.as_view()),
    path('inprocess/detail/<int:bpk>/wortqc/update/<int:pk>', UpdateWortQCEntryView.as_view()),
    path('inprocess/detail/<int:bpk>/yeast/', CreateYeastPitchView.as_view()),
    path('inprocess/detail/<int:bpk>/yeast/<int:pk>', UpdateYeastPitchView.as_view()),
    path('inprocess/detail/<int:bpk>/dates/<int:pk>', UpdateActualDatesView.as_view()),
    path('inprocess/detail/<int:pk>/fermqc/', FermQCEntriesView.as_view(), name='fermqcentries'),
    path('inprocess/detail/<int:bpk>/fermqc/add/', AddFermQCEntryView.as_view()),
    path('inprocess/detail/<int:bpk>/fermqc/update/<int:pk>', UpdateFermQCEntryView.as_view()),
]
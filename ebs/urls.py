from django.urls import path
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
from ebs.views.batch_inprocess_detail_views import UpdateRawMaterialsLogView
from ebs.views.batch_inprocess_detail_views import WortQCEntriesView
from ebs.views.batch_inprocess_detail_views import AddWortQCEntryView
from ebs.views.batch_inprocess_detail_views import UpdateWortQCEntryView
from ebs.views.batch_inprocess_detail_views import CreateYeastPitchView
from ebs.views.batch_inprocess_detail_views import UpdateYeastPitchView
from ebs.views.batch_inprocess_detail_views import UpdateActualDatesView
from ebs.views.batch_inprocess_detail_views import FermQCEntriesView
from ebs.views.batch_inprocess_detail_views import AddFermQCEntryView
from ebs.views.batch_inprocess_detail_views import UpdateFermQCEntryView
from ebs.views.batch_inprocess_detail_views import BatchDOEntriesView
from ebs.views.batch_inprocess_detail_views import AddBatchDOEntryView
from ebs.views.batch_inprocess_detail_views import UpdateBatchDOEntryView
from ebs.views.batch_inprocess_detail_views import CreateTransferView
from ebs.views.batch_inprocess_detail_views import UpdateTransferView
from ebs.views.batch_inprocess_detail_views import CreateCarbonationQCView
from ebs.views.batch_inprocess_detail_views import UpdateCarbonationQCView
from ebs.views.batch_inprocess_detail_views import CanningQCView
from ebs.views.batch_inprocess_detail_views import AddCanningQCView
from ebs.views.batch_inprocess_detail_views import UpdateCanningQCView
from ebs.views.batch_inprocess_detail_views import CreatePackagingRunView
from ebs.views.batch_inprocess_detail_views import UpdatePackagingRunView
from ebs.views.batch_inprocess_detail_views import BatchNoteView
from ebs.views.batch_inprocess_detail_views import AddBatchNoteView
from ebs.views.batch_inprocess_detail_views import UpdateBatchNoteView

urlpatterns = [
    path('upcoming/', UpcomingBatchList.as_view()),
    path('upcoming/create/', UpcomingBatchCreateView.as_view()),
    path('upcoming/update/<int:pk>', UpcomingBatchUpdateView.as_view()),
    path('upcoming/start/<int:pk>', UpcomingBatchStartView.as_view()),
    path('inprocess/', InprocessBatchList.as_view()),
    path('inprocess/create/', InprocessBatchCreateView.as_view()),
    path('inprocess/detail/<int:pk>', InprocessBatchDetailView.as_view(), name='maintenance'),
    path('inprocess/detail/<int:pk>/obeer/', AddObeerDataView.as_view()),
    path('inprocess/detail/<int:pk>/rawmaterials/', RawMaterialsLogView.as_view(), name='rawmaterials'),
    path('inprocess/detail/<int:bpk>/rawmaterials/add/', AddRawMaterialsLogView.as_view()),
    path('inprocess/detail/<int:bpk>/rawmaterials/update/<int:pk>', UpdateRawMaterialsLogView.as_view()),
    path('inprocess/detail/<int:pk>/wortqc/', WortQCEntriesView.as_view(), name='wortqcentries'),
    path('inprocess/detail/<int:bpk>/wortqc/add/', AddWortQCEntryView.as_view()),
    path('inprocess/detail/<int:bpk>/wortqc/update/<int:pk>', UpdateWortQCEntryView.as_view()),
    path('inprocess/detail/<int:bpk>/yeast/', CreateYeastPitchView.as_view()),
    path('inprocess/detail/<int:bpk>/yeast/<int:pk>', UpdateYeastPitchView.as_view()),
    path('inprocess/detail/<int:bpk>/dates/<int:pk>', UpdateActualDatesView.as_view()),
    path('inprocess/detail/<int:pk>/fermqc/', FermQCEntriesView.as_view(), name='fermqcentries'),
    path('inprocess/detail/<int:bpk>/fermqc/add/', AddFermQCEntryView.as_view()),
    path('inprocess/detail/<int:bpk>/fermqc/update/<int:pk>', UpdateFermQCEntryView.as_view()),
    path('inprocess/detail/<int:pk>/do/', BatchDOEntriesView.as_view(), name='doentries'),
    path('inprocess/detail/<int:bpk>/do/add/', AddBatchDOEntryView.as_view()),
    path('inprocess/detail/<int:bpk>/do/update/<int:pk>', UpdateBatchDOEntryView.as_view()),
    path('inprocess/detail/<int:bpk>/xfer/', CreateTransferView.as_view(), name='transfer'),
    path('inprocess/detail/<int:bpk>/xfer/<int:pk>', UpdateTransferView.as_view()),
    path('inprocess/detail/<int:bpk>/carb/', CreateCarbonationQCView.as_view()),
    path('inprocess/detail/<int:bpk>/carb/update/<int:pk>', UpdateCarbonationQCView.as_view()),
    path('inprocess/detail/<int:pk>/canqc/', CanningQCView.as_view(), name='canqcentries'),
    path('inprocess/detail/<int:bpk>/canqc/add/', AddCanningQCView.as_view()),
    path('inprocess/detail/<int:bpk>/canqc/update/<int:pk>', UpdateCanningQCView.as_view()),
    path('inprocess/detail/<int:bpk>/package/', CreatePackagingRunView.as_view()),
    path('inprocess/detail/<int:bpk>/package/update/<int:pk>', UpdatePackagingRunView.as_view()),
    path('inprocess/detail/<int:pk>/batchnote/', BatchNoteView.as_view(), name='batchnotes'),
    path('inprocess/detail/<int:bpk>/batchnote/add/', AddBatchNoteView.as_view()),
    path('inprocess/detail/<int:bpk>/batchnote/update/<int:pk>', UpdateBatchNoteView.as_view()),
]

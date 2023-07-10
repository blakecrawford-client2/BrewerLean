from django.urls import path
from django.urls import re_path
from ebs.views.batch_upcoming_views import UpcomingBatchList, \
    UpcomingBatchCreateView, \
    UpcomingBatchUpdateView, \
    UpcomingBatchStartView, \
    UpcomingBatchDeleteView, \
    UpcomingBatchDetailView, \
    UpcomingBatchPkgPlanCreateView, \
    UpcomingBatchPkgPlanUpdateView
from ebs.views.batch_inprocess_views import InprocessBatchList, \
    InprocessBatchCreateView, \
    InprocessBatchDetailView, \
    InProcessBatchPkgPlanCreateView, \
    InProcessBatchPkgPlanUpdateView
from ebs.views.batch_inprocess_detail_views import AddObeerDataView
from ebs.views.batch_inprocess_detail_views import RawMaterialsLogView
from ebs.views.batch_inprocess_detail_views import AddRawMaterialsLogView
from ebs.views.batch_inprocess_detail_views import UpdateRawMaterialsLogView
from ebs.views.batch_inprocess_detail_views import DeleteRawMaterialsLogView
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
from ebs.views.batch_inprocess_detail_views import ChangeFVView
from ebs.views.batch_inprocess_detail_views import CreateYeastCrashHarvestView
from ebs.views.batch_inprocess_detail_views import CreateFinalCrashDateView
from ebs.views.batch_inprocess_detail_views import CreateDryhopDateView
from ebs.views.batch_inprocess_detail_views import PackagePlanView
from ebs.views.batch_close_views import ArchiveBatchListView
from ebs.views.batch_close_views import ArchiveBatchView
from ebs.views.batch_close_views import ArchiveBatchFullView
from ebs.views.reporting_views import OldSchoolBrewSheet
from ebs.views.reporting_views import BatchWortProductionRecord
from ebs.views.reporting_views import BatchRawMaterialsRecord
from ebs.views.reporting_views import BatchFermentationQCRecord
from ebs.views.reporting_views import BigTVStatusReport
from ebs.views.reporting_views import TankStatusReport
from ebs.views.reporting_views import InventoryPressureReportUpcomingOnly

urlpatterns = [
    ##########
    ## Upcoming URLS
    path('upcoming/', UpcomingBatchList.as_view()),
    path('upcoming/create/', UpcomingBatchCreateView.as_view()),
    path('upcoming/update/<int:pk>', UpcomingBatchUpdateView.as_view()),
    path('upcoming/start/<int:pk>', UpcomingBatchStartView.as_view()),
    path('upcoming/delete/<int:pk>', UpcomingBatchDeleteView.as_view()),
    path('upcoming/detail/<int:pk>', UpcomingBatchDetailView.as_view()),
    path('upcoming/detail/<int:bpk>/pkgplanline/create/', UpcomingBatchPkgPlanCreateView.as_view()),
    path('upcoming/detail/<int:bpk>/pkgplanline/update/<int:pk>', UpcomingBatchPkgPlanUpdateView.as_view()),
    ##########
    ## Inprocess URLs
    path('inprocess/', InprocessBatchList.as_view()),
    path('inprocess/create/', InprocessBatchCreateView.as_view()),
    path('inprocess/detail/<int:pk>/', InprocessBatchDetailView.as_view(), name='maintenance'),
    path('inprocess/detail/<int:pk>/changefv/', ChangeFVView.as_view()),
    path('inprocess/detail/<int:pk>/obeer/', AddObeerDataView.as_view()),
    path('inprocess/detail/<int:pk>/rawmaterials/', RawMaterialsLogView.as_view(), name='rawmaterials'),
    path('inprocess/detail/<int:bpk>/rawmaterials/add/', AddRawMaterialsLogView.as_view()),
    path('inprocess/detail/<int:bpk>/rawmaterials/update/<int:pk>', UpdateRawMaterialsLogView.as_view()),
    path('inprocess/detail/<int:bpk>/rawmaterials/delete/<int:pk>', DeleteRawMaterialsLogView.as_view()),
    path('inprocess/detail/<int:pk>/wortqc/', WortQCEntriesView.as_view(), name='wortqcentries'),
    path('inprocess/detail/<int:bpk>/wortqc/add/', AddWortQCEntryView.as_view()),
    path('inprocess/detail/<int:bpk>/wortqc/update/<int:pk>', UpdateWortQCEntryView.as_view()),
    path('inprocess/detail/<int:bpk>/yeast/', CreateYeastPitchView.as_view()),
    path('inprocess/detail/<int:bpk>/yeast/<int:pk>', UpdateYeastPitchView.as_view()),
    path('inprocess/detail/<int:bpk>/dates/<int:pk>', UpdateActualDatesView.as_view()),
    path('inprocess/detail/<int:pk>/fermqc/', FermQCEntriesView.as_view(), name='fermqcentries'),
    path('inprocess/detail/<int:bpk>/fermqc/add/', AddFermQCEntryView.as_view()),
    path('inprocess/detail/<int:bpk>/fermqc/update/<int:pk>', UpdateFermQCEntryView.as_view()),
    path('inprocess/detail/<int:pk>/yeastcrashharvest/', CreateYeastCrashHarvestView.as_view()),
    path('inprocess/detail/<int:bpk>/coldsideaddition/<int:pk>', CreateDryhopDateView.as_view(), name="coldside"),
    path('inprocess/detail/<int:pk>/do/', BatchDOEntriesView.as_view(), name='doentries'),
    path('inprocess/detail/<int:bpk>/do/add/', AddBatchDOEntryView.as_view()),
    path('inprocess/detail/<int:bpk>/do/update/<int:pk>', UpdateBatchDOEntryView.as_view()),
    path('inprocess/detail/<int:bpk>/finalcrash/<int:pk>', CreateFinalCrashDateView.as_view()),
    path('inprocess/detail/<int:bpk>/xfer/', CreateTransferView.as_view(), name='transfer'),
    path('inprocess/detail/<int:bpk>/xfer/<int:pk>', UpdateTransferView.as_view()),
    path('inprocess/detail/<int:pk>/carb/', CreateCarbonationQCView.as_view()),
    path('inprocess/detail/<int:bpk>/carb/update/<int:pk>', UpdateCarbonationQCView.as_view()),
    path('inprocess/detail/<int:pk>/canqc/', CanningQCView.as_view(), name='canqcentries'),
    path('inprocess/detail/<int:bpk>/canqc/add/', AddCanningQCView.as_view()),
    path('inprocess/detail/<int:bpk>/canqc/update/<int:pk>', UpdateCanningQCView.as_view()),
    path('inprocess/detail/<int:bpk>/package/', CreatePackagingRunView.as_view()),
    path('inprocess/detail/<int:bpk>/package/update/<int:pk>', UpdatePackagingRunView.as_view()),
    path('inprocess/detail/<int:pk>/pkgplanline/',PackagePlanView.as_view()),
    path('inprocess/detail/<int:bpk>/pkgplanline/create/', InProcessBatchPkgPlanCreateView.as_view()),
    path('inprocess/detail/<int:bpk>/pkgplanline/update/<int:pk>', InProcessBatchPkgPlanUpdateView.as_view()),
    path('inprocess/detail/<int:pk>/batchnote/', BatchNoteView.as_view(), name='batchnotes'),
    path('inprocess/detail/<int:bpk>/batchnote/add/', AddBatchNoteView.as_view()),
    path('inprocess/detail/<int:bpk>/batchnote/update/<int:pk>', UpdateBatchNoteView.as_view()),
    path('inprocess/detail/<int:pk>/archive/', ArchiveBatchView.as_view()),
    ##########
    ## archive URLs
    path('archive/', ArchiveBatchListView.as_view()),
    path('archive/detail/<int:pk>/', ArchiveBatchFullView.as_view(), name='maintenance-archive'),
    path('archive/detail/<int:pk>/changefv/', ChangeFVView.as_view()),
    path('archive/detail/<int:pk>/obeer/', AddObeerDataView.as_view()),
    path('archive/detail/<int:pk>/rawmaterials/', RawMaterialsLogView.as_view(), name='rawmaterials-archive'),
    path('archive/detail/<int:bpk>/rawmaterials/add/', AddRawMaterialsLogView.as_view()),
    path('archive/detail/<int:bpk>/rawmaterials/update/<int:pk>', UpdateRawMaterialsLogView.as_view()),
    path('archive/detail/<int:bpk>/rawmaterials/delete/<int:pk>', DeleteRawMaterialsLogView.as_view()),
    path('archive/detail/<int:pk>/wortqc/', WortQCEntriesView.as_view(), name='wortqcentries-archive'),
    path('archive/detail/<int:bpk>/wortqc/add/', AddWortQCEntryView.as_view()),
    path('archive/detail/<int:bpk>/wortqc/update/<int:pk>', UpdateWortQCEntryView.as_view()),
    path('archive/detail/<int:bpk>/yeast/', CreateYeastPitchView.as_view()),
    path('archive/detail/<int:bpk>/yeast/<int:pk>', UpdateYeastPitchView.as_view()),
    path('archive/detail/<int:bpk>/dates/<int:pk>', UpdateActualDatesView.as_view()),
    path('archive/detail/<int:pk>/fermqc/', FermQCEntriesView.as_view(), name='fermqcentries-archive'),
    path('archive/detail/<int:bpk>/fermqc/add/', AddFermQCEntryView.as_view()),
    path('archive/detail/<int:bpk>/fermqc/update/<int:pk>', UpdateFermQCEntryView.as_view()),
    path('archive/detail/<int:bpk>/coldsideaddition/<int:pk>', CreateDryhopDateView.as_view(), name="coldside"),
    path('archive/detail/<int:pk>/do/', BatchDOEntriesView.as_view(), name='doentries-archive'),
    path('archive/detail/<int:bpk>/do/add/', AddBatchDOEntryView.as_view()),
    path('archive/detail/<int:bpk>/do/update/<int:pk>', UpdateBatchDOEntryView.as_view()),
    path('archive/detail/<int:bpk>/finalcrash/<int:pk>', CreateFinalCrashDateView.as_view()),
    path('archive/detail/<int:bpk>/xfer/', CreateTransferView.as_view(), name='transfer-archive'),
    path('archive/detail/<int:bpk>/xfer/<int:pk>', UpdateTransferView.as_view()),
    path('archive/detail/<int:bpk>/carb/', CreateCarbonationQCView.as_view()),
    path('archive/detail/<int:bpk>/carb/update/<int:pk>', UpdateCarbonationQCView.as_view()),
    path('archive/detail/<int:pk>/canqc/', CanningQCView.as_view(), name='canqcentries-archive'),
    path('archive/detail/<int:bpk>/canqc/add/', AddCanningQCView.as_view()),
    path('archive/detail/<int:bpk>/canqc/update/<int:pk>', UpdateCanningQCView.as_view()),
    path('archive/detail/<int:bpk>/package/', CreatePackagingRunView.as_view()),
    path('archive/detail/<int:bpk>/package/update/<int:pk>', UpdatePackagingRunView.as_view()),
    path('archive/detail/<int:pk>/batchnote/', BatchNoteView.as_view(), name='batchnotes-archive'),
    path('archive/detail/<int:bpk>/batchnote/add/', AddBatchNoteView.as_view()),
    path('archive/detail/<int:bpk>/batchnote/update/<int:pk>', UpdateBatchNoteView.as_view()),
    ##########
    ## Report URLs
    path('reports/<int:pk>/oldschool/', OldSchoolBrewSheet.as_view()),
    path('reports/<int:pk>/wortproduction/', BatchWortProductionRecord.as_view()),
    path('reports/<int:pk>/rawmaterials/', BatchRawMaterialsRecord.as_view()),
    path('reports/<int:pk>/fermentationqc/', BatchFermentationQCRecord.as_view()),
    path('reports/bigtvstatus/', BigTVStatusReport.as_view()),
    path('reports/tankstatus/', TankStatusReport.as_view()),
    path('reports/invpressupcomingonlycomplete', InventoryPressureReportUpcomingOnly.as_view()),
]

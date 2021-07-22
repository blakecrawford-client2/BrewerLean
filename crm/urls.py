from django.urls import path, re_path
from django.views.generic import TemplateView
from crm.views.account_views import *
from crm.views.call_views import *

urlpatterns = [
    path('', TemplateView.as_view(template_name='crm/home.html')),
    path('accounts/', AccountListView.as_view()),
    path('account-lists/', AccountListsView.as_view(), name='account_lists'),
    path('accounts/on-prem/', AccountListOnPremView.as_view()),
    path('accounts/on-prem/maintenance/', AccountListOnPremMaintenanceView.as_view()),
    path('accounts/on-prem/acquisition/', AccountListOnPremAcquisitionView.as_view()),
    path('accounts/on-prem/prospect/', AccountListOnPremProspectView.as_view()),
    path('accounts/on-prem/dead/', AccountListOnPremDeadView.as_view()),
    path('accounts/off-prem/', AccountListOffPremView.as_view()),
    path('accounts/off-prem/maintenance/', AccountListOffPremMaintenanceView.as_view()),
    path('accounts/off-prem/acquisition/', AccountListOffPremAcquisitionView.as_view()),
    path('accounts/off-prem/prospect/', AccountListOffPremProspectView.as_view()),
    path('accounts/off-prem/dead/', AccountListOffPremDeadView.as_view()),
    path('accounts/create/', CreateAccountView.as_view()),
    path('accounts/<int:pk>/detail/', AccountDetailView.as_view()),
    path('accounts/<int:pk>/update/', AccountUpdateView.as_view()),
    path('calls/account/', FindAccountForCallView.as_view()),
    path('calls/create/', CreateCallView.as_view()),
    path('calls/list/', CallsListView.as_view(), name='call_list'),
    path('calls/wizard/<int:pk>/type/', CreateCallWizardStep1View.as_view()),
    path('calls/wizard/<int:pk>/<int:cpk>/type/', CreateCallWizardStep1View.as_view()),
    path('calls/wizard/<int:pk>/type/<str:type>/method/', CreateCallWizardStep2View.as_view()),
    path('calls/wizard/<int:pk>/<int:cpk>/type/<str:type>/method/', CreateCallWizardStep2View.as_view()),
    path('calls/wizard/<int:pk>/type/<str:type>/method/<str:method>/open/', CreateOpenCallExitAwaitResponse.as_view()),
    path('calls/wizard/<int:pk>/<int:cpk>/type/<str:type>/method/<str:method>/open/', CreateOpenCallExitAwaitResponse.as_view()),
    path('calls/wizard/<int:pk>/type/<str:type>/method/<str:method>/outcome/', CreateCallWizardStep3View.as_view()),
    path('calls/wizard/<int:pk>/<int:cpk>/type/<str:type>/method/<str:method>/outcome/', CreateCallWizardStep3View.as_view()),
    path('calls/wizard/<int:pk>/type/<str:type>/method/<str:method>/outcome/<str:outcome>/followup/', CreateCallWizardStep4View.as_view()),
    path('calls/wizard/<int:pk>/<int:cpk>/type/<str:type>/method/<str:method>/outcome/<str:outcome>/followup/',CreateCallWizardStep4View.as_view()),
    path('calls/wizard/<int:pk>/type/<str:type>/method/<str:method>/outcome/<str:outcome>/followup/<int:fupweeks>/note/', CreateCallWizardStep5View.as_view()),
    path('calls/wizard/<int:pk>/<int:cpk>/type/<str:type>/method/<str:method>/outcome/<str:outcome>/followup/', CreateCallWizardStep4View.as_view()),
    path('calls/wizard/<int:pk>/<int:cpk>/type/<str:type>/method/<str:method>/outcome/<str:outcome>/followup/<int:fupweeks>/note/', CreateCallWizardStep5View.as_view()),
    path('reports/', TemplateView.as_view(template_name='crm/reports/sales-weekly-status.html')),

]

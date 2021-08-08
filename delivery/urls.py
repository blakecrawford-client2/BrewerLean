from django.urls import path, re_path
from django.views.generic import TemplateView
from crm.views.account_views import *
from delivery.views.delivery_views import CreateDeliveryMetricsView
from delivery.views.delivery_views import DeliveryMetricsListView
from delivery.views.delivery_views import UpdateDeliveryMetricsView

urlpatterns = [
    path('', DeliveryMetricsListView.as_view()),
    path('create/', CreateDeliveryMetricsView.as_view()),
    path('update/<int:pk>', UpdateDeliveryMetricsView.as_view()),
]
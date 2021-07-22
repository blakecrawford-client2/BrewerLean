from django.urls import path
from yeast.views.yeast_views import YeastLabListView
from yeast.views.yeast_views import YeastLabCreateView

urlpatterns = [
    path('lab/list/', YeastLabListView.as_view()),
    path('lab/create/', YeastLabCreateView.as_view()),
]

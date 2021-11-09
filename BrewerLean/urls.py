from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from ebs.views import *

##########
# Other than the main landing page, each module is
# responsible for it's own dispatch configurations
urlpatterns = [
    path('',TemplateView.as_view(template_name="index.html")),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('ebs/', include ('ebs.urls')),
    path('crm/', include ('crm.urls')),
    path('yeast/', include ('yeast.urls')),
    path('delivery/', include ('delivery.urls'))
]

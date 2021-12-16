from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from common.views.BLViews import IndexTemplateView
from decouple import config
from ebs.views import *

##########
# Some admin configuration stuff
admin.site.site_header = 'BL1 Administration'
admin.site.site_title = 'BL1 Administration'
admin.site.index_title = 'Bl1 Administration'

##########
# Other than the main landing page, each module is
# responsible for it's own dispatch configurations
if config('USE_GOOGLE_AUTH', cast=bool):
    urlpatterns = [
        path('', IndexTemplateView.as_view(extra_context={'authmethod': 'google'})),
        path('admin/', admin.site.urls),
        path('accounts/', include('allauth.urls')),
        path('ebs/', include ('ebs.urls')),
        path('crm/', include ('crm.urls')),
        path('yeast/', include ('yeast.urls')),
        path('delivery/', include ('delivery.urls'))
    ]
else:
    urlpatterns = [
        path('', TemplateView.as_view(template_name="index.html", extra_context={'authmethod': 'django'})),
        path('admin/', admin.site.urls),
        path('accounts/', include('django.contrib.auth.urls')),
        path('ebs/', include ('ebs.urls')),
        path('crm/', include ('crm.urls')),
        path('yeast/', include ('yeast.urls')),
        path('delivery/', include ('delivery.urls'))
    ]

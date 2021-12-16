from django.contrib import admin
from common.models.module_config_models import BLModule


@admin.register(BLModule)
class BLModuleAdmin(admin.ModelAdmin):
    ordering = ('mod_order',)
    list_display = ('mod_code', 'mod_name', 'mod_url_suffix', 'mod_order', 'mod_enabled')
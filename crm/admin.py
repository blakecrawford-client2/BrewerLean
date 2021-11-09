from django.contrib import admin
from crm.models.crm_models import Account
from crm.models.crm_models import Call
from crm.models.crm_models import Territory


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_name', 'account_type')

@admin.register(Call)
class CallAdmin(admin.ModelAdmin):
    list_display = 'last_modified_on', 'last_modified_by', 'account'

@admin.register(Territory)
class TerritoryAdmin(admin.ModelAdmin):
    list_display = 'territory_code', 'territory_name'

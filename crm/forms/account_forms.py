from django import forms
from crm.models.crm_models import Account

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['account_type',
                  'account_group',
                  'account_name',
                  'ale_owner',
                  'obeer_code']


class AccountSearchForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['id']

from django.db import models
from django.contrib.auth.models import User


class Territory(models.Model):
    class Meta:
        verbose_name_plural='Territories'

    territory_code = models.CharField(max_length=5, default='TERR')
    territory_name = models.CharField(max_length=100)

    def __str__(self):
        return self.territory_name

    def __unicode__(self):
        return self.territory_name


class Account(models.Model):
    class Meta:
        verbose_name_plural='Accounts'
    class AccountType(models.TextChoices):
        PROSPECT = 'P', 'Prospect'
        ACQUISITION = 'A', 'Acquisition'
        MAINTENANCE = 'M', 'Maintenance'
        DEAD = 'D', 'Dead'
    class AccountGroups(models.TextChoices):
        OFFPREM = 'OF', 'Off-Premise'
        ONPREM = 'ON', 'On-Premise'

    account_name = models.CharField(max_length=255)
    account_group = models.CharField(max_length=2,
                                     choices=AccountGroups.choices,
                                     default=AccountGroups.OFFPREM)
    account_type = models.CharField(max_length=1,
                                    choices=AccountType.choices,
                                    default=AccountType.MAINTENANCE)
    obeer_code = models.CharField(max_length=10,
                                  null=True,
                                  blank=True)
    account_territory = models.ForeignKey(Territory,
                                          null=True,
                                          on_delete=models.SET_NULL)
    ale_owner = models.ForeignKey(User,
                                  null=True,
                                  on_delete=models.SET_NULL)

    def __str__(self):
        return self.account_name

    def __unicode__(self):
        return self.account_name


class CallManager(models.Manager):

    def create_fup_call(self, apk, fupmonday, parent_call):
        account = Account.objects.get(id=apk)
        call = self.create(account=account, schedule_week_monday=fupmonday, parent_call=parent_call)
        return call

    def create_call(self, apk, type, method):
        account = Account.objects.get(id=apk)
        call = self.create(account=account, type=type, method=method)
        return call

    def create_call_lmu(self, apk, type, method, rep):
        account = Account.objects.get(id=apk)
        call = self.create(account=account, type=type, method=method, last_modified_by=rep)
        return call


class Call(models.Model):
    class Meta:
        verbose_name_plural = 'Calls'

    class CallTypes(models.TextChoices):
        SALES = 'S', 'Sales'
        COURTESY = 'C', 'Courtesy'
        INVENTORY = 'I', 'Inventory'
        COLLECTION = 'X', 'Collection'

    class ContactMethods(models.TextChoices):
        PHONE = 'P', 'Phone'
        TEXT = 'T', 'Text Message'
        EMAIL = 'E', 'Email'
        VISIT = 'V', 'VISIT'

    class Outcomes(models.TextChoices):
        RADIOSILENT = 'RST', 'Radio Silent'
        ORDER = 'ODR', 'Order'
        LATER_WRONGPERSON = 'LWP', 'Wrong Person'
        LATER_NOTAVAILABLE = 'LNA', 'Later, Not Available'
        LATER_NOSPACE = 'LNS', 'Later, No Space'
        LATER_WAITINGPRODUCT = 'LPD', 'Later, Diff Product'

    class FollowUpDelays(models.IntegerChoices):
        THISWEEK = 0, 'This Week'
        NEXTWEEK = 1, 'Next Week'
        TWOWEEKS = 2, 'In Two Weeks'
        THREEWEEKS = 3, 'In Three Weeks'
        MONTH = 4, 'In A Month'
        THREEMONTHS = 12, 'In Three Months'
        SIXMONTHS = 26, 'In Six Months'

    objects = CallManager()

    account = models.ForeignKey(Account,
                                null=True,
                                on_delete=models.SET_NULL,
                                default=1)
    schedule_week_monday = models.DateField(null=True, blank=True)
    schedule_week = models.IntegerField(null=True, blank=True)

    type = models.CharField(max_length=1,
                            choices=CallTypes.choices,
                            null=True,
                            blank=True)
    method = models.CharField(max_length=1,
                              choices=ContactMethods.choices,
                              null=True,
                              blank=True)
    samples = models.BooleanField(default=False)
    outcome = models.CharField(max_length=3,
                               choices=Outcomes.choices,
                               null=True,
                               blank=True,)
    note = models.TextField(null=True,
                            blank=True,
                            max_length=500)
    parent_call = models.ForeignKey('self',
                                    null=True,
                                    on_delete=models.SET_NULL,
                                    default=None)
    follow_up_required = models.BooleanField(default=True)
    follow_up_delay = models.IntegerField(choices=FollowUpDelays.choices,
                                          default=FollowUpDelays.NEXTWEEK)
    is_confirmed = models.BooleanField(default=False)
    last_modified_on = models.DateField(auto_now=True)
    last_modified_by = models.ForeignKey(User,
                                         null=True,
                                         on_delete=models.SET_NULL,
                                         default=1)
    
    def __str__(self):
        return self.account.account_name \
               + "::" + self.method

    def __unicode__(self):
        return self.account.account_name \
               + "::" + self.method


class Tasting(models.Model):
    class Sentiments(models.TextChoices):
        SMILEYFACE = 'S', 'Smiley Face'
        OKAYFACE = 'O', 'Okay Face'
        FROWNYFACE = 'F', 'Frowny Face'

    tasting_date = models.DateField(null=True,
                                    blank=True)
    at_account = models.ForeignKey(Account,
                                   null=True,
                                   on_delete=models.SET_NULL)
    estimated_interations = models.IntegerField()
    estimated_attributable_units_sold = models.IntegerField()
    estimated_units_used = models.IntegerField()
    sentiment = models.CharField(max_length=1,
                                 choices=Sentiments.choices,
                                 null=True,
                                 blank=True)
    notes = models.TextField(null=True,
                        blank=True,
                        max_length=500)
    last_modified_on = models.DateField(auto_now=True)
    last_modified_by = models.ForeignKey(User,
                                         null=True,
                                         on_delete=models.SET_NULL,
                                         default=1)

    def __str__(self):
        return self.at_account.account_name \
               + "::" + self.sentiment

    def __unicode__(self):
        return self.at_account.account_name \
               + "::" + self.sentiment

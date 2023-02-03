import logging
from django.views.generic import DetailView
from django.views.generic import TemplateView
from django.views.generic import ListView
from ebs.models.brew_sheets import *
from ebs.models.master_data_facilities import Tank

from common.views.BLViews import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView

###
# Status report for the entire brewery, intended to be
# projected on a large TV or projector
class BigTVStatusReport(ListView):
    model = Batch
    context_object_name = 'batches'
    template_name = 'ebs/batch/reports/big-tv-status-report.html'

    def get_queryset(self):
        return Batch.objects.filter(status='IP').order_by('target_fv')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plan_dates'] = BatchPlanDates.objects.filter(batch__status='IP')
        context['act_dates'] = BatchActualDates.objects.filter(batch__status='IP')
        return context

###
# Report to show all wort production QC data by turn
# for a particular batch
class BatchWortProductionRecord(DetailView):
    model = Batch
    context_object_name = 'batch'
    template_name = 'ebs/batch/reports/batch-wort-production-record.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        batch_id = self.kwargs.get('pk')
        context['plan_dates'] = BatchPlanDates.objects.get(batch=batch_id)
        context['act_dates'] = BatchActualDates.objects.get(batch=batch_id)
        context['wort_qc'] = BatchWortQC.objects.filter(batch=batch_id)
        context['yeast'] = BatchYeastPitch.objects.get(batch=batch_id)
        return context

###
# Report to show batch raw materials log, not by turns,
# for a particular batch
class BatchRawMaterialsRecord(DetailView):
    model = Batch
    context_object_name = 'batch'
    template_name = 'ebs/batch/reports/batch-raw-materials-record.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        batch_id = self.kwargs.get('pk')
        context['materials'] = BatchRawMaterialsLog.objects.filter(batch=batch_id)
        context['grain'] = BatchRawMaterialsLog.objects.filter(batch=batch_id, material__material_type='GR')
        context['hops'] = BatchRawMaterialsLog.objects.filter(batch=batch_id, material__material_type='HP')
        context['other'] = BatchRawMaterialsLog.objects.filter(batch=batch_id, material__material_type='OT')
        return context

###
# Report to show the fermentation QC data for
# a particular batch
class BatchFermentationQCRecord(DetailView):
    model = Batch
    context_object_name = 'batch'
    template_name = 'ebs/batch/reports/batch-ferm-qc-record.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        batch_id = self.kwargs.get('pk')
        context['fermqcs'] = BatchFermentationQC.objects.filter(batch=batch_id)
        return context

###
# Generates the OG alementary brew sheet
class OldSchoolBrewSheet(DetailView):
    model = Batch
    context_object_name = 'batch'
    template_name = 'ebs/batch/reports/old-school-brew-sheet.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        batch_id = self.kwargs.get('pk')
        context['plan_dates'] = BatchPlanDates.objects.get(batch=batch_id)
        context['act_dates'] = BatchActualDates.objects.get(batch=batch_id)
        context['wort_qc'] = BatchWortQC.objects.filter(batch=batch_id)
        context['yeast'] = BatchYeastPitch.objects.filter(batch=batch_id)
        context['ferm'] = BatchFermentationQC.objects.filter(batch=batch_id)
        context['notes'] = BatchNote.objects.filter(batch=batch_id)
        return context

###
# Work-in-progress report to show the tank status for
# each tank in a facility
class TankStatusReport(ListView):
    model = Batch
    context_object_name = 'batches'
    template_name = 'ebs/batch/reports/tank-status-report.html'

    def get_queryset(self):
        return Batch.objects.filter(status='IP').order_by('target_fv')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tanks'] = Tank.objects.filter(tank_type='FV').order_by('tank_name')
        context['upcoming_batches'] = Batch.objects.filter(status='PL')
        context['batch_transfers'] = BatchTransfer.objects.filter(batch__status='IP')
        return context


class InventoryPressureReportUpcomingOnly(LoginRequiredMixin, TemplateView):

    template_name = 'ebs/batch/reports/inventory_pressure_upcoming_only.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # first get all upcoming batches
        upcoming_batches = Batch.objects.filter(status='PL')

        # Now get a list of all materials
        all_materials = Material.objects.all()
        # Create a dict of material_name:quantity, where quantity is zero.
        all_materials_dict = {}
        for material in all_materials:
            all_materials_dict[material.material_name] = 0

        # now put them in buckets relative to completeness for inventory
        # pressure purposes
        abstract_complete_batches = []
        pkgplan_abstract_complete_batches = []
        no_abstract_batches = []
        no_pkgplan_batches=[]
        cc_batches = []

        for upcoming_batch in upcoming_batches:

            # figures out if each batch has a package plan
            try:
                pplan = upcoming_batch.package_plan
            except:
                pplan = None
            if not pplan:
                no_pkgplan_batches.append(upcoming_batch)

            # figures out if each batch has a materials abstract
            try:
                matabs = upcoming_batch.batch_product.materials_abstract.all()
            except:
                matabs = None
            if not matabs:
                no_abstract_batches.append(upcoming_batch)

        # finally makes a list of batches clearing both hurdles.
        # this is the list of batches that are computationally complete
        for batch in upcoming_batches:
            if batch not in no_pkgplan_batches and batch not in no_abstract_batches:
                cc_batches.append(batch)

        # use the de-duped list to identify all in-common materials and sum
        # their respective quantities
        for cc_batch in cc_batches:
            for cc_batch_materials in cc_batch.batch_product.materials_abstract.all():
                current_qty = all_materials_dict[cc_batch_materials.material.material_name]
                add_qty = cc_batch_materials.material_qty
                sum_qty = float(current_qty) + float(add_qty)
                all_materials_dict[cc_batch_materials.material.material_name] = sum_qty

        # Treating packaging separately, just for a moment
        for cc_batch in cc_batches:
            pkgplan = cc_batch.package_plan
            cans_12oz_reqd = float(pkgplan.cs_12oz) * 24.0
            cans_16oz_reqd = float(pkgplan.cs_16oz) * 24.0
            ends_reqd = cans_12oz_reqd + cans_16oz_reqd
            short_trays_reqd = pkgplan.cs_12oz
            tall_trays_reqd = pkgplan.cs_16oz
            handles_4pk_reqd = float(pkgplan.cs_16oz) * 6.0
            handles_6pk_reqd = float(pkgplan.cs_12oz) * 4.0



        context["upcoming_full_count"] = len(upcoming_batches)
        context["no_pkg_plan"] = len(no_pkgplan_batches)
        context["no_abstract_batches"] = len(no_abstract_batches)
        context["complete_config_batches_count"] = len(cc_batches)
        context["complete_config_batches"] = cc_batches
        context["materials_dict"] = all_materials_dict
        context["cans_12oz"] = cans_12oz_reqd
        context["cant_16oz"] = cans_16oz_reqd
        context["short_trays"] = short_trays_reqd
        context["tall_trays"] = tall_trays_reqd
        context["handles_4pk"] = handles_4pk_reqd
        context["handles_6pk"] = handles_6pk_reqd
        context["ends"] = ends_reqd
        context["ale_halfs"] = pkgplan.kg_half_owned
        context["ale_sixths"] = pkgplan.kg_sixth_owned
        context["ale_ow_halfs"] = pkgplan.kg_half_oneway
        context["ale_ow_sixths"] = pkgplan.kg_sixth_oneway
        context["client_halfs"] = pkgplan.kg_half_client
        context["client_sixths"] = pkgplan.kg_sixth_client
        context["client_ow_halfs"] = pkgplan.kg_half_client_oneway
        context["client_ow_sixths"] = pkgplan.kg_sixth_client_oneway
        return context
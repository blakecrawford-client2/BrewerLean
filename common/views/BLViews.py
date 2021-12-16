from datetime import datetime

from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from common.models.module_config_models import BLModule


##########
# Simple Mixin to add method to return menu module
# configuration to downstream classes without needing
# to get too crazy w/ subclasses and what have you
class BLModulesMixin:

    def get_modules_context_data(self):
        return BLModule.objects.filter(mod_enabled=True).order_by('mod_order')


##########
# Extended standard class-based views to always include
# the updating user as well as the updating time in the
# y/m/d format.  Create and Update view are required
# for this app's purposes.
class BLDetailView(DetailView, BLModulesMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modules'] = self.get_modules_context_data()
        return context


class BLListView(ListView, BLModulesMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modules'] = self.get_modules_context_data()
        return context


class BLCreateView(CreateView, BLModulesMixin):

    def form_valid(self, form):
        form.instance.last_modified_by = self.request.user
        form.instance.last_modified_on = datetime.today().strftime('%Y-%m-%d')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modules'] = self.get_modules_context_data()
        return context


class BLUpdateView(UpdateView, BLModulesMixin):

    def form_valid(self, form):
        form.instance.last_modified_by = self.request.user
        form.instance.last_modified_on = datetime.today().strftime('%Y-%m-%d')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modules'] = self.get_modules_context_data()
        return context


##########
# Specialized DeleteView to just continue
# without requiring any confirmations step
class BLDeleteWithoutConfirmationView(DeleteView, BLModulesMixin):

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modules'] = self.get_modules_context_data()
        return context


##########
# Specialized TemplateView that allows the configurable
# modules system to display the correct menus
# class BaseTemplateView(TemplateView):
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         modules = BLModule.objects.filter(mod_enabled=True).order_by('mod_order')
#         context['modules'] = modules
#         return context


##########
# Main Index View (moving this from a TemplateView.as_view()
# call made in the urls.py).
class IndexTemplateView(TemplateView, BLModulesMixin):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modules'] = self.get_modules_context_data()
        return context

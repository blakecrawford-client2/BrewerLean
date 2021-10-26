from datetime import datetime
from django.views.generic.edit import FormView, UpdateView, CreateView, DeleteView
from django.views.generic import ListView


##########
# Extended standard class-based viewx to always include
# the updating user as well as the updating time in the
# y/m/d format.  Create and Update view are required
# for this app's purposes.
class BLCreateView(CreateView):
    def form_valid(self, form):
        form.instance.last_modified_by = self.request.user
        form.instance.last_modified_on = datetime.today().strftime('%Y-%m-%d')
        return super().form_valid(form)

class BLUpdateView(UpdateView):
    def form_valid(self, form):
        form.instance.last_modified_by = self.request.user
        form.instance.last_modified_on = datetime.today().strftime('%Y-%m-%d')
        return super().form_valid(form)

##########
# Specialized DeleteView to just continue
# without requiring any confirmations step
class BLDeleteWithoutConfirmationView(DeleteView):
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

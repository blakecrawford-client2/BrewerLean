from datetime import datetime
from django.views.generic.edit import FormView, UpdateView, CreateView, DeleteView
from django.views.generic import ListView

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

class BLDeleteWithoutConfirmationView(DeleteView):
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

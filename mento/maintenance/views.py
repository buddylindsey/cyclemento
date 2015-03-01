from django.core.urlresolvers import reverse_lazy

from django.views.generic import CreateView

from .models import Maintenance
from .forms import MaintenanceForm


class MaintenanceCreateView(CreateView):
    model = Maintenance
    form_class = MaintenanceForm
    success_url = reverse_lazy('dashboard')

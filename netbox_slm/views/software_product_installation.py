from netbox.views import generic
from netbox_slm import filtersets, forms, tables, models
from netbox_slm.models import SoftwareProductInstallation


class SoftwareProductInstallationListView(generic.ObjectListView):
    """View for listing all existing SoftwareProductInstallations."""

    queryset = SoftwareProductInstallation.objects.all()
    filterset = filtersets.SoftwareProductInstallationFilterSet
    filterset_form = forms.SoftwareProductInstallationFilterForm
    table = tables.SoftwareProductInstallationTable


class SoftwareProductInstallationView(generic.ObjectView):
    """Display SoftwareProductInstallation details"""

    queryset = SoftwareProductInstallation.objects.all()


class SoftwareProductInstallationEditView(generic.ObjectEditView):
    """View for editing and creating a SoftwareProductInstallation instance."""

    queryset = SoftwareProductInstallation.objects.all()
    form = forms.SoftwareProductInstallationForm


class SoftwareProductInstallationDeleteView(generic.ObjectDeleteView):
    """View for deleting a SoftwareProductInstallation instance"""

    queryset = SoftwareProductInstallation.objects.all()


class SoftwareProductInstallationBulkDeleteView(generic.BulkDeleteView):
    
    queryset = SoftwareProductInstallation.objects.all()
    table = tables.SoftwareProductInstallationTable

class SoftwareProductInstallationBulkImportView(generic.BulkImportView):
    
    queryset = SoftwareProductInstallation.objects.all()
    table = tables.SoftwareProductInstallationTable
    model_form = forms.SoftwareProductInstallationBulkImportForm

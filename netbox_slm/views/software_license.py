from netbox.views import generic
from netbox_slm import filtersets, forms, tables, models
from netbox_slm.models import SoftwareLicense


class SoftwareLicenseListView(generic.ObjectListView):
    """View for listing all existing SoftwareLicenses."""

    queryset = SoftwareLicense.objects.all()
    filterset = filtersets.SoftwareLicenseFilterSet
    filterset_form = forms.SoftwareLicenseFilterForm
    table = tables.SoftwareLicenseTable


class SoftwareLicenseView(generic.ObjectView):
    """Display SoftwareLicense details"""

    queryset = SoftwareLicense.objects.all()


class SoftwareLicenseEditView(generic.ObjectEditView):
    """View for editing and creating a SoftwareLicense instance."""

    queryset = SoftwareLicense.objects.all()
    form = forms.SoftwareLicenseForm


class SoftwareLicenseDeleteView(generic.ObjectDeleteView):
    """View for deleting a SoftwareLicense instance"""

    queryset = SoftwareLicense.objects.all()


class SoftwareLicenseBulkDeleteView(generic.BulkDeleteView):
    
    queryset = SoftwareLicense.objects.all()
    table = tables.SoftwareLicenseTable
    
     
class SoftwareLicenseBulkImportView(generic.BulkImportView):
    
    queryset = SoftwareLicense.objects.all()
    table = tables.SoftwareLicenseTable

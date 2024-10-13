from netbox.views import generic
from netbox_slm import filtersets, forms, tables, models
from netbox_slm.models import SoftwareProduct


class SoftwareProductListView(generic.ObjectListView):
    """View for listing all existing SoftwareProducts."""

    queryset = SoftwareProduct.objects.all()
    filterset = filtersets.SoftwareProductFilterSet
    filterset_form = forms.SoftwareProductFilterForm
    table = tables.SoftwareProductTable


class SoftwareProductView(generic.ObjectView):
    """Display SoftwareProduct details"""

    queryset = SoftwareProduct.objects.all()

    def get_extra_context(self, request, instance):
        versions = instance.softwareproductversion_set.all()
        return {"versions": versions}


class SoftwareProductEditView(generic.ObjectEditView):
    """View for editing and creating a SoftwareProduct instance."""

    queryset = SoftwareProduct.objects.all()
    form = forms.SoftwareProductForm


class SoftwareProductDeleteView(generic.ObjectDeleteView):
    """View for deleting a SoftwareProduct instance"""
    queryset = SoftwareProduct.objects.all()


class SoftwareProductBulkDeleteView(generic.BulkDeleteView):
    
    queryset = SoftwareProduct.objects.all()
    table = tables.SoftwareProductTable


class SoftwareProductBulkImportView(generic.BulkImportiew):
    
    queryset = SoftwareProduct.objects.all()
    table = tables.SoftwareProductTable
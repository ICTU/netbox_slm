from netbox.views import generic
from netbox_slm.filters import SoftwareProductFilter, SoftwareProductVersionFilter
from netbox_slm.forms import (
    SoftwareProductForm, SoftwareProductFilterForm, SoftwareProductCSVForm, SoftwareProductBulkEditForm,
    SoftwareProductVersionForm, SoftwareProductVersionFilterForm, SoftwareProductVersionCSVForm,
    SoftwareProductVersionBulkEditForm
)
from netbox_slm.models import (
    SoftwareProduct, SoftwareProductVersion
)
from netbox_slm.tables import SoftwareProductTable, SoftwareProductVersionTable


class SoftwareProductListView(generic.ObjectListView):
    """View for listing all existing SoftwareProducts."""

    queryset = SoftwareProduct.objects.all()
    filterset = SoftwareProductFilter
    filterset_form = SoftwareProductFilterForm
    table = SoftwareProductTable
    template_name = "netbox_slm/object_list.html"


class SoftwareProductView(generic.ObjectView):
    """Display SoftwareProduct details"""

    queryset = SoftwareProduct.objects.all()

    def get_extra_context(self, request, instance):
        versions = instance.softwareproduct_versions.all()
        return {"versions": versions}


class SoftwareProductEditView(generic.ObjectEditView):
    """View for editing and creating a SoftwareProduct instance."""

    queryset = SoftwareProduct.objects.all()
    model_form = SoftwareProductForm


class SoftwareProductDeleteView(generic.ObjectDeleteView):
    """View for deleting a SoftwareProduct instance"""

    queryset = SoftwareProduct.objects.all()


class SoftwareProductBulkImportView(generic.BulkImportView):
    queryset = SoftwareProduct.objects.all()
    model_form = SoftwareProductCSVForm
    table = SoftwareProductTable


class SoftwareProductBulkEditView(generic.BulkEditView):
    queryset = SoftwareProduct.objects.all()
    filterset = SoftwareProductFilter
    table = SoftwareProductTable
    form = SoftwareProductBulkEditForm


class SoftwareProductBulkDeleteView(generic.BulkDeleteView):
    queryset = SoftwareProduct.objects.all()
    table = SoftwareProductTable


class SoftwareProductVersionListView(generic.ObjectListView):
    """View for listing all existing SoftwareProductVersions."""

    queryset = SoftwareProductVersion.objects.all()
    filterset = SoftwareProductVersionFilter
    filterset_form = SoftwareProductVersionFilterForm
    table = SoftwareProductVersionTable
    template_name = "netbox_slm/object_list.html"


class SoftwareProductVersionView(generic.ObjectView):
    """Display SoftwareProductVersion details"""

    queryset = SoftwareProductVersion.objects.all()

    # def get_extra_context(self, request, instance):
    #     records = instance.record_set.all()
    #     return {"records": records}


class SoftwareProductVersionEditView(generic.ObjectEditView):
    """View for editing and creating a SoftwareProductVersion instance."""

    queryset = SoftwareProductVersion.objects.all()
    model_form = SoftwareProductVersionForm


class SoftwareProductVersionDeleteView(generic.ObjectDeleteView):
    """View for deleting a SoftwareProductVersion instance"""

    queryset = SoftwareProductVersion.objects.all()


class SoftwareProductVersionBulkImportView(generic.BulkImportView):
    queryset = SoftwareProductVersion.objects.all()
    model_form = SoftwareProductVersionCSVForm
    table = SoftwareProductVersionTable


class SoftwareProductVersionBulkEditView(generic.BulkEditView):
    queryset = SoftwareProductVersion.objects.all()
    filterset = SoftwareProductVersionFilter
    table = SoftwareProductVersionTable
    form = SoftwareProductVersionBulkEditForm


class SoftwareProductVersionBulkDeleteView(generic.BulkDeleteView):
    queryset = SoftwareProductVersion.objects.all()
    table = SoftwareProductVersionTable

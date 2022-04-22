from netbox.views import generic
from netbox_slm import filtersets
from netbox_slm import forms
from netbox_slm import tables
from netbox_slm.models import (
    SoftwareProduct, SoftwareProductVersion, SoftwareProductInstallation
)


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


class SoftwareProductBulkImportView(generic.BulkImportView):
    queryset = SoftwareProduct.objects.all()
    model_form = forms.SoftwareProductCSVForm
    table = tables.SoftwareProductTable


class SoftwareProductBulkEditView(generic.BulkEditView):
    queryset = SoftwareProduct.objects.all()
    filterset = filtersets.SoftwareProductFilterSet
    filterset_form = forms.SoftwareProductFilterForm
    table = tables.SoftwareProductTable
    form = forms.SoftwareProductBulkEditForm


class SoftwareProductBulkDeleteView(generic.BulkDeleteView):
    queryset = SoftwareProduct.objects.all()
    table = tables.SoftwareProductTable


class SoftwareProductVersionListView(generic.ObjectListView):
    """View for listing all existing SoftwareProductVersions."""

    queryset = SoftwareProductVersion.objects.all()
    filterset = filtersets.SoftwareProductVersionFilterSet
    filterset_form = forms.SoftwareProductVersionFilterForm
    table = tables.SoftwareProductVersionTable


class SoftwareProductVersionView(generic.ObjectView):
    """Display SoftwareProductVersion details"""

    queryset = SoftwareProductVersion.objects.all()

    def get_extra_context(self, request, instance):
        installation_count = instance.get_installation_count()
        return {"installations": installation_count}


class SoftwareProductVersionEditView(generic.ObjectEditView):
    """View for editing and creating a SoftwareProductVersion instance."""

    queryset = SoftwareProductVersion.objects.all()
    form = forms.SoftwareProductVersionForm


class SoftwareProductVersionDeleteView(generic.ObjectDeleteView):
    """View for deleting a SoftwareProductVersion instance"""

    queryset = SoftwareProductVersion.objects.all()


class SoftwareProductVersionBulkImportView(generic.BulkImportView):
    queryset = SoftwareProductVersion.objects.all()
    model_form = forms.SoftwareProductVersionCSVForm
    table = tables.SoftwareProductVersionTable


class SoftwareProductVersionBulkEditView(generic.BulkEditView):
    queryset = SoftwareProductVersion.objects.all()
    filterset = filtersets.SoftwareProductVersionFilterSet
    table = tables.SoftwareProductVersionTable
    form = forms.SoftwareProductVersionBulkEditForm


class SoftwareProductVersionBulkDeleteView(generic.BulkDeleteView):
    queryset = SoftwareProductVersion.objects.all()
    table = tables.SoftwareProductVersionTable


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


class SoftwareProductInstallationBulkImportView(generic.BulkImportView):
    queryset = SoftwareProductInstallation.objects.all()
    model_form = forms.SoftwareProductInstallationCSVForm
    table = tables.SoftwareProductInstallationTable


class SoftwareProductInstallationBulkEditView(generic.BulkEditView):
    queryset = SoftwareProductInstallation.objects.all()
    filterset = filtersets.SoftwareProductInstallationFilterSet
    table = tables.SoftwareProductInstallationTable
    form = forms.SoftwareProductInstallationBulkEditForm


class SoftwareProductInstallationBulkDeleteView(generic.BulkDeleteView):
    queryset = SoftwareProductInstallation.objects.all()
    table = tables.SoftwareProductInstallationTable

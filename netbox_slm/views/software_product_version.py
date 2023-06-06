from netbox.views import generic
from netbox_slm import filtersets, forms, tables
from netbox_slm.models import SoftwareProductVersion


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
    model_form = forms.SoftwareProductVersionImportForm
    table = tables.SoftwareProductVersionTable


class SoftwareProductVersionBulkEditView(generic.BulkEditView):
    queryset = SoftwareProductVersion.objects.all()
    filterset = filtersets.SoftwareProductVersionFilterSet
    table = tables.SoftwareProductVersionTable
    form = forms.SoftwareProductVersionBulkEditForm


class SoftwareProductVersionBulkDeleteView(generic.BulkDeleteView):
    queryset = SoftwareProductVersion.objects.all()
    table = tables.SoftwareProductVersionTable

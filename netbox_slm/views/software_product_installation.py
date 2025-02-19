from netbox.views import generic
from netbox_slm import filtersets, forms, tables
from netbox_slm.models import SoftwareProductInstallation
from utilities.views import register_model_view


@register_model_view(SoftwareProductInstallation, "list", path="", detail=False)
class SoftwareProductInstallationListView(generic.ObjectListView):
    queryset = SoftwareProductInstallation.objects.all()
    filterset = filtersets.SoftwareProductInstallationFilterSet
    filterset_form = forms.SoftwareProductInstallationFilterForm
    table = tables.SoftwareProductInstallationTable


@register_model_view(SoftwareProductInstallation)
class SoftwareProductInstallationView(generic.ObjectView):
    queryset = SoftwareProductInstallation.objects.all()


@register_model_view(SoftwareProductInstallation, "add", detail=False)
@register_model_view(SoftwareProductInstallation, "edit")
class SoftwareProductInstallationEditView(generic.ObjectEditView):
    queryset = SoftwareProductInstallation.objects.all()
    form = forms.SoftwareProductInstallationForm


@register_model_view(SoftwareProductInstallation, "delete")
class SoftwareProductInstallationDeleteView(generic.ObjectDeleteView):
    queryset = SoftwareProductInstallation.objects.all()


@register_model_view(SoftwareProductInstallation, "bulk_import", detail=False)
class SoftwareProductInstallationBulkImportView(generic.BulkImportView):
    queryset = SoftwareProductInstallation.objects.all()
    model_form = forms.SoftwareProductInstallationBulkImportForm


@register_model_view(SoftwareProductInstallation, "bulk_edit", path="edit", detail=False)
class SoftwareProductInstallationBulkEditView(generic.BulkEditView):
    queryset = SoftwareProductInstallation.objects.all()
    filterset = filtersets.SoftwareProductInstallationFilterSet
    table = tables.SoftwareProductInstallationTable
    form = forms.SoftwareProductInstallationBulkEditForm


@register_model_view(SoftwareProductInstallation, "bulk_delete", path="delete", detail=False)
class SoftwareProductInstallationBulkDeleteView(generic.BulkDeleteView):
    queryset = SoftwareProductInstallation.objects.all()
    filterset = filtersets.SoftwareProductInstallationFilterSet
    table = tables.SoftwareProductInstallationTable

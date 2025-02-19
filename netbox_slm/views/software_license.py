from netbox.views import generic
from netbox_slm import filtersets, forms, tables
from netbox_slm.models import SoftwareLicense
from utilities.views import register_model_view


@register_model_view(SoftwareLicense, "list", path="", detail=False)
class SoftwareLicenseListView(generic.ObjectListView):
    queryset = SoftwareLicense.objects.all()
    filterset = filtersets.SoftwareLicenseFilterSet
    filterset_form = forms.SoftwareLicenseFilterForm
    table = tables.SoftwareLicenseTable


@register_model_view(SoftwareLicense)
class SoftwareLicenseView(generic.ObjectView):
    queryset = SoftwareLicense.objects.all()


@register_model_view(SoftwareLicense, "add", detail=False)
@register_model_view(SoftwareLicense, "edit")
class SoftwareLicenseEditView(generic.ObjectEditView):
    queryset = SoftwareLicense.objects.all()
    form = forms.SoftwareLicenseForm


@register_model_view(SoftwareLicense, "delete")
class SoftwareLicenseDeleteView(generic.ObjectDeleteView):
    queryset = SoftwareLicense.objects.all()


@register_model_view(SoftwareLicense, "bulk_import", detail=False)
class SoftwareLicenseBulkImportView(generic.BulkImportView):
    queryset = SoftwareLicense.objects.all()
    model_form = forms.SoftwareLicenseBulkImportForm


@register_model_view(SoftwareLicense, "bulk_edit", path="edit", detail=False)
class SoftwareLicenseBulkEditView(generic.BulkEditView):
    queryset = SoftwareLicense.objects.all()
    filterset = filtersets.SoftwareLicenseFilterSet
    table = tables.SoftwareLicenseTable
    form = forms.SoftwareLicenseBulkEditForm


@register_model_view(SoftwareLicense, "bulk_delete", path="delete", detail=False)
class SoftwareLicenseBulkDeleteView(generic.BulkDeleteView):
    queryset = SoftwareLicense.objects.all()
    filterset = filtersets.SoftwareLicenseFilterSet
    table = tables.SoftwareLicenseTable

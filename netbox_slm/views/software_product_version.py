from netbox.views import generic
from netbox_slm import filtersets, forms, tables
from netbox_slm.models import SoftwareProductVersion
from utilities.views import register_model_view


@register_model_view(SoftwareProductVersion, "list", path="", detail=False)
class SoftwareProductVersionListView(generic.ObjectListView):
    queryset = SoftwareProductVersion.objects.all()
    filterset = filtersets.SoftwareProductVersionFilterSet
    filterset_form = forms.SoftwareProductVersionFilterForm
    table = tables.SoftwareProductVersionTable


@register_model_view(SoftwareProductVersion)
class SoftwareProductVersionView(generic.ObjectView):
    queryset = SoftwareProductVersion.objects.all()

    def get_extra_context(self, request, instance):
        installation_count = instance.get_installation_count()
        return {"installations": installation_count}


@register_model_view(SoftwareProductVersion, "add", detail=False)
@register_model_view(SoftwareProductVersion, "edit")
class SoftwareProductVersionEditView(generic.ObjectEditView):
    queryset = SoftwareProductVersion.objects.all()
    form = forms.SoftwareProductVersionForm


@register_model_view(SoftwareProductVersion, "delete")
class SoftwareProductVersionDeleteView(generic.ObjectDeleteView):
    queryset = SoftwareProductVersion.objects.all()


@register_model_view(SoftwareProductVersion, "bulk_import", detail=False)
class SoftwareProductVersionBulkImportView(generic.BulkImportView):
    queryset = SoftwareProductVersion.objects.all()
    model_form = forms.SoftwareProductVersionBulkImportForm


@register_model_view(SoftwareProductVersion, "bulk_edit", path="edit", detail=False)
class SoftwareProductVersionBulkEditView(generic.BulkEditView):
    queryset = SoftwareProductVersion.objects.all()
    filterset = filtersets.SoftwareProductVersionFilterSet
    table = tables.SoftwareProductVersionTable
    form = forms.SoftwareProductVersionBulkEditForm


@register_model_view(SoftwareProductVersion, "bulk_delete", path="delete", detail=False)
class SoftwareProductVersionBulkDeleteView(generic.BulkDeleteView):
    queryset = SoftwareProductVersion.objects.all()
    filterset = filtersets.SoftwareProductVersionFilterSet
    table = tables.SoftwareProductVersionTable

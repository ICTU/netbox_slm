from netbox.plugins import get_plugin_config
from netbox.views import generic
from netbox_slm import filtersets, forms, tables, models
from utilities.views import ViewTab, register_model_view


@register_model_view(models.SoftwareProductVersion, "list", path="", detail=False)
class SoftwareProductVersionListView(generic.ObjectListView):
    queryset = models.SoftwareProductVersion.objects.all()
    filterset = filtersets.SoftwareProductVersionFilterSet
    filterset_form = forms.SoftwareProductVersionFilterForm
    table = tables.SoftwareProductVersionTable


class SoftwareProductVersionTabMixin(generic.ObjectChildrenView):
    queryset = NotImplemented
    hide_column_names = ()
    child_model = models.SoftwareProductVersion
    table = tables.SoftwareProductVersionTable

    tab = ViewTab(
        label=models.SoftwareProductVersion._meta.verbose_name_plural.title(),
        badge=lambda obj: obj.softwareproductversion_set.count(),
        weight=get_plugin_config("netbox_slm", "tab_weight_software_product_version"),
    )

    def get_children(self, request, parent):
        return parent.softwareproductversion_set.restrict(request.user, "view").all()

    def get_table(self, *args, **kwargs):
        installation_table = super().get_table(*args, **kwargs)
        for column_name in self.hide_column_names:
            installation_table.columns.hide(column_name)
        return installation_table


@register_model_view(models.SoftwareProductVersion)
class SoftwareProductVersionView(generic.ObjectView):
    queryset = models.SoftwareProductVersion.objects.all()

    def get_extra_context(self, request, instance):
        installation_count = instance.get_installation_count()
        return {"installations": installation_count}


@register_model_view(models.SoftwareProductVersion, "add", detail=False)
@register_model_view(models.SoftwareProductVersion, "edit")
class SoftwareProductVersionEditView(generic.ObjectEditView):
    queryset = models.SoftwareProductVersion.objects.all()
    form = forms.SoftwareProductVersionForm


@register_model_view(models.SoftwareProductVersion, "delete")
class SoftwareProductVersionDeleteView(generic.ObjectDeleteView):
    queryset = models.SoftwareProductVersion.objects.all()


@register_model_view(models.SoftwareProductVersion, "bulk_import", detail=False)
class SoftwareProductVersionBulkImportView(generic.BulkImportView):
    queryset = models.SoftwareProductVersion.objects.all()
    model_form = forms.SoftwareProductVersionBulkImportForm


@register_model_view(models.SoftwareProductVersion, "bulk_edit", path="edit", detail=False)
class SoftwareProductVersionBulkEditView(generic.BulkEditView):
    queryset = models.SoftwareProductVersion.objects.all()
    filterset = filtersets.SoftwareProductVersionFilterSet
    table = tables.SoftwareProductVersionTable
    form = forms.SoftwareProductVersionBulkEditForm


@register_model_view(models.SoftwareProductVersion, "bulk_delete", path="delete", detail=False)
class SoftwareProductVersionBulkDeleteView(generic.BulkDeleteView):
    queryset = models.SoftwareProductVersion.objects.all()
    filterset = filtersets.SoftwareProductVersionFilterSet
    table = tables.SoftwareProductVersionTable


@register_model_view(models.SoftwareProduct, name="versions")
class SoftwareProductVersionTabListView(SoftwareProductVersionTabMixin):
    queryset = models.SoftwareProduct.objects.all()
    hide_column_names = ("software_product",)

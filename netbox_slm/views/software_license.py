from netbox.plugins import get_plugin_config
from netbox.views import generic
from netbox_slm import filtersets, forms, tables, models
from utilities.views import ViewTab, register_model_view


@register_model_view(models.SoftwareLicense, "list", path="", detail=False)
class SoftwareLicenseListView(generic.ObjectListView):
    queryset = models.SoftwareLicense.objects.all()
    filterset = filtersets.SoftwareLicenseFilterSet
    filterset_form = forms.SoftwareLicenseFilterForm
    table = tables.SoftwareLicenseTable


class SoftwareLicenseTabMixin(generic.ObjectChildrenView):
    queryset = NotImplemented
    hide_column_names = ()
    child_model = models.SoftwareLicense
    table = tables.SoftwareLicenseTable

    tab = ViewTab(
        label=models.SoftwareLicense._meta.verbose_name_plural.title(),
        badge=lambda obj: obj.softwarelicense_set.count(),
        weight=get_plugin_config("netbox_slm", "tab_weight_software_license"),
    )

    def get_children(self, request, parent):
        return parent.softwarelicense_set.restrict(request.user, "view").all()

    def get_table(self, *args, **kwargs):
        installation_table = super().get_table(*args, **kwargs)
        for column_name in self.hide_column_names:
            installation_table.columns.hide(column_name)
        return installation_table


@register_model_view(models.SoftwareLicense)
class SoftwareLicenseView(generic.ObjectView):
    queryset = models.SoftwareLicense.objects.all()


@register_model_view(models.SoftwareLicense, "add", detail=False)
@register_model_view(models.SoftwareLicense, "edit")
class SoftwareLicenseEditView(generic.ObjectEditView):
    queryset = models.SoftwareLicense.objects.all()
    form = forms.SoftwareLicenseForm


@register_model_view(models.SoftwareLicense, "delete")
class SoftwareLicenseDeleteView(generic.ObjectDeleteView):
    queryset = models.SoftwareLicense.objects.all()


@register_model_view(models.SoftwareLicense, "bulk_import", detail=False)
class SoftwareLicenseBulkImportView(generic.BulkImportView):
    queryset = models.SoftwareLicense.objects.all()
    model_form = forms.SoftwareLicenseBulkImportForm


@register_model_view(models.SoftwareLicense, "bulk_edit", path="edit", detail=False)
class SoftwareLicenseBulkEditView(generic.BulkEditView):
    queryset = models.SoftwareLicense.objects.all()
    filterset = filtersets.SoftwareLicenseFilterSet
    table = tables.SoftwareLicenseTable
    form = forms.SoftwareLicenseBulkEditForm


@register_model_view(models.SoftwareLicense, "bulk_delete", path="delete", detail=False)
class SoftwareLicenseBulkDeleteView(generic.BulkDeleteView):
    queryset = models.SoftwareLicense.objects.all()
    filterset = filtersets.SoftwareLicenseFilterSet
    table = tables.SoftwareLicenseTable


@register_model_view(models.SoftwareProduct, name="licenses")
class SoftwareProductLicenseTabListView(SoftwareLicenseTabMixin):
    queryset = models.SoftwareProduct.objects.all()
    hide_column_names = ("software_product",)


@register_model_view(models.SoftwareProductInstallation, name="licenses")
class SoftwareProductInstallationLicenseTabListView(SoftwareLicenseTabMixin):
    queryset = models.SoftwareProductInstallation.objects.all()
    hide_column_names = ("installation",)


@register_model_view(models.SoftwareProductVersion, name="licenses")
class SoftwareProductVersionLicenseTabListView(SoftwareLicenseTabMixin):
    queryset = models.SoftwareProductVersion.objects.all()
    hide_column_names = ("version",)

from dcim.models import Manufacturer
from netbox.plugins import get_plugin_config
from netbox.views import generic
from netbox_slm import filtersets, forms, tables, models
from utilities.views import ViewTab, register_model_view


@register_model_view(models.SoftwareProduct, "list", path="", detail=False)
class SoftwareProductListView(generic.ObjectListView):
    queryset = models.SoftwareProduct.objects.all()
    filterset = filtersets.SoftwareProductFilterSet
    filterset_form = forms.SoftwareProductFilterForm
    table = tables.SoftwareProductTable


class SoftwareProductTabMixin(generic.ObjectChildrenView):
    queryset = NotImplemented
    hide_column_names = ()
    child_model = models.SoftwareProduct
    table = tables.SoftwareProductTable

    tab = ViewTab(
        label=models.SoftwareProduct._meta.verbose_name_plural.title(),
        badge=lambda obj: obj.softwareproduct_set.count(),
        weight=get_plugin_config("netbox_slm", "tab_weight_software_product"),
    )

    def get_children(self, request, parent):
        return parent.softwareproduct_set.restrict(request.user, "view").all()

    def get_table(self, *args, **kwargs):
        installation_table = super().get_table(*args, **kwargs)
        for column_name in self.hide_column_names:
            installation_table.columns.hide(column_name)
        return installation_table


@register_model_view(models.SoftwareProduct)
class SoftwareProductView(generic.ObjectView):
    queryset = models.SoftwareProduct.objects.all()

    def get_extra_context(self, request, instance):
        versions = instance.softwareproductversion_set.all()
        return {"versions": versions}


@register_model_view(models.SoftwareProduct, "add", detail=False)
@register_model_view(models.SoftwareProduct, "edit")
class SoftwareProductEditView(generic.ObjectEditView):
    queryset = models.SoftwareProduct.objects.all()
    form = forms.SoftwareProductForm


@register_model_view(models.SoftwareProduct, "delete")
class SoftwareProductDeleteView(generic.ObjectDeleteView):
    queryset = models.SoftwareProduct.objects.all()


@register_model_view(models.SoftwareProduct, "bulk_import", detail=False)
class SoftwareProductBulkImportView(generic.BulkImportView):
    queryset = models.SoftwareProduct.objects.all()
    model_form = forms.SoftwareProductBulkImportForm


@register_model_view(models.SoftwareProduct, "bulk_edit", path="edit", detail=False)
class SoftwareProductBulkEditView(generic.BulkEditView):
    queryset = models.SoftwareProduct.objects.all()
    filterset = filtersets.SoftwareProductFilterSet
    table = tables.SoftwareProductTable
    form = forms.SoftwareProductBulkEditForm


@register_model_view(models.SoftwareProduct, "bulk_delete", path="delete", detail=False)
class SoftwareProductBulkDeleteView(generic.BulkDeleteView):
    queryset = models.SoftwareProduct.objects.all()
    filterset = filtersets.SoftwareProductFilterSet
    table = tables.SoftwareProductTable


@register_model_view(Manufacturer, name="slm-products")
class ManufacturerProductTabListView(SoftwareProductTabMixin):
    queryset = Manufacturer.objects.all()
    hide_column_names = ("manufacturer",)

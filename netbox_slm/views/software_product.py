from netbox.views import generic
from netbox_slm import filtersets, forms, tables
from netbox_slm.models import SoftwareProduct
from utilities.views import register_model_view


@register_model_view(SoftwareProduct, "list", path="", detail=False)
class SoftwareProductListView(generic.ObjectListView):
    queryset = SoftwareProduct.objects.all()
    filterset = filtersets.SoftwareProductFilterSet
    filterset_form = forms.SoftwareProductFilterForm
    table = tables.SoftwareProductTable


@register_model_view(SoftwareProduct)
class SoftwareProductView(generic.ObjectView):
    queryset = SoftwareProduct.objects.all()

    def get_extra_context(self, request, instance):
        versions = instance.softwareproductversion_set.all()
        return {"versions": versions}


@register_model_view(SoftwareProduct, "add", detail=False)
@register_model_view(SoftwareProduct, "edit")
class SoftwareProductEditView(generic.ObjectEditView):
    queryset = SoftwareProduct.objects.all()
    form = forms.SoftwareProductForm


@register_model_view(SoftwareProduct, "delete")
class SoftwareProductDeleteView(generic.ObjectDeleteView):
    queryset = SoftwareProduct.objects.all()


@register_model_view(SoftwareProduct, "bulk_import", detail=False)
class SoftwareProductBulkImportView(generic.BulkImportView):
    queryset = SoftwareProduct.objects.all()
    model_form = forms.SoftwareProductBulkImportForm


@register_model_view(SoftwareProduct, "bulk_edit", path="edit", detail=False)
class SoftwareProductBulkEditView(generic.BulkEditView):
    queryset = SoftwareProduct.objects.all()
    filterset = filtersets.SoftwareProductFilterSet
    table = tables.SoftwareProductTable
    form = forms.SoftwareProductBulkEditForm


@register_model_view(SoftwareProduct, "bulk_delete", path="delete", detail=False)
class SoftwareProductBulkDeleteView(generic.BulkDeleteView):
    queryset = SoftwareProduct.objects.all()
    filterset = filtersets.SoftwareProductFilterSet
    table = tables.SoftwareProductTable

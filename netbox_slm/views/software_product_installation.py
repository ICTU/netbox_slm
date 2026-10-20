from dcim.models import Device
from netbox.plugins import get_plugin_config
from netbox.views import generic
from netbox_slm import filtersets, forms, tables, models
from utilities.views import ViewTab, register_model_view
from virtualization.models import Cluster, VirtualMachine


@register_model_view(models.SoftwareProductInstallation, name="list", path="", detail=False)
class SoftwareProductInstallationListView(generic.ObjectListView):
    queryset = models.SoftwareProductInstallation.objects.all()
    filterset = filtersets.SoftwareProductInstallationFilterSet
    filterset_form = forms.SoftwareProductInstallationFilterForm
    table = tables.SoftwareProductInstallationTable


class SoftwareProductInstallationTabMixin(generic.ObjectChildrenView):
    queryset = NotImplemented
    hide_column_names = ()
    child_model = models.SoftwareProductInstallation
    table = tables.SoftwareProductInstallationTable

    tab = ViewTab(
        label=models.SoftwareProductInstallation._meta.verbose_name_plural.title(),
        badge=lambda obj: obj.softwareproductinstallation_set.count(),
        weight=get_plugin_config("netbox_slm", "tab_weight_software_product_installation"),
    )

    def get_children(self, request, parent):
        return parent.softwareproductinstallation_set.restrict(request.user, "view").all()

    def get_table(self, *args, **kwargs):
        installation_table = super().get_table(*args, **kwargs)
        for column_name in self.hide_column_names:
            installation_table.columns.hide(column_name)
        return installation_table


@register_model_view(models.SoftwareProductInstallation)
class SoftwareProductInstallationView(generic.ObjectView):
    queryset = models.SoftwareProductInstallation.objects.all()


@register_model_view(models.SoftwareProductInstallation, name="add", detail=False)
@register_model_view(models.SoftwareProductInstallation, name="edit")
class SoftwareProductInstallationEditView(generic.ObjectEditView):
    queryset = models.SoftwareProductInstallation.objects.all()
    form = forms.SoftwareProductInstallationForm


@register_model_view(models.SoftwareProductInstallation, name="delete")
class SoftwareProductInstallationDeleteView(generic.ObjectDeleteView):
    queryset = models.SoftwareProductInstallation.objects.all()


@register_model_view(models.SoftwareProductInstallation, name="bulk_import", detail=False)
class SoftwareProductInstallationBulkImportView(generic.BulkImportView):
    queryset = models.SoftwareProductInstallation.objects.all()
    model_form = forms.SoftwareProductInstallationBulkImportForm


@register_model_view(models.SoftwareProductInstallation, name="bulk_edit", path="edit", detail=False)
class SoftwareProductInstallationBulkEditView(generic.BulkEditView):
    queryset = models.SoftwareProductInstallation.objects.all()
    filterset = filtersets.SoftwareProductInstallationFilterSet
    table = tables.SoftwareProductInstallationTable
    form = forms.SoftwareProductInstallationBulkEditForm


@register_model_view(models.SoftwareProductInstallation, name="bulk_delete", path="delete", detail=False)
class SoftwareProductInstallationBulkDeleteView(generic.BulkDeleteView):
    queryset = models.SoftwareProductInstallation.objects.all()
    filterset = filtersets.SoftwareProductInstallationFilterSet
    table = tables.SoftwareProductInstallationTable


@register_model_view(models.SoftwareProduct, name="installations")
class SoftwareProductInstallationTabListView(SoftwareProductInstallationTabMixin):
    queryset = models.SoftwareProduct.objects.all()
    hide_column_names = ("software_product",)


@register_model_view(models.SoftwareProductVersion, name="installations")
class SoftwareProductVersionInstallationTabListView(SoftwareProductInstallationTabMixin):
    queryset = models.SoftwareProductVersion.objects.all()
    hide_column_names = ("version",)


@register_model_view(Device, name="slm-installations")
class DeviceInstallationTabListView(SoftwareProductInstallationTabMixin):
    queryset = Device.objects.all()
    hide_column_names = ("platform", "type")


@register_model_view(Cluster, name="slm-installations")
class ClusterInstallationTabListView(SoftwareProductInstallationTabMixin):
    queryset = Cluster.objects.all()
    hide_column_names = ("platform", "type")


@register_model_view(VirtualMachine, name="slm-installations")
class VirtualMachineInstallationTabListView(SoftwareProductInstallationTabMixin):
    queryset = VirtualMachine.objects.all()
    hide_column_names = ("platform", "type")

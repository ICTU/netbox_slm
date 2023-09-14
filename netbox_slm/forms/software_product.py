from django import forms

from dcim.models import Manufacturer
from netbox.forms import NetBoxModelForm, NetBoxModelImportForm, NetBoxModelBulkEditForm, NetBoxModelFilterSetForm
from netbox_slm.models import SoftwareProduct
from utilities.forms.fields import DynamicModelChoiceField, TagFilterField


class SoftwareProductForm(NetBoxModelForm):
    """Form for creating a new SoftwareProduct object."""

    manufacturer = DynamicModelChoiceField(
        queryset=Manufacturer.objects.all(),
        required=True,
    )

    class Meta:
        model = SoftwareProduct
        fields = ("name", "manufacturer", "description", "tags")


class SoftwareProductFilterForm(NetBoxModelFilterSetForm):
    model = SoftwareProduct
    fieldsets = ((None, ("q", "tag")),)

    tag = TagFilterField(model)


class SoftwareProductImportForm(NetBoxModelImportForm):
    class Meta:
        model = SoftwareProduct
        fields = (
            "name",
            "manufacturer",
        )


class SoftwareProductBulkEditForm(NetBoxModelBulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=SoftwareProduct.objects.all(),
        widget=forms.MultipleHiddenInput(),
    )

    class Meta:
        model = SoftwareProduct
        nullable_fields = []

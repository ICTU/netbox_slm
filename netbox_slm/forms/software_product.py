from django import forms

from dcim.models import Manufacturer
from netbox.forms import NetBoxModelForm, NetBoxModelImportForm, NetBoxModelBulkEditForm, NetBoxModelFilterSetForm
from netbox_slm.models import SoftwareProduct
from utilities.forms.fields import CommentField, DynamicModelChoiceField, TagFilterField
from utilities.forms.rendering import FieldSet


class SoftwareProductForm(NetBoxModelForm):
    """Form for creating a new SoftwareProduct object."""

    comments = CommentField()

    manufacturer = DynamicModelChoiceField(
        queryset=Manufacturer.objects.all(),
        required=True,
    )

    class Meta:
        model = SoftwareProduct
        fields = (
            "name",
            "description",
            "manufacturer",
            "tags",
            "comments",
        )


class SoftwareProductFilterForm(NetBoxModelFilterSetForm):
    model = SoftwareProduct
    fieldsets = (FieldSet(None, ("q", "tag")),)
    tag = TagFilterField(model)


class SoftwareProductImportForm(NetBoxModelImportForm):
    class Meta:
        model = SoftwareProduct
        fields = (
            "name",
            "description",
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

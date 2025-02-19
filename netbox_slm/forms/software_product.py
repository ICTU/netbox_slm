from django.forms import CharField

from dcim.models import Manufacturer
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm, NetBoxModelImportForm, NetBoxModelBulkEditForm
from netbox_slm.models import SoftwareProduct
from utilities.forms.fields import (
    CommentField,
    DynamicModelChoiceField,
    TagFilterField,
    DynamicModelMultipleChoiceField,
)
from utilities.forms.rendering import FieldSet


class SoftwareProductForm(NetBoxModelForm):
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
    fieldsets = (
        FieldSet("q", "filter_id", "tag"),
        FieldSet("name", "description", "manufacturer_id"),
    )
    selector_fields = ("q", "filter_id", "name")

    tag = TagFilterField(model)

    name = CharField(required=False)
    description = CharField(required=False)
    manufacturer_id = DynamicModelMultipleChoiceField(
        queryset=Manufacturer.objects.all(),
        required=False,
        label="Manufacturer",
    )


class SoftwareProductBulkImportForm(NetBoxModelImportForm):
    class Meta:
        model = SoftwareProduct
        fields = (
            "name",
            "description",
            "manufacturer",
            "tags",
        )


class SoftwareProductBulkEditForm(NetBoxModelBulkEditForm):
    model = SoftwareProduct
    fieldsets = (FieldSet("manufacturer"),)
    nullable_fields = ("manufacturer", "comments")

    tag = TagFilterField(model)
    comments = CommentField()

    manufacturer = DynamicModelChoiceField(
        queryset=Manufacturer.objects.all(),
        required=False,
    )

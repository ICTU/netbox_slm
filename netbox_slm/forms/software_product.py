from django.forms import CharField

from dcim.models import Manufacturer
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm, NetBoxModelImportForm
from netbox_slm.models import SoftwareProduct
from utilities.forms.fields import (
    CommentField,
    DynamicModelChoiceField,
    TagFilterField,
    DynamicModelMultipleChoiceField,
)
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
    fieldsets = (
        FieldSet("q", "filter_id", "tag"),
        FieldSet("name", "description", "manufacturer"),
    )
    selector_fields = ("q", "filter_id", "name")

    tag = TagFilterField(model)

    name = CharField(required=False)
    description = CharField(required=False)
    manufacturer = DynamicModelMultipleChoiceField(
        queryset=Manufacturer.objects.all(),
        required=False,
    )


class SoftwareProductBulkImportForm(NetBoxModelImportForm):
    class Meta:
        model = SoftwareProduct
        fields = (
            "name",
            "description",
            "manufacturer",
            "tags",
            "comments",
        )

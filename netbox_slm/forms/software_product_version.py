from django.forms import DateField
from django.urls import reverse_lazy

from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from netbox_slm.models import SoftwareProduct, SoftwareProductVersion
from utilities.forms.fields import CommentField, DynamicModelChoiceField, TagFilterField
from utilities.forms.rendering import FieldSet
from utilities.forms.widgets import APISelect, DatePicker


class SoftwareProductVersionForm(NetBoxModelForm):
    """Form for creating a new SoftwareProductVersion object."""

    comments = CommentField()

    release_date = DateField(required=False, widget=DatePicker())
    end_of_support = DateField(required=False, widget=DatePicker())

    software_product = DynamicModelChoiceField(
        queryset=SoftwareProduct.objects.all(),
        widget=APISelect(attrs={"data-url": reverse_lazy("plugins-api:netbox_slm-api:softwareproduct-list")}),
    )

    class Meta:
        model = SoftwareProductVersion
        fields = (
            "name",
            "release_date",
            "documentation_url",
            "end_of_support",
            "filename",
            "file_checksum",
            "file_link",
            "release_type",
            "software_product",
            "tags",
            "comments",
        )


class SoftwareProductVersionFilterForm(NetBoxModelFilterSetForm):
    model = SoftwareProductVersion
    fieldsets = (FieldSet(None, ("q", "tag")),)
    tag = TagFilterField(model)

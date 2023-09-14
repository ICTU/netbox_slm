from django import forms
from django.urls import reverse_lazy
from django.utils.translation import gettext as _

from netbox.forms import NetBoxModelForm, NetBoxModelImportForm, NetBoxModelBulkEditForm, NetBoxModelFilterSetForm
from netbox_slm.models import SoftwareProduct, SoftwareProductVersion
from utilities.forms.fields import DynamicModelChoiceField, TagFilterField
from utilities.forms.widgets import APISelect


class SoftwareProductVersionForm(NetBoxModelForm):
    """Form for creating a new SoftwareProductVersion object."""
    name = forms.CharField(label=_("Version"))

    software_product = DynamicModelChoiceField(
        queryset=SoftwareProduct.objects.all(),
        widget=APISelect(
            attrs={"data-url": reverse_lazy("plugins-api:netbox_slm-api:softwareproduct-list")}
        ),
    )

    class Meta:
        model = SoftwareProductVersion
        fields = ("name", "software_product", "tags")


class SoftwareProductVersionFilterForm(NetBoxModelFilterSetForm):
    model = SoftwareProductVersion
    fieldsets = (
        (None, ('q', 'tag')),
    )

    tag = TagFilterField(model)


class SoftwareProductVersionImportForm(NetBoxModelImportForm):
    class Meta:
        model = SoftwareProductVersion
        fields = ("name",)


class SoftwareProductVersionBulkEditForm(NetBoxModelBulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=SoftwareProduct.objects.all(),
        widget=forms.MultipleHiddenInput(),
    )

    class Meta:
        model = SoftwareProductVersion
        nullable_fields = []

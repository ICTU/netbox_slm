from django import forms
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from extras.forms import (
    CustomFieldModelForm,
    CustomFieldModelCSVForm,
    AddRemoveTagsForm,
    CustomFieldModelBulkEditForm,
    CustomFieldModelFilterForm,
)
from dcim.models import Manufacturer, Device
from netbox_slm.models import SoftwareProduct, SoftwareProductVersion, SoftwareProductInstallation
from utilities.forms import (
    BootstrapMixin, DynamicModelChoiceField, APISelect, DynamicModelMultipleChoiceField
)
from virtualization.models import VirtualMachine


class SoftwareProductForm(BootstrapMixin, CustomFieldModelForm):
    """Form for creating a new SoftwareProduct object."""

    manufacturer = DynamicModelChoiceField(
        queryset=Manufacturer.objects.all(),
        required=False,
        # initial_params={
        #     'device_types': 'device_type'
        # }
    )

    # tags = DynamicModelMultipleChoiceField(
    #     queryset=Tag.objects.all(),
    #     required=False,
    # )

    class Meta:
        model = SoftwareProduct
        fields = ("name", "manufacturer", "description",)  # "tags")


class SoftwareProductFilterForm(BootstrapMixin, CustomFieldModelFilterForm):
    """Form for filtering SoftwareProduct instances."""

    model = SoftwareProduct

    q = forms.CharField(required=False, label="Search")

    name = forms.CharField(
        required=False,
        label="Name",
    )

    # tag = TagFilterField(SoftwareProduct)


class SoftwareProductCSVForm(CustomFieldModelCSVForm):
    class Meta:
        model = SoftwareProduct
        fields = ("name",)


class SoftwareProductBulkEditForm(BootstrapMixin, AddRemoveTagsForm, CustomFieldModelBulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=SoftwareProduct.objects.all(),
        widget=forms.MultipleHiddenInput(),
    )

    class Meta:
        nullable_fields = []


class SoftwareProductVersionForm(BootstrapMixin, CustomFieldModelForm):
    """Form for creating a new SoftwareProductVersion object."""
    name = forms.CharField(label=_("Version"))

    software_product = DynamicModelChoiceField(
        queryset=SoftwareProduct.objects.all(),
        required=False,
        widget=APISelect(
            attrs={"data-url": reverse_lazy("plugins-api:netbox_slm-api:softwareproduct-list")}
        ),
    )

    # tags = DynamicModelMultipleChoiceField(
    #     queryset=Tag.objects.all(),
    #     required=False,
    # )

    class Meta:
        model = SoftwareProductVersion
        fields = ("name", "software_product",)  # "tags")

    # def clean(self):
    #     import pdb;pdb.set_trace()
    #     return super(SoftwareProductVersionForm, self).clean()


class SoftwareProductVersionFilterForm(BootstrapMixin, CustomFieldModelFilterForm):
    """Form for filtering SoftwareProductVersion instances."""

    model = SoftwareProductVersion

    q = forms.CharField(required=False, label="Search")

    name = forms.CharField(
        required=False,
        label="Name",
    )

    # tag = TagFilterField(SoftwareProduct)


class SoftwareProductVersionCSVForm(CustomFieldModelCSVForm):
    class Meta:
        model = SoftwareProductVersion
        fields = ("name",)


class SoftwareProductVersionBulkEditForm(BootstrapMixin, AddRemoveTagsForm, CustomFieldModelBulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=SoftwareProduct.objects.all(),
        widget=forms.MultipleHiddenInput(),
    )

    class Meta:
        nullable_fields = []


class SoftwareProductInstallationForm(BootstrapMixin, CustomFieldModelForm):
    """Form for creating a new SoftwareProductInstallation object."""

    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        required=False,
        # initial_params={
        #     'device_types': 'device_type'
        # }
    )
    virtualmachine = DynamicModelChoiceField(
        queryset=VirtualMachine.objects.all(),
        required=False,
        # initial_params={
        #     'device_types': 'device_type'
        # }
    )
    software_product = DynamicModelChoiceField(
        queryset=SoftwareProduct.objects.all(),
        required=True,
        widget=APISelect(
            attrs={"data-url": reverse_lazy("plugins-api:netbox_slm-api:softwareproduct-list")}
        ),
    )
    version = DynamicModelChoiceField(
        queryset=SoftwareProductVersion.objects.all(),
        required=True,
        widget=APISelect(
            attrs={"data-url": reverse_lazy("plugins-api:netbox_slm-api:softwareproductversion-list")}
        ),
        query_params={
            'software_product': '$software_product',
        }
    )

    # todo need version and device ?

    # tags = DynamicModelMultipleChoiceField(
    #     queryset=Tag.objects.all(),
    #     required=False,
    # )

    class Meta:
        model = SoftwareProductInstallation
        fields = ("device", "virtualmachine", "software_product", "version",)  # "tags")

    # def clean(self):
    #     import pdb;pdb.set_trace()
    #     return super(SoftwareProductInstallationForm, self).clean()


class SoftwareProductInstallationFilterForm(BootstrapMixin, CustomFieldModelFilterForm):
    """Form for filtering SoftwareProductInstallation instances."""

    model = SoftwareProductInstallation

    q = forms.CharField(required=False, label="Search")

    # tag = TagFilterField(SoftwareProduct)


class SoftwareProductInstallationCSVForm(CustomFieldModelCSVForm):
    class Meta:
        model = SoftwareProductInstallation
        fields = tuple()


class SoftwareProductInstallationBulkEditForm(BootstrapMixin, AddRemoveTagsForm, CustomFieldModelBulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=SoftwareProductInstallation.objects.all(),
        widget=forms.MultipleHiddenInput(),
    )

    class Meta:
        nullable_fields = []

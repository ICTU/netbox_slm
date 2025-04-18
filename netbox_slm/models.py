from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.html import format_html, urlencode
from license_expression import Licensing, get_spdx_licensing

from netbox.models import NetBoxModel
from utilities.querysets import RestrictedQuerySet
from utilities.validators import EnhancedURLValidator

spdx_licensing: Licensing = get_spdx_licensing()


class LaxURLField(models.URLField):
    """
    NetBox Custom Field approach, based on utilities.forms.fields.LaxURLField
    Overriding default_validators is needed, as they are always added
    """

    default_validators = [EnhancedURLValidator()]


class SoftwareProduct(NetBoxModel):
    name = models.CharField(max_length=128)
    comments = models.TextField(blank=True)

    description = models.CharField(max_length=255, null=True, blank=True)
    manufacturer = models.ForeignKey(to="dcim.Manufacturer", on_delete=models.PROTECT, null=True, blank=True)

    objects = RestrictedQuerySet.as_manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:netbox_slm:softwareproduct", kwargs={"pk": self.pk})

    def get_installation_count(self):
        count = SoftwareProductInstallation.objects.filter(software_product_id=self.pk).count()
        query_string = urlencode(dict(software_product_id=self.pk))
        search_target = reverse("plugins:netbox_slm:softwareproductinstallation_list")
        # Can be composed directly with reverse(query=) in Django 5.2, see https://code.djangoproject.com/ticket/25582
        return format_html(f"<a href='{search_target}?{query_string}'>{count}</a>") if count else "0"


class SoftwareReleaseTypes(models.TextChoices):
    ALPHA = "A", "Alpha"
    BETA = "B", "Beta"
    RELEASE_CANDIDATE = "RC", "Release candidate"
    STABLE = "S", "Stable release"


class SoftwareProductVersion(NetBoxModel):
    name = models.CharField(max_length=64)
    comments = models.TextField(blank=True)

    description = models.CharField(max_length=255, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    documentation_url = LaxURLField(max_length=1024, null=True, blank=True)
    end_of_support = models.DateField(null=True, blank=True)
    filename = models.CharField(max_length=64, null=True, blank=True)
    file_checksum = models.CharField(max_length=128, null=True, blank=True)
    file_link = LaxURLField(max_length=1024, null=True, blank=True)

    release_type = models.CharField(
        max_length=3,
        choices=SoftwareReleaseTypes.choices,
        default=SoftwareReleaseTypes.STABLE,
    )

    software_product = models.ForeignKey(
        to="netbox_slm.SoftwareProduct",
        on_delete=models.PROTECT,
    )

    objects = RestrictedQuerySet.as_manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:netbox_slm:softwareproductversion", kwargs={"pk": self.pk})

    def get_installation_count(self):
        count = SoftwareProductInstallation.objects.filter(version_id=self.pk).count()
        query_string = urlencode(dict(version_id=self.pk))
        search_target = reverse("plugins:netbox_slm:softwareproductinstallation_list")
        # Can be composed directly with reverse(query=) in Django 5.2, see https://code.djangoproject.com/ticket/25582
        return format_html(f"<a href='{search_target}?{query_string}'>{count}</a>") if count else "0"


class SoftwareProductInstallation(NetBoxModel):
    comments = models.TextField(blank=True)

    device = models.ForeignKey(to="dcim.Device", on_delete=models.PROTECT, null=True, blank=True)
    virtualmachine = models.ForeignKey(
        to="virtualization.VirtualMachine", on_delete=models.PROTECT, null=True, blank=True
    )
    cluster = models.ForeignKey(to="virtualization.Cluster", on_delete=models.PROTECT, null=True, blank=True)
    software_product = models.ForeignKey(to="netbox_slm.SoftwareProduct", on_delete=models.PROTECT)
    version = models.ForeignKey(to="netbox_slm.SoftwareProductVersion", on_delete=models.PROTECT)

    objects = RestrictedQuerySet.as_manager()

    def __str__(self):
        return f"{self.pk} ({self.platform})"

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_platform",
                check=(
                    models.Q(device__isnull=False, virtualmachine__isnull=True, cluster__isnull=True)
                    | models.Q(device__isnull=True, virtualmachine__isnull=False, cluster__isnull=True)
                    | models.Q(device__isnull=True, virtualmachine__isnull=True, cluster__isnull=False)
                ),
                violation_error_message="Installation requires exactly one platform destination.",
            )
        ]

    def get_absolute_url(self):
        return reverse("plugins:netbox_slm:softwareproductinstallation", kwargs={"pk": self.pk})

    @property
    def platform(self):
        return self.device or self.virtualmachine or self.cluster

    def render_type(self):
        if self.device:
            return "device"
        if self.virtualmachine:
            return "virtualmachine"
        return "cluster"


def spdx_license_names():
    names = [(item[0], item[0]) for item in spdx_licensing.known_symbols.items() if not item[1].is_exception]
    names.sort()
    names.insert(0, ("", "---------"))  # set default value
    return names


def validate_spdx_expression(value):
    expression_info = spdx_licensing.validate(value)
    if expression_info.errors:
        raise ValidationError(f"{value} is not a known SPDX license expression")


class SoftwareLicense(NetBoxModel):
    name = models.CharField(max_length=128)
    comments = models.TextField(blank=True)

    description = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=128)
    spdx_expression = models.CharField(max_length=64, null=True, blank=True, validators=[validate_spdx_expression])
    stored_location = models.CharField(max_length=255, null=True, blank=True)
    stored_location_url = LaxURLField(max_length=1024, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)
    support = models.BooleanField(default=None, null=True, blank=True)
    license_amount = models.PositiveIntegerField(default=None, null=True, blank=True)

    software_product = models.ForeignKey(to="netbox_slm.SoftwareProduct", on_delete=models.PROTECT)
    version = models.ForeignKey(to="netbox_slm.SoftwareProductVersion", on_delete=models.PROTECT, null=True, blank=True)
    installation = models.ForeignKey(
        to="netbox_slm.SoftwareProductInstallation", on_delete=models.SET_NULL, null=True, blank=True
    )

    objects = RestrictedQuerySet.as_manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:netbox_slm:softwarelicense", kwargs={"pk": self.pk})

    @property
    def stored_location_txt(self):
        if self.stored_location_url and not self.stored_location:
            return "Link"
        return self.stored_location

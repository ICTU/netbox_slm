from django.db import models
from django.urls import reverse
from extras.utils import extras_features
from netbox.models import PrimaryModel
from utilities.querysets import RestrictedQuerySet


# @extras_features('custom_fields', 'custom_links', 'export_templates', 'tags', 'webhooks')
class SoftwareProduct(PrimaryModel):
    """
    A SoftwareProduct represents ...
    """
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    
    manufacturer = models.ForeignKey(
        to='dcim.Manufacturer',
        on_delete=models.PROTECT,
        related_name='software_products'
    )

    objects = RestrictedQuerySet.as_manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:netbox_slm:softwareproduct", kwargs={"pk": self.pk})


# @extras_features('custom_fields', 'custom_links', 'export_templates', 'tags', 'webhooks')
class SoftwareProductVersion(PrimaryModel):
    software_product = models.ForeignKey(
        to='netbox_slm.SoftwareProduct',
        on_delete=models.PROTECT,
        related_name='softwareproduct_versions'
    )
    name = models.CharField(max_length=64)

    objects = RestrictedQuerySet.as_manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:netbox_slm:softwareproductversion", kwargs={"pk": self.pk})


# @extras_features('custom_fields', 'custom_links', 'export_templates', 'tags', 'webhooks')
class SoftwareProductInstallation(PrimaryModel):
    device = models.ForeignKey(
        to='dcim.Device',
        on_delete=models.PROTECT,
        related_name='softwareproduct_installations'
    )
    # virtualmachine = models.ForeignKey(
    #     to='virtualization.VirtualMachine',
    #     on_delete=models.PROTECT,
    #     related_name='softwareproduct_installations'
    # )
    software_product = models.ForeignKey(
        to='netbox_slm.SoftwareProduct',
        on_delete=models.PROTECT,
        related_name='software_products'
    )
    version = models.ForeignKey(
        to='netbox_slm.SoftwareProductVersion',
        on_delete=models.PROTECT,
        related_name='softwareproduct_versions'
    )

    objects = RestrictedQuerySet.as_manager()

    def __str__(self):
        return f"{self.pk}"

    def get_absolute_url(self):
        return reverse("plugins:netbox_slm:softwareproductinstallation", kwargs={"pk": self.pk})

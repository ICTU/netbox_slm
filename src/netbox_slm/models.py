from django.db import models
from django.urls import reverse, reverse_lazy
from django.utils import safestring

from netbox.models import NetBoxModel
from utilities.querysets import RestrictedQuerySet


class SoftwareProduct(NetBoxModel):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=255, null=True, blank=True)
    
    manufacturer = models.ForeignKey(
        to='dcim.Manufacturer',
        on_delete=models.PROTECT,
        null=True, blank=True
    )

    objects = RestrictedQuerySet.as_manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:netbox_slm:softwareproduct", kwargs={"pk": self.pk})

    def get_installation_count(self):
        count = SoftwareProductInstallation.objects.filter(software_product_id=self.pk).count()
        return safestring.mark_safe("<a href=\"{url}\">{count}</a>".format(
            url=reverse_lazy("plugins:netbox_slm:softwareproductinstallation_list") + f"?q={self.name}",
            count=count
        )) if count else "0"


class SoftwareProductVersion(NetBoxModel):
    software_product = models.ForeignKey(
        to='netbox_slm.SoftwareProduct',
        on_delete=models.PROTECT,
    )
    name = models.CharField(max_length=64)

    objects = RestrictedQuerySet.as_manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:netbox_slm:softwareproductversion", kwargs={"pk": self.pk})

    def get_installation_count(self):
        count = SoftwareProductInstallation.objects.filter(version_id=self.pk).count()
        return safestring.mark_safe("<a href=\"{url}\">{count}</a>".format(
            url=reverse_lazy("plugins:netbox_slm:softwareproductinstallation_list") + f"?q={self.name}",
            count=count
        )) if count else "0"


class SoftwareProductInstallation(NetBoxModel):
    device = models.ForeignKey(
        to='dcim.Device',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    virtualmachine = models.ForeignKey(
        to='virtualization.VirtualMachine',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    software_product = models.ForeignKey(
        to='netbox_slm.SoftwareProduct',
        on_delete=models.PROTECT,
    )
    version = models.ForeignKey(
        to='netbox_slm.SoftwareProductVersion',
        on_delete=models.PROTECT,
    )

    objects = RestrictedQuerySet.as_manager()

    def __str__(self):
        return f"{self.pk}"

    def get_absolute_url(self):
        return reverse("plugins:netbox_slm:softwareproductinstallation", kwargs={"pk": self.pk})

    def get_platform(self):
        return self.device or self.virtualmachine

    def render_type(self):
        return f"{'device' if self.device else 'virtualmachine'}"

"""
clear the database from develop/test values set by fill_db
"""

import django

django.setup()  # before other imports

from dcim.models import Device, DeviceRole, DeviceType, Manufacturer, Site
from virtualization.models import Cluster, ClusterGroup, ClusterType, VirtualMachine

from netbox_slm.models import (
    SoftwareProduct,
    SoftwareProductInstallation,
    SoftwareProductVersion,
    SoftwareLicense,
)


SoftwareProductInstallation.objects.all().delete()
SoftwareLicense.objects.all().delete()
SoftwareProductVersion.objects.all().delete()
SoftwareProduct.objects.all().delete()
VirtualMachine.objects.all().delete()
Device.objects.all().delete()
DeviceRole.objects.all().delete()
DeviceType.objects.all().delete()
Cluster.objects.all().delete()
ClusterGroup.objects.all().delete()
ClusterType.objects.all().delete()
Manufacturer.objects.all().delete()
Site.objects.all().delete()

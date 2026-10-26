from django.test import TestCase

from dcim.models import Device, DeviceRole, DeviceType, Manufacturer, Site
from netbox_slm.models import SoftwareProduct, SoftwareProductVersion, SoftwareProductInstallation, SoftwareLicense
from virtualization.models import Cluster, ClusterType, VirtualMachine


class SlmBaseTestCase(TestCase):
    p_name: str = "test product"
    v_name: str = "test version"
    l_name: str = "test license"
    test_url: str = "https://github.com/ICTU/netbox_slm"
    cluster: Cluster
    device: Device
    vm: VirtualMachine
    software_product: SoftwareProduct
    software_product_version: SoftwareProductVersion
    software_product_installation: SoftwareProductInstallation

    @classmethod
    def setUpTestData(cls):
        manufacturer = Manufacturer.objects.create(name="test manufacturer")
        device_type = DeviceType.objects.create(model="test device type", manufacturer=manufacturer)
        device_role = DeviceRole.objects.create(name="test device role")
        site = Site.objects.create(name="test site")
        cls.device = Device.objects.create(name="test device", device_type=device_type, role=device_role, site=site)
        cls.vm = VirtualMachine.objects.create(name="test VM")
        cluster_type = ClusterType.objects.create(name="test cluster type")
        cls.cluster = Cluster.objects.create(name="test cluster", type=cluster_type)

        cls.bulk_edit_data = {"comments": "Blah Blah for view tests"}
        cls.bulk_update_data = {"comments": "Blah Blah for api tests"}

        software_products = (
            SoftwareProduct(name=cls.p_name),
            SoftwareProduct(name=cls.p_name + "2"),
            SoftwareProduct(name=cls.p_name + "3"),
        )
        cls.software_product = SoftwareProduct.objects.bulk_create(software_products)[0]

        software_product_versions = (
            SoftwareProductVersion(name=cls.v_name, software_product=cls.software_product),
            SoftwareProductVersion(name=cls.v_name + "2", software_product=cls.software_product),
            SoftwareProductVersion(name=cls.v_name + "3", software_product=cls.software_product),
        )
        cls.software_product_version = SoftwareProductVersion.objects.bulk_create(software_product_versions)[0]

        software_product_installations = (
            SoftwareProductInstallation(
                virtualmachine=cls.vm, software_product=cls.software_product, version=cls.software_product_version
            ),
            SoftwareProductInstallation(
                device=cls.device, software_product=cls.software_product, version=cls.software_product_version
            ),
            SoftwareProductInstallation(
                cluster=cls.cluster, software_product=cls.software_product, version=cls.software_product_version
            ),
        )
        cls.software_product_installation = SoftwareProductInstallation.objects.bulk_create(
            software_product_installations
        )[0]

        software_licenses = (
            SoftwareLicense(
                name=cls.l_name,
                software_product=cls.software_product,
                version=cls.software_product_version,
                installation=cls.software_product_installation,
                stored_location_url=cls.test_url,
            ),
            SoftwareLicense(
                name=cls.l_name + "2",
                software_product=cls.software_product,
                version=cls.software_product_version,
            ),
            SoftwareLicense(
                name=cls.l_name + "3",
                software_product=cls.software_product,
                installation=cls.software_product_installation,
            ),
        )
        cls.software_license = SoftwareLicense.objects.bulk_create(software_licenses)[0]

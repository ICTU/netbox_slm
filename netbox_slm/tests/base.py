from django.test import TestCase

from dcim.models import Device, DeviceRole, DeviceType, Manufacturer, Site
from netbox_slm.models import SoftwareProduct, SoftwareProductVersion, SoftwareProductInstallation, SoftwareLicense
from virtualization.models import Cluster, ClusterType, VirtualMachine


class SlmBaseTestCase(TestCase):
    p_name: str = "test product"
    v_name: str = "test version"
    l_name: str = "test license"
    test_url: str = "https://github.com/ICTU/netbox_slm"
    vm: VirtualMachine
    software_product: SoftwareProduct
    software_product_version: SoftwareProductVersion
    software_product_installation: SoftwareProductInstallation

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        manufacturer = Manufacturer.objects.create(name="test manufacturer")
        device_type = DeviceType.objects.create(model="test device type", manufacturer=manufacturer)
        device_role = DeviceRole.objects.create(name="test device role")
        site = Site.objects.create(name="test site")
        cls.device = Device.objects.create(name="test device", device_type=device_type, role=device_role, site=site)
        cls.vm = VirtualMachine.objects.create(name="test VM")
        cluster_type = ClusterType.objects.create(name="test cluster type")
        cls.cluster = Cluster.objects.create(name="test cluster", type=cluster_type)

        cls.software_product = SoftwareProduct.objects.create(name=cls.p_name)
        cls.software_product_version = SoftwareProductVersion.objects.create(
            name=cls.v_name, software_product=cls.software_product
        )
        cls.software_product_installation = SoftwareProductInstallation.objects.create(
            virtualmachine=cls.vm, software_product=cls.software_product, version=cls.software_product_version
        )
        cls.software_license = SoftwareLicense.objects.create(
            name=cls.l_name,
            software_product=cls.software_product,
            version=cls.software_product_version,
            installation=cls.software_product_installation,
            stored_location_url=cls.test_url,
        )

    @classmethod
    def tearDownClass(cls):
        SoftwareLicense.objects.all().delete()
        SoftwareProductInstallation.objects.all().delete()
        SoftwareProductVersion.objects.all().delete()
        SoftwareProduct.objects.all().delete()
        Cluster.objects.all().delete()
        ClusterType.objects.all().delete()
        VirtualMachine.objects.all().delete()
        Device.objects.all().delete()
        Site.objects.all().delete()
        DeviceRole.objects.all().delete()
        DeviceType.objects.all().delete()
        Manufacturer.objects.all().delete()
        super().tearDownClass()

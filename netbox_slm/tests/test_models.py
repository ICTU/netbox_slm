from django.test import TestCase

from dcim.models import Device, DeviceRole, DeviceType, Manufacturer, Site
from virtualization.models import Cluster, ClusterType, VirtualMachine
from netbox_slm.models import SoftwareProduct, SoftwareProductVersion, SoftwareProductInstallation, SoftwareLicense


class ModelTestCase(TestCase):
    def setUp(self):
        self.p_name = "test product"
        self.v_name = "test version"
        self.l_name = "test license"

        manufacturer = Manufacturer.objects.create(name="test manufacturer")
        device_type = DeviceType.objects.create(model="test device type", manufacturer=manufacturer)
        device_role = DeviceRole.objects.create(name="test device role")
        site = Site.objects.create(name="test site")
        self.device = Device.objects.create(name="test device", device_type=device_type, role=device_role, site=site)
        self.vm = VirtualMachine.objects.create(name="test VM")
        cluster_type = ClusterType.objects.create(name="test cluster type")
        self.cluster = Cluster.objects.create(name="test cluster", type=cluster_type)
        self.test_url = "https://github.com/ICTU/netbox_slm"

        self.software_product = SoftwareProduct.objects.create(name=self.p_name)
        self.software_product_version = SoftwareProductVersion.objects.create(
            name=self.v_name, software_product=self.software_product
        )
        self.software_product_installation = SoftwareProductInstallation.objects.create(
            virtualmachine=self.vm, software_product=self.software_product, version=self.software_product_version
        )
        self.software_license = SoftwareLicense.objects.create(
            name=self.l_name,
            software_product=self.software_product,
            version=self.software_product_version,
            installation=self.software_product_installation,
            stored_location_url=self.test_url,
        )

    def test_model_name(self):
        self.assertEqual(self.p_name, str(self.software_product))
        self.assertEqual(self.v_name, str(self.software_product_version))
        self.assertTrue(str(self.software_product_installation)[0].isdigit())  # starts with PK
        self.assertEqual(self.l_name, str(self.software_license))

    def test_absolute_url(self):
        self.assertEqual("/plugins/slm/software-products/1/", self.software_product.get_absolute_url())
        self.assertEqual("/plugins/slm/versions/1/", self.software_product_version.get_absolute_url())
        self.assertEqual("/plugins/slm/installations/1/", self.software_product_installation.get_absolute_url())
        self.assertEqual("/plugins/slm/licenses/1/", self.software_license.get_absolute_url())

    def test_get_installation_count(self):
        installation_ss = '<a href="/plugins/slm/installations/?q={}">1</a>'
        self.assertEqual(installation_ss.format(self.p_name), self.software_product.get_installation_count())
        self.assertEqual(installation_ss.format(self.v_name), self.software_product_version.get_installation_count())

    def test_product_installation_methods(self):
        self.assertEqual("virtualmachine", self.software_product_installation.render_type())
        self.assertEqual(self.vm, self.software_product_installation.platform)

        self.software_product_installation.virtualmachine = None
        self.software_product_installation.device = self.device
        self.software_product_installation.save()
        self.assertEqual("device", self.software_product_installation.render_type())
        self.assertEqual(self.device, self.software_product_installation.platform)

        self.software_product_installation.device = None
        self.software_product_installation.cluster = self.cluster
        self.software_product_installation.save()
        self.assertEqual("cluster", self.software_product_installation.render_type())
        self.assertEqual(self.cluster, self.software_product_installation.platform)

    def test_software_license_stored_location_txt(self):
        self.assertEqual("Link", self.software_license.stored_location_txt)

        self.software_license.stored_location = "GitHub"
        self.software_license.save()
        self.assertEqual("GitHub", self.software_license.stored_location_txt)

from django.test import TestCase

from netbox_slm.models import SoftwareProduct, SoftwareProductVersion, SoftwareProductInstallation


class ModelTestCase(TestCase):
    def setUp(self):
        self.p_name = "test product"
        self.v_name = "test version"

        self.software_product = SoftwareProduct.objects.create(name=self.p_name)
        self.software_product_version = SoftwareProductVersion.objects.create(
            name=self.v_name, software_product=self.software_product
        )
        self.software_product_installation = SoftwareProductInstallation.objects.create(
            software_product=self.software_product, version=self.software_product_version
        )

    def test_model_name(self):
        self.assertEqual(self.p_name, str(self.software_product))
        self.assertEqual(self.v_name, str(self.software_product_version))
        self.assertTrue(str(self.software_product_installation).isnumeric())  # should be PK

    def test_absolute_url(self):
        self.assertEqual("/plugins/slm/software-products/1/", self.software_product.get_absolute_url())
        self.assertEqual("/plugins/slm/versions/1/", self.software_product_version.get_absolute_url())
        self.assertEqual("/plugins/slm/installations/1/", self.software_product_installation.get_absolute_url())

    def test_get_installation_count(self):
        installation_ss = '<a href="/plugins/slm/installations/?q={}">1</a>'
        self.assertEqual(installation_ss.format(self.p_name), self.software_product.get_installation_count())
        self.assertEqual(installation_ss.format(self.v_name), self.software_product_version.get_installation_count())

    def test_product_installation_methods(self):
        self.assertEqual("virtualmachine", self.software_product_installation.render_type())
        self.assertIsNone(self.software_product_installation.get_platform())

from .base import SlmBaseTestCase


class ModelTestCase(SlmBaseTestCase):
    """Test basic model functionality and custom overrides"""

    def test_model_name(self):
        self.assertEqual(self.p_name, str(self.software_product))
        self.assertEqual(self.v_name, str(self.software_product_version))
        self.assertTrue(str(self.software_product_installation)[0].isdigit())  # starts with PK
        self.assertEqual(self.l_name, str(self.software_license))

    def test_absolute_url(self):
        self.assertEqual(
            f"/plugins/slm/software-products/{self.software_product.pk}/", self.software_product.get_absolute_url()
        )
        self.assertEqual(
            f"/plugins/slm/versions/{self.software_product_version.pk}/",
            self.software_product_version.get_absolute_url(),
        )
        self.assertEqual(
            f"/plugins/slm/installations/{self.software_product_installation.pk}/",
            self.software_product_installation.get_absolute_url(),
        )
        self.assertEqual(f"/plugins/slm/licenses/{self.software_license.pk}/", self.software_license.get_absolute_url())

    def test_get_installation_count(self):
        self.assertEqual(
            f"<a href='/plugins/slm/installations/?software_product_id={self.software_product.pk}'>1</a>",
            self.software_product.get_installation_count(),
        )
        self.assertEqual(
            f"<a href='/plugins/slm/installations/?version_id={self.software_product_version.pk}'>1</a>",
            self.software_product_version.get_installation_count(),
        )

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

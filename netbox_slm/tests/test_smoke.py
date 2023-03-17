from django.test import TestCase

from netbox_slm.models import SoftwareProduct, SoftwareProductVersion, SoftwareProductInstallation


class ModelTestCase(TestCase):
    def test_smoke(self):
        software_product = SoftwareProduct.objects.create(name="test product")
        software_product_version = SoftwareProductVersion.objects.create(
            name="test version", software_product=software_product
        )
        software_product_installation = SoftwareProductInstallation.objects.create(
            software_product=software_product, version=software_product_version
        )

        self.assertEqual('virtualmachine', software_product_installation.render_type())

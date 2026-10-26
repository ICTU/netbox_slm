from unittest import skip

from netbox_slm.models import (
    SoftwareProduct,
    SoftwareProductVersion,
    SoftwareProductInstallation,
    SoftwareLicense,
)
from utilities.testing import ViewTestCases
from .base import SlmBaseTestCase


class SoftwareProductViewTestCase(
    SlmBaseTestCase,
    ViewTestCases.GetObjectViewTestCase,
    ViewTestCases.GetObjectChangelogViewTestCase,
    ViewTestCases.CreateObjectViewTestCase,
    ViewTestCases.EditObjectViewTestCase,
    ViewTestCases.DeleteObjectViewTestCase,
    ViewTestCases.ListObjectsViewTestCase,
):
    model = SoftwareProduct

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.form_data = {
            "name": "Test name - SoftwareProduct",
        }

    def _get_base_url(self):
        return "plugins:netbox_slm:softwareproduct_{}"

    @skip("Not yet working")
    def test_create_object_with_permission(self): ...

    @skip("Not yet working")
    def test_create_object_with_constrained_permission(self): ...

    @skip("Not yet working")
    def test_edit_object_with_permission(self): ...

    @skip("Not yet working")
    def test_edit_object_with_constrained_permission(self): ...

    @skip("Not yet working")
    def test_delete_object_with_permission(self): ...

    @skip("Not yet working")
    def test_delete_object_with_constrained_permission(self): ...


class SoftwareProductVersionViewTestCase(
    SlmBaseTestCase,
    ViewTestCases.GetObjectViewTestCase,
    ViewTestCases.GetObjectChangelogViewTestCase,
    ViewTestCases.CreateObjectViewTestCase,
    ViewTestCases.EditObjectViewTestCase,
    ViewTestCases.DeleteObjectViewTestCase,
    ViewTestCases.ListObjectsViewTestCase,
):
    model = SoftwareProductVersion

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.form_data = {
            "name": "Test name - SoftwareProductVersion",
            "software_product": cls.software_product.pk,
        }

    def _get_base_url(self):
        return "plugins:netbox_slm:softwareproductversion_{}"

    @skip("Not yet working")
    def test_create_object_with_permission(self): ...

    @skip("Not yet working")
    def test_create_object_with_constrained_permission(self): ...

    @skip("Not yet working")
    def test_edit_object_with_permission(self): ...

    @skip("Not yet working")
    def test_edit_object_with_constrained_permission(self): ...

    @skip("Not yet working")
    def test_delete_object_with_permission(self): ...

    @skip("Not yet working")
    def test_delete_object_with_constrained_permission(self): ...


class SoftwareProductInstallationViewTestCase(
    SlmBaseTestCase,
    ViewTestCases.GetObjectViewTestCase,
    ViewTestCases.GetObjectChangelogViewTestCase,
    ViewTestCases.CreateObjectViewTestCase,
    ViewTestCases.EditObjectViewTestCase,
    ViewTestCases.DeleteObjectViewTestCase,
    ViewTestCases.ListObjectsViewTestCase,
):
    model = SoftwareProductInstallation

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.form_data = {
            "device": cls.device.pk,
            "software_product": cls.software_product.pk,
            "version": cls.software_product_version.pk,
        }

    def _get_base_url(self):
        return "plugins:netbox_slm:softwareproductinstallation_{}"


class SoftwareLicenseViewTestCase(
    SlmBaseTestCase,
    ViewTestCases.GetObjectViewTestCase,
    ViewTestCases.GetObjectChangelogViewTestCase,
    ViewTestCases.CreateObjectViewTestCase,
    ViewTestCases.EditObjectViewTestCase,
    ViewTestCases.DeleteObjectViewTestCase,
    ViewTestCases.ListObjectsViewTestCase,
):
    model = SoftwareLicense

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.form_data = {
            "name": "Test name - SoftwareLicense",
            "type": "Test type - SoftwareLicense",
            "software_product": cls.software_product.pk,
        }

    def _get_base_url(self):
        return "plugins:netbox_slm:softwarelicense_{}"

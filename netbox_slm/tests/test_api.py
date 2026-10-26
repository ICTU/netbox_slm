from netbox_slm.models import (
    SoftwareProduct,
    SoftwareProductVersion,
    SoftwareProductInstallation,
    SoftwareLicense,
)

from utilities.testing.api import APIViewTestCases

from .base import SlmBaseTestCase


class SoftwareProductViewSetTestCase(
    APIViewTestCases.GetObjectViewTestCase,
    APIViewTestCases.ListObjectsViewTestCase,
    APIViewTestCases.CreateObjectViewTestCase,
    APIViewTestCases.UpdateObjectViewTestCase,
    # APIViewTestCases.DeleteObjectViewTestCase,
    SlmBaseTestCase,
):
    model = SoftwareProduct
    view_namespace = "plugins-api:netbox_slm"
    brief_fields = ["description", "display", "id", "name", "url"]

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.create_data = [{
            "name": "Test name - SoftwareProduct",
        }]


class SoftwareProductVersionViewSetTestCase(
    APIViewTestCases.GetObjectViewTestCase,
    APIViewTestCases.ListObjectsViewTestCase,
    APIViewTestCases.CreateObjectViewTestCase,
    APIViewTestCases.UpdateObjectViewTestCase,
    # APIViewTestCases.DeleteObjectViewTestCase,
    SlmBaseTestCase,
):
    model = SoftwareProductVersion
    view_namespace = "plugins-api:netbox_slm"
    brief_fields = ["description", "display", "id", "name", "url"]

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.create_data = [{
            "name": "Test name - SoftwareProductVersion",
            "software_product": cls.software_product.pk,
        }]


class SoftwareProductInstallationViewSetTestCase(
    APIViewTestCases.GetObjectViewTestCase,
    APIViewTestCases.ListObjectsViewTestCase,
    APIViewTestCases.CreateObjectViewTestCase,
    # APIViewTestCases.UpdateObjectViewTestCase,
    APIViewTestCases.DeleteObjectViewTestCase,
    SlmBaseTestCase,
):
    model = SoftwareProductInstallation
    view_namespace = "plugins-api:netbox_slm"
    brief_fields = ["display", "id", "url"]

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.create_data = [{
            "device": cls.device.pk,
            "software_product": cls.software_product.pk,
            "version": cls.software_product_version.pk,
        }]
        # cls.bulk_update_data["cluster"] = cls.cluster.pk


class SoftwareLicenseViewSetTestCase(
    APIViewTestCases.GetObjectViewTestCase,
    APIViewTestCases.ListObjectsViewTestCase,
    APIViewTestCases.CreateObjectViewTestCase,
    APIViewTestCases.UpdateObjectViewTestCase,
    APIViewTestCases.DeleteObjectViewTestCase,
    SlmBaseTestCase,
):
    model = SoftwareLicense
    view_namespace = "plugins-api:netbox_slm"
    brief_fields = ["description", "display", "id", "name", "url"]

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.create_data = [{
            "name": "Test name - SoftwareLicense",
            "type": "Test type - SoftwareLicense",
            "software_product": cls.software_product.pk,
        }]
        cls.bulk_update_data["type"] = "Test2"

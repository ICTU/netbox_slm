from netbox_slm.tables import (
    SoftwareProductTable,
    SoftwareProductVersionTable,
    SoftwareProductInstallationTable,
    SoftwareLicenseTable,
)

from utilities.testing.tables import TableTestCases

from .base import SlmBaseTestCase


class SoftwareProductTableTestCase(TableTestCases.StandardTableTestCase, SlmBaseTestCase):
    table = SoftwareProductTable


class SoftwareProductVersionTableTestCase(TableTestCases.StandardTableTestCase, SlmBaseTestCase):
    table = SoftwareProductVersionTable


class SoftwareProductInstallationTableTestCase(TableTestCases.StandardTableTestCase, SlmBaseTestCase):
    table = SoftwareProductInstallationTable


class SoftwareLicenseTableTestCase(TableTestCases.StandardTableTestCase, SlmBaseTestCase):
    table = SoftwareLicenseTable

    def test_render_installation(self):
        for _, queryset in self.get_queryset_sources():
            table = self.get_table(queryset)
            self.assertEqual(str(self.vm), table.render_installation(record=self.software_license))

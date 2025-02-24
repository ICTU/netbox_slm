from unittest.mock import patch

from django.contrib.auth import get_user_model

from .base import SlmBaseTestCase


class FunctionalTestCase(SlmBaseTestCase):
    """Functional test cases that require a client and user with permissions"""

    def setUp(self):
        test_user, _ = get_user_model().objects.get_or_create(username="test", is_superuser=True)
        self.client.force_login(test_user)

    @classmethod
    def tearDownClass(cls):
        get_user_model().objects.all().delete()
        super().tearDownClass()

    def test_template_content(self):
        cluster_response = self.client.get(f"/virtualization/clusters/{self.cluster.pk}/")
        self.assertContains(cluster_response, f'<a href="/plugins/slm/installations/add/?cluster={self.cluster.pk}"')
        self.assertContains(cluster_response, "</span> Add an installation")

        device_response = self.client.get(f"/dcim/devices/{self.device.pk}/")
        self.assertContains(device_response, f'<a href="/plugins/slm/installations/add/?device={self.device.pk}"')
        self.assertContains(device_response, "</span> Add an installation")

        vm_response = self.client.get(f"/virtualization/virtual-machines/{self.vm.pk}/")
        self.assertTemplateUsed(vm_response, "netbox_slm/installations_card_include.html")
        self.assertContains(vm_response, f'<a href="/plugins/slm/installations/add/?virtualmachine={self.vm.pk}"')

    def test_setting_skip_content(self):
        # self.settings(PLUGINS_CONFIG=dict(netbox_slm=dict(link_virtualmachine_installations=None)))
        with patch.dict("netbox_slm.template_content.installations", {"virtualmachine": None}):
            vm_response = self.client.get(f"/virtualization/virtual-machines/{self.vm.pk}/")
        self.assertTemplateNotUsed(vm_response, "netbox_slm/installations_card_include.html")

    def test_setting_left_content(self):
        # self.settings(PLUGINS_CONFIG=dict(netbox_slm=dict(link_device_installations="left")))
        with patch.dict("netbox_slm.template_content.installations", {"device": "left"}):
            device_response = self.client.get(f"/dcim/devices/{self.device.pk}/")
        self.assertContains(device_response, f'<a href="/plugins/slm/installations/add/?device={self.device.pk}"')
        self.assertContains(device_response, "</span> Add an installation")

    def test_setting_full_content(self):
        # self.settings(PLUGINS_CONFIG=dict(netbox_slm=dict(link_cluster_installations="full")))
        with patch.dict("netbox_slm.template_content.installations", {"cluster": "full"}):
            cluster_response = self.client.get(f"/virtualization/clusters/{self.cluster.pk}/")
        self.assertContains(cluster_response, f'<a href="/plugins/slm/installations/add/?cluster={self.cluster.pk}"')
        self.assertContains(cluster_response, "</span> Add an installation")

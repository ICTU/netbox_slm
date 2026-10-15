"""
fill the database with develop/test values
"""

import django

from datetime import date
from hashlib import md5
from itertools import chain

django.setup()  # before app imports

from netbox.choices import ColorChoices
from dcim.models import Device, DeviceRole, DeviceType, Manufacturer, Site
from virtualization.models import Cluster, ClusterGroup, ClusterType, VirtualMachine

from netbox_slm.models import (
    SoftwareProduct,
    SoftwareProductInstallation,
    SoftwareProductVersion,
    SoftwareLicense,
    SoftwareReleaseTypes,
)


# NetBox objects
site = Site.objects.create(name="Main", slug="main")
manufacturer_cisco = Manufacturer.objects.create(name="Cisco", description="Cisco Systems, Inc.", slug="cisco")
manufacturer_dell = Manufacturer.objects.create(name="Dell", description="Dell Inc.", slug="dell")
manufacturer_docker = Manufacturer.objects.create(name="Docker", description="Docker, Inc.", slug="docker")
manufacturer_elastic = Manufacturer.objects.create(name="Elastic", description="Elastic", slug="elastic")
manufacturer_ictu = Manufacturer.objects.create(name="ICTU", description="Stichting ICTU", slug="ictu")
manufacturer_microsoft = Manufacturer.objects.create(
    name="Microsoft", description="Microsoft Corporation", slug="microsoft"
)
manufacturer_netbox = Manufacturer.objects.create(name="NetBox", description="NetBox Labs", slug="netbox")
manufacturer_redhat = Manufacturer.objects.create(name="Red Hat", description="Red Hat, LLC", slug="redhat")
manufacturer_sonar = Manufacturer.objects.create(name="Sonar", description="Sonar", slug="sonar")
manufacturer_vmware = Manufacturer.objects.create(name="VMware", description="VMware LLC", slug="vmware")

cluster_group_blue = ClusterGroup.objects.create(name="Blue", slug="blue")
cluster_group_green = ClusterGroup.objects.create(name="Green", slug="green")
cluster_type_hypervisor = ClusterType.objects.create(name="Hypervisor", slug="compute")
cluster_type_search = ClusterType.objects.create(name="Search", slug="search")
cluster_c1 = Cluster.objects.create(name="c1", type=cluster_type_hypervisor, group=cluster_group_blue)
cluster_c2 = Cluster.objects.create(name="c2", type=cluster_type_hypervisor, group=cluster_group_green)
cluster_es1 = Cluster.objects.create(name="es1", type=cluster_type_search, group=cluster_group_blue)
cluster_es2 = Cluster.objects.create(name="es2", type=cluster_type_search, group=cluster_group_green)

device_role_red = DeviceRole.objects.create(name="Red", color=ColorChoices.COLOR_RED, slug="red")
device_role_green = DeviceRole.objects.create(name="Green", color=ColorChoices.COLOR_GREEN, slug="green")
device_role_blue = DeviceRole.objects.create(name="Blue", color=ColorChoices.COLOR_BLUE, slug="blue")
device_role_dark = DeviceRole.objects.create(name="Dark", color=ColorChoices.COLOR_DARK_GREY, slug="dark")
device_type_router = DeviceType.objects.create(
    manufacturer=manufacturer_cisco, model="Layer 3", u_height=1.0, slug="router"
)
device_type_switch = DeviceType.objects.create(
    manufacturer=manufacturer_cisco, model="Layer 2", u_height=1.0, slug="switch"
)
device_type_dell_1u = DeviceType.objects.create(manufacturer=manufacturer_dell, model="1U", u_height=1.0, slug="dell1u")
device_type_dell_2u = DeviceType.objects.create(manufacturer=manufacturer_dell, model="2U", u_height=2.0, slug="dell2u")
device_type_dell_4u = DeviceType.objects.create(manufacturer=manufacturer_dell, model="4U", u_height=4.0, slug="dell4u")

device_router01 = Device.objects.create(
    name="router01", role=device_role_red, device_type=device_type_router, site=site
)
device_switch01 = Device.objects.create(
    name="switch01", role=device_role_green, device_type=device_type_switch, site=site
)
device_switch02 = Device.objects.create(
    name="switch02", role=device_role_blue, device_type=device_type_switch, site=site
)
device_switch10 = Device.objects.create(
    name="switch10", role=device_role_dark, device_type=device_type_switch, site=site
)

server_numbers = set(chain(range(10, 13), range(20, 23)))
device_server01 = Device.objects.create(
    name="server01", role=device_role_red, device_type=device_type_dell_2u, site=site
)
device_server02 = Device.objects.create(
    name="server02", role=device_role_dark, device_type=device_type_dell_1u, site=site
)
device_server10 = Device.objects.create(
    name="server10", role=device_role_green, device_type=device_type_dell_1u, site=site, cluster=cluster_c2
)
Device.objects.create(
    name="server11", role=device_role_green, device_type=device_type_dell_4u, site=site, cluster=cluster_c2
)
Device.objects.create(
    name="server12", role=device_role_green, device_type=device_type_dell_4u, site=site, cluster=cluster_c2
)
device_server20 = Device.objects.create(
    name="server20", role=device_role_blue, device_type=device_type_dell_1u, site=site, cluster=cluster_c1
)
Device.objects.create(
    name="server21", role=device_role_blue, device_type=device_type_dell_4u, site=site, cluster=cluster_c1
)
Device.objects.create(
    name="server22", role=device_role_blue, device_type=device_type_dell_4u, site=site, cluster=cluster_c1
)

vm_numbers = set(chain(range(11, 15), range(21, 25)))
for vm_num in vm_numbers:
    VirtualMachine.objects.create(name=f"vm{vm_num}", site=site, cluster=cluster_es1 if vm_num < 20 else cluster_es2)

# SLM products
software_product_bios = SoftwareProduct.objects.create(name="BIOS", manufacturer=manufacturer_dell)
software_product_docker = SoftwareProduct.objects.create(name="Docker Engine", manufacturer=manufacturer_docker)
software_product_elasticsearch = SoftwareProduct.objects.create(name="Elasticsearch", manufacturer=manufacturer_elastic)
software_product_esxi = SoftwareProduct.objects.create(name="ESXi", manufacturer=manufacturer_vmware)
software_product_idrac = SoftwareProduct.objects.create(name="iDRAC Firmware", manufacturer=manufacturer_dell)
software_product_ios = SoftwareProduct.objects.create(name="IOS", manufacturer=manufacturer_cisco)
software_product_ios_xe = SoftwareProduct.objects.create(name="IOS XE", manufacturer=manufacturer_cisco)
software_product_netbox = SoftwareProduct.objects.create(name="NetBox", manufacturer=manufacturer_netbox)
software_product_quality_time = SoftwareProduct.objects.create(name="Quality-time", manufacturer=manufacturer_ictu)
software_product_rhel = SoftwareProduct.objects.create(
    name="Red Hat Enterprise Linux", manufacturer=manufacturer_redhat
)
software_product_sonarqube = SoftwareProduct.objects.create(name="SonarQube", manufacturer=manufacturer_sonar)
SoftwareProduct.objects.create(name="Update-time", manufacturer=manufacturer_ictu)
software_product_vcenter = SoftwareProduct.objects.create(name="vCenter Server", manufacturer=manufacturer_vmware)
software_product_windows_server = SoftwareProduct.objects.create(
    name="Windows Server", manufacturer=manufacturer_microsoft
)

# SLM product versions
bios_v2_27_0 = SoftwareProductVersion.objects.create(
    name="2.27.0",
    software_product=software_product_bios,
    release_type=SoftwareReleaseTypes.STABLE,
    release_date=date(day=27, month=4, year=2026),
    filename="bios_v2_27_0.efi",
    file_checksum=md5(b"TestString1").hexdigest(),
)
SoftwareProductVersion.objects.create(
    name="1.9.16",
    software_product=software_product_bios,
    release_type=SoftwareReleaseTypes.STABLE,
    release_date=date(day=22, month=10, year=2025),
    filename="bios_v1_9_16.efi",
    file_checksum=md5(b"TestString2").hexdigest(),
)
SoftwareProductVersion.objects.create(
    name="1.8.16",
    software_product=software_product_bios,
    release_type=SoftwareReleaseTypes.STABLE,
    release_date=date(day=17, month=3, year=2026),
    filename="bios_v1_8_16.efi",
    file_checksum=md5(b"TestString42").hexdigest(),
)

ios_xe_v26_2_1 = SoftwareProductVersion.objects.create(
    name="26.2.1",
    software_product=software_product_ios_xe,
    release_type=SoftwareReleaseTypes.STABLE,
    release_date=date(day=31, month=8, year=2026),
)
ios_v15_9 = SoftwareProductVersion.objects.create(
    name="15.9M&T",
    software_product=software_product_ios,
    release_type=SoftwareReleaseTypes.STABLE,
    release_date=date(day=31, month=7, year=2019),
    end_of_support=date(day=31, month=7, year=2031),
)

docker_v29_9_1 = SoftwareProductVersion.objects.create(
    name="29.9.1",
    software_product=software_product_docker,
    release_type=SoftwareReleaseTypes.STABLE,
    release_date=date(day=14, month=10, year=2026),
)
SoftwareProductVersion.objects.create(
    name="29.9.0",
    software_product=software_product_docker,
    release_type=SoftwareReleaseTypes.STABLE,
    release_date=date(day=8, month=10, year=2026),
)
SoftwareProductVersion.objects.create(
    name="29.8.2",
    software_product=software_product_docker,
    release_type=SoftwareReleaseTypes.STABLE,
    release_date=date(day=30, month=9, year=2026),
)

elasticsearch_v9_5_5 = SoftwareProductVersion.objects.create(
    name="9.5.5",
    software_product=software_product_elasticsearch,
    release_type=SoftwareReleaseTypes.STABLE,
    release_date=date(day=6, month=10, year=2026),
)

esxi_v9_1_1_0 = SoftwareProductVersion.objects.create(
    name="9.1.1.0",
    software_product=software_product_esxi,
    release_type=SoftwareReleaseTypes.STABLE,
    release_date=date(day=3, month=9, year=2026),
)
esxi_v9x = SoftwareProductVersion.objects.create(
    name="v9.x",
    software_product=software_product_esxi,
)
esxi_v8x = SoftwareProductVersion.objects.create(
    name="v8.x",
    software_product=software_product_esxi,
)

idrac_v7_30_30_51 = SoftwareProductVersion.objects.create(
    name="7.30.30.51",
    software_product=software_product_idrac,
    release_type=SoftwareReleaseTypes.STABLE,
    release_date=date(day=15, month=6, year=2026),
    documentation_url="https://www.dell.com/support/home/en-us/drivers/driversdetails?driverid=cpchx",
)
SoftwareProductVersion.objects.create(
    name="7.30.10.50",
    software_product=software_product_idrac,
    release_type=SoftwareReleaseTypes.STABLE,
    release_date=date(day=16, month=3, year=2026),
    documentation_url="https://www.dell.com/support/home/en-us/drivers/driversdetails?driverid=924yt",
)
SoftwareProductVersion.objects.create(
    name="7.20.80.50",
    software_product=software_product_idrac,
    release_type=SoftwareReleaseTypes.STABLE,
    release_date=date(day=16, month=12, year=2025),
    documentation_url="https://www.dell.com/support/home/en-us/drivers/driversdetails?driverid=kywdc",
)
SoftwareProductVersion.objects.create(
    name="7.00.00.183",
    software_product=software_product_idrac,
    release_type=SoftwareReleaseTypes.STABLE,
    release_date=date(day=17, month=10, year=2025),
    documentation_url="https://www.dell.com/support/home/en-us/drivers/driversdetails?driverid=vp556",
)

netbox_v4_6_3 = SoftwareProductVersion.objects.create(
    name="4.6.3",
    software_product=software_product_netbox,
    release_type=SoftwareReleaseTypes.STABLE,
    release_date=date(day=16, month=6, year=2026),
)

quality_time_v5_60_1 = SoftwareProductVersion.objects.create(
    name="5.60.1",
    software_product=software_product_quality_time,
    release_type=SoftwareReleaseTypes.STABLE,
    release_date=date(day=9, month=10, year=2026),
    documentation_url="https://quality-time.readthedocs.io/en/v5.60.1/",
)
SoftwareProductVersion.objects.create(
    name="5.60.1-rc.0",
    software_product=software_product_quality_time,
    release_type=SoftwareReleaseTypes.RELEASE_CANDIDATE,
    release_date=date(day=9, month=10, year=2026),
    documentation_url="https://quality-time.readthedocs.io/en/v5.60.1-rc.0/",
)

rhel_9_8 = SoftwareProductVersion.objects.create(
    name="9.8",
    software_product=software_product_rhel,
    release_type=SoftwareReleaseTypes.STABLE,
    release_date=date(day=19, month=5, year=2026),
    documentation_url="https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/9.8_release_notes/index",
)
SoftwareProductVersion.objects.create(
    name="8.10",
    software_product=software_product_rhel,
    release_type=SoftwareReleaseTypes.STABLE,
    release_date=date(day=22, month=5, year=2024),
    end_of_support=date(day=31, month=5, year=2029),
    documentation_url="https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/8.10_release_notes/index",
)

sonarqube_v2026_4_1 = SoftwareProductVersion.objects.create(
    name="2026.4.1",
    software_product=software_product_sonarqube,
    release_type=SoftwareReleaseTypes.STABLE,
    release_date=date(day=7, month=8, year=2026),
    documentation_url="https://github.com/ICTU/sonar/releases/tag/2026.4.1",
)

vcenter_v9_0_2 = SoftwareProductVersion.objects.create(
    name="9.0.2",
    software_product=software_product_vcenter,
    release_type=SoftwareReleaseTypes.STABLE,
    release_date=date(day=20, month=1, year=2026),
    description="vCenter Server 9.0.2.0.25148086",
    documentation_url="https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0.html",
)
vcenter_v9_0_1 = SoftwareProductVersion.objects.create(
    name="9.0.1",
    software_product=software_product_vcenter,
    release_type=SoftwareReleaseTypes.STABLE,
    release_date=date(day=29, month=9, year=2025),
    description="vCenter Server 9.0.1.0.24957454",
    documentation_url="https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0.html",
)
SoftwareProductVersion.objects.create(
    name="9.0",
    software_product=software_product_vcenter,
    release_type=SoftwareReleaseTypes.STABLE,
    release_date=date(day=17, month=6, year=2025),
    description="vCenter Server 9.0.0.10000",
    documentation_url="https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-0.html",
)
SoftwareProductVersion.objects.create(
    name="8.0",
    software_product=software_product_vcenter,
    release_type=SoftwareReleaseTypes.STABLE,
    release_date=date(day=11, month=10, year=2022),
    description="vCenter Server 8.0.0.10000",
    documentation_url="https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0.html",
)

windows_server_2025 = SoftwareProductVersion.objects.create(
    name="2025",
    software_product=software_product_windows_server,
    release_type=SoftwareReleaseTypes.STABLE,
    release_date=date(day=1, month=11, year=2024),
    end_of_support=date(day=13, month=11, year=2029),
    description="Windows Server 2025 (Base Build 26100.1742)",
    documentation_url="https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0.html",
)

# SLM product installations
installation_esxi = {}
for server_num in server_numbers:
    device_obj = Device.objects.get(name=f"server{server_num}")
    SoftwareProductInstallation.objects.create(
        device=device_obj,
        software_product=software_product_bios,
        version=bios_v2_27_0,
    )
    installation_esxi[server_num] = SoftwareProductInstallation.objects.create(
        device=device_obj,
        software_product=software_product_esxi,
        version=esxi_v9_1_1_0,
    )
SoftwareProductInstallation.objects.create(
    device=device_router01, software_product=software_product_ios_xe, version=ios_xe_v26_2_1
)
SoftwareProductInstallation.objects.create(
    device=device_switch01, software_product=software_product_ios, version=ios_xe_v26_2_1
)
SoftwareProductInstallation.objects.create(
    device=device_switch02, software_product=software_product_ios, version=ios_xe_v26_2_1
)
SoftwareProductInstallation.objects.create(
    device=device_switch10, software_product=software_product_ios, version=ios_v15_9
)
server01_docker = SoftwareProductInstallation.objects.create(
    device=device_server01, software_product=software_product_docker, version=docker_v29_9_1
)
server01_idrac = SoftwareProductInstallation.objects.create(
    device=device_server01, software_product=software_product_idrac, version=idrac_v7_30_30_51
)
SoftwareProductInstallation.objects.create(
    device=device_server01, software_product=software_product_netbox, version=netbox_v4_6_3
)
SoftwareProductInstallation.objects.create(
    device=device_server01, software_product=software_product_quality_time, version=quality_time_v5_60_1
)
SoftwareProductInstallation.objects.create(
    device=device_server01, software_product=software_product_rhel, version=rhel_9_8
)
server01_sonar = SoftwareProductInstallation.objects.create(
    device=device_server01, software_product=software_product_sonarqube, version=sonarqube_v2026_4_1
)
SoftwareProductInstallation.objects.create(
    device=device_server02, software_product=software_product_windows_server, version=windows_server_2025
)
server10_vcenter = SoftwareProductInstallation.objects.create(
    device=device_server10, software_product=software_product_vcenter, version=vcenter_v9_0_2
)
server20_vcenter = SoftwareProductInstallation.objects.create(
    device=device_server20, software_product=software_product_vcenter, version=vcenter_v9_0_1
)

for vm_num in vm_numbers:
    vm_obj = VirtualMachine.objects.get(name=f"vm{vm_num}")
    SoftwareProductInstallation.objects.create(
        virtualmachine=vm_obj, software_product=software_product_rhel, version=rhel_9_8
    )
    SoftwareProductInstallation.objects.create(
        virtualmachine=vm_obj, software_product=software_product_elasticsearch, version=elasticsearch_v9_5_5
    )

installation_es1 = SoftwareProductInstallation.objects.create(
    cluster=cluster_es1, software_product=software_product_elasticsearch, version=elasticsearch_v9_5_5
)
installation_es2 = SoftwareProductInstallation.objects.create(
    cluster=cluster_es2, software_product=software_product_elasticsearch, version=elasticsearch_v9_5_5
)

# SLM licenses
SoftwareLicense.objects.create(
    name="Docker Engine",
    software_product=software_product_docker,
    type="Free",
    support=False,
    installation=server01_docker,
    spdx_expression="Apache-2.0",
)

SoftwareLicense.objects.create(
    name="ES1 - Basic",
    software_product=software_product_elasticsearch,
    type="Resource based",
    start_date=date(day=1, month=1, year=2025),
    support=False,
    installation=installation_es1,
    spdx_expression="Elastic-2.0",
)
SoftwareLicense.objects.create(
    name="ES2 - Basic",
    software_product=software_product_elasticsearch,
    type="Resource based",
    start_date=date(day=1, month=1, year=2025),
    support=False,
    installation=installation_es2,
    spdx_expression="Elastic-2.0",
)

SoftwareLicense.objects.create(
    name="server42 - 32 Cores",
    software_product=software_product_esxi,
    type="Resource based",
    start_date=date(day=28, month=10, year=2021),
    expiration_date=date(day=28, month=10, year=2025),
    support=True,
    version=esxi_v8x,
    stored_location="Vault",
)
SoftwareLicense.objects.create(
    name="server10 - 16 Cores",
    software_product=software_product_esxi,
    type="Resource based",
    start_date=date(day=9, month=7, year=2025),
    support=True,
    installation=installation_esxi[10],
    version=esxi_v9x,
    stored_location="Vault",
)
SoftwareLicense.objects.create(
    name="server11 - 64 Cores",
    software_product=software_product_esxi,
    type="Resource based",
    start_date=date(day=9, month=7, year=2025),
    support=True,
    installation=installation_esxi[11],
    version=esxi_v9x,
    stored_location="Vault",
)
SoftwareLicense.objects.create(
    name="server12 - 64 Cores",
    software_product=software_product_esxi,
    type="Resource based",
    start_date=date(day=9, month=7, year=2025),
    support=True,
    installation=installation_esxi[12],
    version=esxi_v9x,
    stored_location="Vault",
)
SoftwareLicense.objects.create(
    name="server20 - 16 Cores",
    software_product=software_product_esxi,
    type="Resource based",
    start_date=date(day=9, month=7, year=2025),
    support=True,
    installation=installation_esxi[20],
    version=esxi_v9x,
    stored_location="Vault",
)
SoftwareLicense.objects.create(
    name="server21 - 64 Cores",
    software_product=software_product_esxi,
    type="Resource based",
    start_date=date(day=9, month=7, year=2025),
    support=True,
    installation=installation_esxi[21],
    version=esxi_v9x,
    stored_location="Vault",
)
SoftwareLicense.objects.create(
    name="server22 - 64 Cores",
    software_product=software_product_esxi,
    type="Resource based",
    start_date=date(day=9, month=7, year=2025),
    support=True,
    installation=installation_esxi[22],
    version=esxi_v9x,
    stored_location="Vault",
)

SoftwareLicense.objects.create(
    name="Basic iDRAC",
    software_product=software_product_idrac,
    type="Features",
    start_date=date(day=7, month=10, year=2025),
    support=False,
    stored_location="Dell Digital Locker",
    stored_location_url="https://www.dell.com/myaccount/en-us",
)
SoftwareLicense.objects.create(
    name="Express iDRAC",
    software_product=software_product_idrac,
    type="Features",
    start_date=date(day=19, month=4, year=2025),
    support=True,
    stored_location="Dell Digital Locker",
    stored_location_url="https://www.dell.com/myaccount/en-us",
)
SoftwareLicense.objects.create(
    name="Enterprise iDRAC",
    software_product=software_product_idrac,
    type="Features",
    start_date=date(day=21, month=7, year=2026),
    support=True,
    installation=server01_idrac,
    stored_location="Dell Digital Locker",
    stored_location_url="https://www.dell.com/myaccount/en-us",
)

SoftwareLicense.objects.create(
    name="Red Hat Enterprise Linux Server",
    software_product=software_product_rhel,
    type="Server instance",
    support=True,
    license_amount=3,
    stored_location="Red Hat Customer Portal",
    stored_location_url="https://access.redhat.com/",
)
SoftwareLicense.objects.create(
    name="Red Hat Enterprise Linux for Virtual Datacenters",
    software_product=software_product_rhel,
    type="Cluster-wide",
    support=True,
    stored_location="Red Hat Hybrid Cloud Console",
    stored_location_url="https://console.redhat.com/",
)

SoftwareLicense.objects.create(
    name="server01 - 100k LoC",
    software_product=software_product_sonarqube,
    type="Size based",
    start_date=date(day=4, month=12, year=2024),
    support=True,
    installation=server01_sonar,
    stored_location="Vault",
)

SoftwareLicense.objects.create(
    name="vCenter Server for Essentials",
    software_product=software_product_vcenter,
    type="Server instance",
    support=True,
    start_date=date(day=7, month=10, year=2024),
    expiration_date=date(day=7, month=10, year=2025),
)
SoftwareLicense.objects.create(
    name="vCenter Server Foundation",
    software_product=software_product_vcenter,
    type="Server instance",
    support=True,
    installation=server10_vcenter,
)
SoftwareLicense.objects.create(
    name="vCenter Server Standard",
    software_product=software_product_vcenter,
    type="Server instance",
    support=True,
    installation=server20_vcenter,
)

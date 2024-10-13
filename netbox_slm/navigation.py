from django.conf import settings

from netbox.plugins import PluginMenuButton, PluginMenuItem, PluginMenu
from . import SLMConfig

slm_items = (
    PluginMenuItem(
        link="plugins:netbox_slm:softwareproduct_list",
        link_text="Software Products",
        permissions=["netbox_slm.add_softwareproduct"],
        buttons=(
            PluginMenuButton(
                "plugins:netbox_slm:softwareproduct_add",
                "Add",
                "mdi mdi-plus-thick",
                permissions=["netbox_slm.add_softwareproduct"],
            ),
        ),
    ),
    PluginMenuItem(
        link="plugins:netbox_slm:softwareproductversion_list",
        link_text="Versions",
        permissions=["netbox_slm.add_softwareproductversion"],
        buttons=(
            PluginMenuButton(
                "plugins:netbox_slm:softwareproductversion_add",
                "Add",
                "mdi mdi-plus-thick",
                permissions=["netbox_slm.add_softwareproductversion"],
            ),
        ),
    ),
    PluginMenuItem(
        link="plugins:netbox_slm:softwareproductinstallation_list",
        link_text="Installations",
        permissions=["netbox_slm.add_softwareproductinstallation"],
        buttons=(
            PluginMenuButton(
                "plugins:netbox_slm:softwareproductinstallation_add",
                "Add",
                "mdi mdi-plus-thick",
                permissions=["netbox_slm.add_softwareproductinstallation"],
            ),
        ),
    ),
    PluginMenuItem(
        link="plugins:netbox_slm:softwarelicense_list",
        link_text="Licenses",
        permissions=["netbox_slm.add_softwarelicense"],
        buttons=(
            PluginMenuButton(
                "plugins:netbox_slm:softwarelicense_add",
                "Add",
                "mdi mdi-plus-thick",
                permissions=["netbox_slm.add_softwarelicense"],
            ),
        ),
    ),
)

if settings.PLUGINS_CONFIG["netbox_slm"].get("top_level_menu") is True:
    menu = PluginMenu(
        label="Software Lifecycle",
        groups=((SLMConfig.verbose_name, slm_items),),
        icon_class="mdi mdi-content-save",
    )
else:
    menu_items = slm_items

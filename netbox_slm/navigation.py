from netbox.plugins import PluginMenuButton, PluginMenuItem, PluginMenu
from django.conf import settings

plugin_settings = settings.PLUGINS_CONFIG["netbox_slm"]

items = (
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
            PluginMenuButton(
                "plugins:netbox_slm:softwareproduct_import",
                "Import",
                "mdi mdi-upload",
                permissions=["netbox_slm.import_softwareproduct"],
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
            PluginMenuButton(
                "plugins:netbox_slm:softwareproductversion_import",
                "Import",
                "mdi mdi-upload",
                permissions=["netbox_slm.import_softwareproductversion"],
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
            PluginMenuButton(
                "plugins:netbox_slm:softwareproductinstallation_import",
                "Import",
                "mdi mdi-upload",
                permissions=["netbox_slm.import_softwareproductinstallation"],
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
            PluginMenuButton(
                "plugins:netbox_slm:softwarelicense_import",
                "Import",
                "mdi mdi-upload",
                permissions=["netbox_slm.import_softwarelicense"],
            ),
        ),
    ),
)



if plugin_settings.get("top_level_menu"):
    menu = PluginMenu(
       label="Software",
       groups=(("SOFTWARE MANAGMENT", items),),
       icon_class="mdi mdi-content-save",
   )
else:
    menu_items = items

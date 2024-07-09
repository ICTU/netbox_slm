from netbox.plugins import PluginMenuButton, PluginMenuItem

menu_items = (
    PluginMenuItem(
        link="plugins:netbox_slm:softwareproduct_list",
        link_text="Software Products",
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
                permissions=["netbox_slm.add_softwareproduct"],
            ),
        ),
    ),
    PluginMenuItem(
        link="plugins:netbox_slm:softwareproductversion_list",
        link_text="Versions",
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
                permissions=["netbox_slm.add_softwareproductversion"],
            ),
        ),
    ),
    PluginMenuItem(
        link="plugins:netbox_slm:softwareproductinstallation_list",
        link_text="Installations",
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
                permissions=["netbox_slm.add_softwareproductinstallation"],
            ),
        ),
    ),
    PluginMenuItem(
        link="plugins:netbox_slm:softwarelicense_list",
        link_text="Licenses",
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
                permissions=["netbox_slm.add_softwarelicense"],
            ),
        ),
    ),
)

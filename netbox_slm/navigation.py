from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices


menu_items = (
    PluginMenuItem(
        link='plugins:netbox_slm:softwareproduct_list',
        link_text='Software Products',
        buttons=(
            PluginMenuButton(
                "plugins:netbox_slm:softwareproduct_add",
                "Add",
                "mdi mdi-plus-thick",
                ButtonColorChoices.GREEN,
                permissions=["netbox_slm.add_softwareproduct"],
            ),
            PluginMenuButton(
                "plugins:netbox_slm:softwareproduct_import",
                "Import",
                "mdi mdi-upload",
                ButtonColorChoices.CYAN,
                permissions=["netbox_slm.add_softwareproduct"],
            ),
        )
    ),
    PluginMenuItem(
        link='plugins:netbox_slm:softwareproductversion_list',
        link_text='Versions',
        buttons=(
            PluginMenuButton(
                "plugins:netbox_slm:softwareproductversion_add",
                "Add",
                "mdi mdi-plus-thick",
                ButtonColorChoices.GREEN,
                permissions=["netbox_slm.add_softwareproductversion"],
            ),
            PluginMenuButton(
                "plugins:netbox_slm:softwareproductversion_import",
                "Import",
                "mdi mdi-upload",
                ButtonColorChoices.CYAN,
                permissions=["netbox_slm.add_softwareproductversion"],
            ),
        )
    ),
    PluginMenuItem(
        link='plugins:netbox_slm:softwareproductinstallation_list',
        link_text='Installations',
        buttons=(
            PluginMenuButton(
                "plugins:netbox_slm:softwareproductinstallation_add",
                "Add",
                "mdi mdi-plus-thick",
                ButtonColorChoices.GREEN,
                permissions=["netbox_slm.add_softwareproductinstallation"],
            ),
            PluginMenuButton(
                "plugins:netbox_slm:softwareproductinstallation_import",
                "Import",
                "mdi mdi-upload",
                ButtonColorChoices.CYAN,
                permissions=["netbox_slm.add_softwareproductinstallation"],
            ),
        )
    ),
)

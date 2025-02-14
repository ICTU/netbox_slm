from netbox.plugins import PluginTemplateExtension, get_plugin_config

installations = dict(
    device=get_plugin_config("netbox_slm", "link_device_installations"),
    cluster=get_plugin_config("netbox_slm", "link_cluster_installations"),
    virtualmachine=get_plugin_config("netbox_slm", "link_virtualmachine_installations"),
)


class InstallationsCard(PluginTemplateExtension):
    models = ["dcim.device", "virtualization.cluster", "virtualization.virtualmachine"]

    def get_object_name(self):
        object_model_meta = self.context["object"]._meta  # one of the self.models defined above
        return object_model_meta.model_name

    def render_card(self):
        return self.render(
            "netbox_slm/installations_card_include.html",
            extra_context={
                "search_obj": self.get_object_name(),
            },
        )

    def left_page(self):
        return self.render_card() if installations[self.get_object_name()] == "left" else ""

    def right_page(self):
        return self.render_card() if installations[self.get_object_name()] == "right" else ""

    def full_width_page(self):
        return self.render_card() if installations[self.get_object_name()] == "full" else ""


# auto imported by default PluginConfig.template_extensions = template_content.template_extensions
template_extensions = [InstallationsCard]

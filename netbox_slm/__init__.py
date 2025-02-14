from netbox.plugins import PluginConfig

__version__ = "1.7.0"


class SLMConfig(PluginConfig):
    name = "netbox_slm"
    verbose_name = "Software Lifecycle Management"
    version = __version__
    description = "Software Lifecycle Management Netbox Plugin."
    author = "ICTU"
    author_email = "open-source-projects@ictu.nl"
    base_url = "slm"
    required_settings = []
    default_settings = {
        "top_level_menu": True,
        "link_cluster_installations": "right",
        "link_device_installations": "right",
        "link_virtualmachine_installations": "right",
    }


config = SLMConfig

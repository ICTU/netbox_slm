from extras.plugins import PluginConfig

__version__ = "1.4"


class SLMConfig(PluginConfig):
    name = 'netbox_slm'
    verbose_name = 'Software Lifecycle Management'
    description = 'Software Lifecycle Management Netbox Plugin.'
    version = __version__
    author = 'ICTU'
    author_email = 'open-source-projects@ictu.nl'
    base_url = 'slm'
    required_settings = []
    default_settings = {
        'version_info': False
    }


config = SLMConfig

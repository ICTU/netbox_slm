from extras.plugins import PluginConfig


class SLMConfig(PluginConfig):
    name = 'netbox_slm'
    verbose_name = 'Software Lifecycle Management'
    description = 'Software Lifecycle Management'
    version = '1.1'
    author = 'Hedde van der Heide'
    author_email = 'hedde.vanderheide@ictu.nl'
    base_url = 'slm'
    required_settings = []
    default_settings = {
        'version_info': False
    }

config = SLMConfig

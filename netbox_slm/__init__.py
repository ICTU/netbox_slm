"""
Copyright 2022-2025 ICTU

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from netbox.plugins import PluginConfig

__version__ = "1.8.0"


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

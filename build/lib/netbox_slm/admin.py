from django.apps import apps
from django.conf import settings
from django.contrib import admin

if settings.DEBUG:
    for model in apps.get_app_config("netbox_slm").get_models():
        admin.site.register(model)

from django.urls import path, include

from netbox_slm import views  # noqa F401
from utilities.urls import get_model_urls

urlpatterns = [
    path("software-products/", include(get_model_urls("netbox_slm", "softwareproduct", detail=False))),
    path("software-products/<int:pk>/", include(get_model_urls("netbox_slm", "softwareproduct"))),
    path("versions/", include(get_model_urls("netbox_slm", "softwareproductversion", detail=False))),
    path("versions/<int:pk>/", include(get_model_urls("netbox_slm", "softwareproductversion"))),
    path("installations/", include(get_model_urls("netbox_slm", "softwareproductinstallation", detail=False))),
    path("installations/<int:pk>/", include(get_model_urls("netbox_slm", "softwareproductinstallation"))),
    path("licenses/", include(get_model_urls("netbox_slm", "softwarelicense", detail=False))),
    path("licenses/<int:pk>/", include(get_model_urls("netbox_slm", "softwarelicense"))),
]

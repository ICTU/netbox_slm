from netbox.api.routers import NetBoxRouter
from netbox_slm.api.views import (
    NetboxSLMRootView,
    SoftwareProductViewSet,
    SoftwareProductVersionViewSet,
    SoftwareProductInstallationViewSet,
)

router = NetBoxRouter()
router.APIRootView = NetboxSLMRootView

router.register("softwareproducts", SoftwareProductViewSet)
router.register("softwareproductversions", SoftwareProductVersionViewSet)
router.register("softwareproductinstallations", SoftwareProductInstallationViewSet)
urlpatterns = router.urls
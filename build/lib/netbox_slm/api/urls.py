from netbox.api.routers import NetBoxRouter
from netbox_slm.api.views import (
    NetboxSLMRootView,
    SoftwareProductViewSet,
    SoftwareProductVersionViewSet,
    SoftwareProductInstallationViewSet,
    SoftwareLicenseViewSet,
)

router = NetBoxRouter()
router.APIRootView = NetboxSLMRootView

router.register("softwareproducts", SoftwareProductViewSet)
router.register("softwareproductversions", SoftwareProductVersionViewSet)
router.register("softwareproductinstallations", SoftwareProductInstallationViewSet)
router.register("softwarelicenses", SoftwareLicenseViewSet)
urlpatterns = router.urls

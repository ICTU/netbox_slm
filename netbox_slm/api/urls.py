from netbox.api.routers import NetBoxRouter
from netbox_slm.api.views import (
    SoftwareProductViewSet,
    SoftwareProductVersionViewSet,
    SoftwareProductInstallationViewSet,
    SoftwareLicenseViewSet,
)

app_name = 'netbox_slm'

router = NetBoxRouter()
router.register("softwareproducts", SoftwareProductViewSet)
router.register("softwareproductversions", SoftwareProductVersionViewSet)
router.register("softwareproductinstallations", SoftwareProductInstallationViewSet)
router.register("softwarelicenses", SoftwareLicenseViewSet)

urlpatterns = router.urls

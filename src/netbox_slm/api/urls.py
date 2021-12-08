from netbox.api import OrderedDefaultRouter
from netbox_slm.api.views import (
    NetboxSLMRootView,
    SoftwareProductViewSet,
    SoftwareProductVersionViewSet,
)

router = OrderedDefaultRouter()
router.APIRootView = NetboxSLMRootView

router.register("softwareproducts", SoftwareProductViewSet)
router.register("softwareproductversions", SoftwareProductVersionViewSet)
urlpatterns = router.urls
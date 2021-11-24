from netbox.api import OrderedDefaultRouter
from netbox_slm.api.views import (
    NetboxSLMRootView,
    SoftwareProductViewSet
)

router = OrderedDefaultRouter()
router.APIRootView = NetboxSLMRootView

router.register("softwareproducts", SoftwareProductViewSet)
urlpatterns = router.urls
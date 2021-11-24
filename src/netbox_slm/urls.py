from django.urls import path
from extras.views import ObjectChangeLogView
from netbox_slm import views
from netbox_slm.models import SoftwareProduct, SoftwareProductVersion

urlpatterns = [
    # Software Products
    path("software-products/", views.SoftwareProductListView.as_view(), name='softwareproduct_list'),
    path("software-products/add/", views.SoftwareProductEditView.as_view(), name='softwareproduct_add'),
    path("software-products/import/", views.SoftwareProductBulkImportView.as_view(), name="softwareproduct_import"),
    path("software-products/edit/", views.SoftwareProductBulkEditView.as_view(), name="softwareproduct_bulk_edit"),
    path("software-products/delete/", views.SoftwareProductBulkDeleteView.as_view(), name="softwareproduct_bulk_delete"),
    path("software-products/<int:pk>/", views.SoftwareProductView.as_view(), name="softwareproduct"),
    path("software-products/<int:pk>/delete/", views.SoftwareProductDeleteView.as_view(), name="softwareproduct_delete"),
    path("software-products/<int:pk>/edit/", views.SoftwareProductEditView.as_view(), name="softwareproduct_edit"),
    path(
        "software-products/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="softwareproduct_changelog",
        kwargs={"model": SoftwareProduct},
    ),

    # Software Product Versions
    path("versions/", views.SoftwareProductVersionListView.as_view(), name='softwareproductversion_list'),
    path("versions/add/", views.SoftwareProductVersionEditView.as_view(), name='softwareproductversion_add'),
    path("versions/import/", views.SoftwareProductVersionBulkImportView.as_view(), name="softwareproductversion_import"),
    path("versions/edit/", views.SoftwareProductVersionBulkEditView.as_view(), name="softwareproductversion_bulk_edit"),
    path("versions/delete/", views.SoftwareProductVersionBulkDeleteView.as_view(), name="softwareproductversion_bulk_delete"),
    path("versions/<int:pk>/", views.SoftwareProductVersionView.as_view(), name="softwareproductversion"),
    path("versions/<int:pk>/delete/", views.SoftwareProductVersionDeleteView.as_view(), name="softwareproductversion_delete"),
    path("versions/<int:pk>/edit/", views.SoftwareProductVersionEditView.as_view(), name="softwareproductversion_edit"),
    path(
        "versions/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="softwareproductversion_changelog",
        kwargs={"model": SoftwareProductVersion},
    ),
]

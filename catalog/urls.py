from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (
    HomeView,
    ContactsView,
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("product_list/", ProductListView.as_view(), name="product_list"),
    path("product_list/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="product_detail"),
    path("product_list/create", ProductCreateView.as_view(), name="product_create"),
    path(
        "product_list/<int:pk>/update",
        ProductUpdateView.as_view(),
        name="product_update",
    ),
    path(
        "product_list/<int:pk>/delete",
        ProductDeleteView.as_view(),
        name="product_delete",
    ),
]

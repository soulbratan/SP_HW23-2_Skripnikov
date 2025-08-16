from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import HomeView, ContactsView, ProductListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product_list/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]

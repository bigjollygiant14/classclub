from django.urls import path

# from .views import ProductDetailView, ProductListView
from .views import active_manufacturers, manufacturer_detail, product_detail, product_list

urlpatterns = [
    # path("", ProductListView.as_view(), name="product-list"),
    # path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail")
    path("products/", product_list, name="product-list"),
    path("products/<int:pk>/", product_detail, name="product-detail"),
    path("manufacturers/", active_manufacturers, name="active-manufacturers"),
    path("manufacturers/<int:pk>/", manufacturer_detail, name="manufacturer-detail")
]

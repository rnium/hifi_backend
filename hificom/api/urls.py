from django.urls import path
from hificom.api import views

urlpatterns = [
    path('homepage/', views.user_homepage, name="user_homepage"),
    path('homepage/stats/', views.dashboard_stats, name="dashboard_stats"),
    path('categories/', views.CategoriesView.as_view(), name="categories"),
    path('categories/<str:identifier>/', views.ViewCategory.as_view(), name="view_category"),
    path('categories/<str:identifier>/groups/', views.CategoryGroupsView.as_view(), name="view_category_groups"), # slug of root
    path('categories/<str:identifier>/tables/', views.CategorTablesView.as_view(), name="category_tables"),
    path('categories/<str:slug>/tables/update/', views.update_tables, name="update_tables"),
    path('categories/<str:slug>/products/unpaginated/', views.CategoryUnpaginatedProductsView.as_view(), name="category_products_unpaginated"),
    path('categories/<str:slug>/products/', views.CategoryProductsView.as_view(), name="category_products"),
    path('categories/<str:slug>/allproducts/', views.AllProductsSemiDetailView.as_view(), name="all_products_full"),
    path('t/<str:slug>/products/', views.TaggedProductsView.as_view(), name="tagged_products"),
    path('t/<str:slug>/products/unpaginated/', views.TaggedProductsUnpaginatedView.as_view(), name="tagged_products_unpaginated"),
    path('categories/<str:slug>/addproduct/', views.add_product, name="add_product"),
    path('cartproducts/', views.get_cart_products, name="cartproducts"),
    path('initwishlist/', views.initiate_wishlist, name="initiate_wishlist"),
    path('syncwishlist/', views.sync_wishlist, name="sync_wishlist"),
    path('applycoupon/', views.apply_coupon, name="apply_coupon"),
    path('searchproduct/', views.SearchProduct.as_view(), name="search_product"),
    path('product/<str:slug>/', views.ProductDetailView.as_view(), name="detailed_product"),
    path('product/<str:slug>/keyfeatures/', views.ProductKeyFeaturesView.as_view(), name="product_keyfeatures"),
    path('product/<int:pk>/edit/', views.edit_product, name="edit_product"),
    path('product/<int:pk>/delete/', views.DeleteProduct.as_view(), name="delete_product"),
    path('product/<int:pk>/alterstock/', views.alter_stock_status, name="alter_stock_status"),
    path('relatedproducts/<int:pk>/', views.RelatedProductsView.as_view(), name="related_products"),
    path('order/confirm/', views.ConfirmOrder.as_view(), name="confirm_order"),
]

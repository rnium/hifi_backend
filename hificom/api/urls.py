from django.urls import path
from hificom.api import views

urlpatterns = [
    path('categories/', views.CategoriesView.as_view(), name="categories"),
    path('categories/<str:slug>/', views.ViewCategory.as_view(), name="view_category"),
    path('categories/<str:slug>/tables/update/', views.update_tables, name="update_tables"),
]

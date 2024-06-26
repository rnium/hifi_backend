from django.urls import path
from hificom.api import views

urlpatterns = [
    path('categories/', views.CategoryView.as_view(), name="categories"),
]

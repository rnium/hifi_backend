from django.urls import path
from . import views

urlpatterns = [
    path('admin/token/login/', views.admin_token_login, name='admin_token_login'),
    path('profile/update/', views.update_profile, name='update_profile'),
]

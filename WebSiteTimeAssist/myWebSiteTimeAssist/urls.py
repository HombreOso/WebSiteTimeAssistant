# urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('delete_account/', views.delete_account_rendering, name='delete_account'),
    path('delete_account_decided/', views.delete_account, name='delete_account_decided'),
    path('user_profile/', views.user_profile, name="user_profile"),
    path('', views.home_rendering, name="home")
]

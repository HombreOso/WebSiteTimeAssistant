# urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('delete_account/', views.delete_account, name='delete_account'),
    path('user_profile/', views.user_profile, name="user_profile")
]

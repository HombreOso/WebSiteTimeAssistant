# urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('delete_account/', views.delete_account, name='delete_account'),
]

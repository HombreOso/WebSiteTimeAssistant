# urls.py

from django.urls import path
from .views import delete_account

urlpatterns = [
    # Other URL patterns
    path('delete_account/', delete_account, name='delete_account'),
]

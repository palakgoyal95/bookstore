from django.urls import path
from .views import register, test_protected

urlpatterns = [
    path('register/', register),
    path('test-protected/', test_protected),
]

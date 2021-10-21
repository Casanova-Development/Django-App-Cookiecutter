"""{{ cookiecutter.app_name|capitalize }} urls module."""

# Django
from django.urls import include, path
# Django Rest Framework
from rest_framework.routers import DefaultRouter

# Local views
# Your imports goes here.


router_v1 = DefaultRouter()

# Your paths goes here. Use router.register().

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]

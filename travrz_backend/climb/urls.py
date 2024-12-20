"""
URL mappings for the climb app.
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from climb import views

router = DefaultRouter()
# will create the following routes for us automatically
# based on the viewset actions we've defined
router.register("", views.ClimbViewSet)
router.register("tags", views.TagViewSet)

app_name = "climb"

urlpatterns = [
    path("", include(router.urls)),
]

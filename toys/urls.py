from django.urls import path, include
from rest_framework.routers import DefaultRouter
from toys.views import ToyViewSet

router = DefaultRouter()
router.register(r'toys', ToyViewSet, basename='toy')

urlpatterns = [
    path('', include(router.urls)),
]

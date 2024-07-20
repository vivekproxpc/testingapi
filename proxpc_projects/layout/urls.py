from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LayoutViewSet, SectionViewSet,SectionDetailViewSet

router = DefaultRouter()
router.register(r'layouts', LayoutViewSet)
router.register(r'sections', SectionViewSet)
router.register(r'section-details', SectionDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

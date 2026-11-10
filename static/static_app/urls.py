from .views import NoteViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'notes', NoteViewSet, basename='note')
urlpatterns = router.urls
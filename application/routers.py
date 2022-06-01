from rest_framework import routers
from application.viewsets import BookViewSet

router = routers.DefaultRouter()
router.register('books', BookViewSet)
from django.urls import path, include
from application.routers import router

urlpatterns = [
    path('', include(router.urls))
]
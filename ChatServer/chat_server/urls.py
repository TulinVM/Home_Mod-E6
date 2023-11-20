from .views import ApiUsers, ApiRooms
from rest_framework.routers import DefaultRouter
from django.urls import path, include


router = DefaultRouter()
router.register('rooms', ApiRooms)
router.register('users', ApiUsers)

urlpatterns = [
    path('', ApiUsers.as_view({'get': 'list'})),
    path('api/', include(router.urls)),
]

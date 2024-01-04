from rest_framework import routers
from .views import EventViewSet, UserInvitedViewSet
from django.urls import include, path, re_path


router = routers.DefaultRouter()
router.register(r'event', EventViewSet)
router.register(r'user/invite', UserInvitedViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]

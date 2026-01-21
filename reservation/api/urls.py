from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.artist import ArtistViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'artists', ArtistViewSet, basename='artist')

urlpatterns = [
    path('', include(router.urls)),
]

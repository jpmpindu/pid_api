# api/views/artist.py
from rest_framework import viewsets
from api.models.artist import Artist
from api.serializers.artist import ArtistSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

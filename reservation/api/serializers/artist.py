from rest_framework import serializers
from api.models.artist import Artist

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'firstname', 'lastname']  # adapte selon tes champs

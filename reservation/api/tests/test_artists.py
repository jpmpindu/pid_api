from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models.artist import Artist

class ArtistAPITests(APITestCase):

    def setUp(self):
        """
        Crée des artistes de test dans une DB vierge.
        """
        self.artist1 = Artist.objects.create(firstname="Test", lastname="Artist1")
        self.artist2 = Artist.objects.create(firstname="Demo", lastname="Artist2")

    def test_get_artist_list(self):
        """
        Récupérer la liste des artistes.
        """
        url = reverse('api:artist-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_artist(self):
        """
        Créer un nouvel artiste via l'API.
        """
        url = reverse('api:artist-list')
        data = {"firstname": "New", "lastname": "Artist"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Artist.objects.count(), 3)
        self.assertEqual(Artist.objects.get(id=response.data['id']).firstname, "New")

    def test_get_artist_detail(self):
        """
        Récupérer le détail d'un artiste existant.
        """
        url = reverse('api:artist-detail', args=[self.artist1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['firstname'], "Test")

    def test_update_artist(self):
        """
        Mettre à jour un artiste existant.
        """
        url = reverse('api:artist-detail', args=[self.artist1.id])
        data = {"firstname": "Updated", "lastname": self.artist1.lastname}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Artist.objects.get(id=self.artist1.id).firstname, "Updated")

    def test_delete_artist(self):
        """
        Supprimer un artiste.
        """
        url = reverse('api:artist-detail', args=[self.artist2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Artist.objects.filter(id=self.artist2.id).exists())

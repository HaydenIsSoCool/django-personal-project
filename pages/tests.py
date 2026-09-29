from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Pokemon
from django.urls import reverse

# Create your tests here.
class Pokedex(TestCase):
    @classmethod
    def setUpTestData(cls):
        # makes a fake user
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="bestpasswordever"
        )

        # fake user makes a fake pokemon
        cls.pokemon = Pokemon.objects.create(
            name="Testmon",
            type= "Test / Flying",
            dexNum = "0198",
            gen = "Test Land",
            cover = "bulbasaur.jfif"
        )

    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get('/pokemon/1/')
        self.assertEqual(response.status_code, 200)

    # Checks to make sure pokemon webpage exists
    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get('/pokemon/1/')
        self.assertEqual(response.status_code, 200)

    
    # Checks to make sure that homepage 
    def test_pokemon_listview(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test")
        self.assertTemplateUsed(response, 'home.html') 


    def test_pokemon_model(self):
        self.assertEqual(self.pokemon.name, "Testmon")
        self.assertEqual(self.pokemon.type, "Test / Flying")
        self.assertEqual(self.pokemon.dexNum, "0198")
        self.assertEqual(self.pokemon.gen, "Test Land")
        self.assertEqual(self.pokemon.get_absolute_url(), "/pokemon/1/")    

      # checks to makes ure that post page works
    def test_post_detailview(self):
        response = self.client.get(reverse('pokemon_detail', kwargs={"pk": self.pokemon.pk}))
        no_response = self.client.get("/post/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Testmon")
        self.assertTemplateUsed(response, "pokemon_detail.html")

    ### Github username = HaydenIsSoCool
    ### Github password = Murkrow2011!

        
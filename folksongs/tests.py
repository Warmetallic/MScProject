from django.test import Client, TestCase
from django.urls import reverse

# Create your tests here.
class CountryTests(TestCase):

    def test_temp_text(self):
        country = Client()
        response = country.get('/')
        self.assertEqual(response.status_code, 200)

    def test_story_text(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Folk")

    def test_story_text_song(self):
        client = Client()
        response = client.get('/song/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Song")

    def test_story_text_signup(self):
        client = Client()
        response = client.get('/signup/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Registration")

    def test_view_uses_correct_template_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_view_uses_correct_template_song(self):
        response = self.client.get(reverse('song'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'song.html')

    def test_view_uses_correct_template_signup(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_view_uses_correct_template_login(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_view_uses_correct_template_logout(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/logged_out.html')



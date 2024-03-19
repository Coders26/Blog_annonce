from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from .models import Annonce, Commentaire, Info
from django.contrib.auth.models import User



class NewAnnonceTestCase(TestCase):
    def test_new_annonce_success(self):
        url = reverse('new_annonce')
        data = {
            'title': 'Test Title',
            'image': SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg"),
            'description': 'Test Description',
            'contenu': 'Test Content'
        }
        response = self.client.post(url, data, format='multipart')
        self.assertRedirects(response, reverse('annonce'))
        self.assertTrue(Annonce.objects.filter(title='Test Title').exists())

    def test_new_annonce_GET_request(self):
        url = reverse('new_annonce')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class AnnonceSingleViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create sample objects
        cls.user = User.objects.create(username='testuser', password='testpassword')
        # Create a simple image file for testing
        image_file = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        cls.annonce = Annonce.objects.create(
            title='Test Annonce',
            description='Description',
            contenu='Contenu',
            image=image_file
        )

    def test_annonce_single_view(self):
        # Access the view for the Annonce object created
        url = reverse('annonce_single', kwargs={'pk': self.annonce.pk})
        response = self.client.get(url)

        # Check if the response is successful (status code 200)
        self.assertEqual(response.status_code, 200)

        # Check if the correct annonce is displayed
        self.assertContains(response, self.annonce.title)
        self.assertContains(response, self.annonce.description)
        self.assertContains(response, self.annonce.contenu)

    def test_comment_creation_and_display(self):
        # Prepare data for the comment
        comment_data = {
            'name': 'Test User',
            'comment': 'Test Comment'
        }

        # Access the view to create the comment
        url = reverse('annonce_single', kwargs={'pk': self.annonce.pk})
        response = self.client.post(url, comment_data)

        # Check if the comment is created successfully
        self.assertEqual(response.status_code, 200)

        # Check if the comment is associated with the correct annonce
        self.assertTrue(
            Commentaire.objects.filter(nom='Test User', commentaire='Test Comment', annonce=self.annonce).exists())

        # Now, let's retrieve the page again to see if the comment is displayed
        response = self.client.get(url)

        # Check if the comment is displayed
        self.assertContains(response, 'Test User')
        self.assertContains(response, 'Test Comment')
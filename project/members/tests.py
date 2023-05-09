from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Profile, ProfilePicture
from io import BytesIO
from django.core.files.base import ContentFile
from PIL import Image

# Used to create a 'fake' image for testing
def create_test_image(filename='test_image.jpg', size=(100, 100), color='blue', image_format='JPEG'):
    img_file = BytesIO()
    image = Image.new('RGB', size, color)
    image.save(img_file, image_format)
    img_file.seek(0)
    return ContentFile(img_file.read(), filename)

class UserRegistrationTestCase(TestCase):

    def test_user_registration(self):
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        }
        response = self.client.post(reverse('signup'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testuser').exists())


class UserAuthenticationTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword123'
        )


    def test_user_signin(self):
        response = self.client.post(reverse('signin'), {
            'username': 'testuser',
            'password': 'testpassword123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.wsgi_request.user.is_authenticated)


    def test_user_signout(self):
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.get(reverse('signout'))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(response.wsgi_request.user.is_authenticated)


class UserProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword123'
        )
        self.user2 = User.objects.create_user(
            username='testuser2',
            email='testuser2@example.com',
            password='testpassword123'
        )
        self.profile_picture = ProfilePicture.objects.create(image=create_test_image())



    def test_user_profile_created(self):
        self.assertTrue(Profile.objects.filter(user=self.user).exists())


    def test_user_profile_view(self):
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.get(reverse('view_user', args=[self.user.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')


    def test_user_account_update(self):
        self.client.login(username='testuser', password='testpassword')

        mock_image = SimpleUploadedFile('test_image.jpg', b'file_content', content_type='image/jpeg')

        response = self.client.post(reverse('update_account'), {
            'username': 'newusername',
            'email': 'newemail@test.com',
            'image': mock_image
        })

        self.assertEqual(response.status_code, 302)



    def test_user_follow_unfollow(self):
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.post(reverse('follow', args=[self.user2.pk]), {'next': '/'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.user2.profile.followers.filter(pk=self.user.pk).exists())
        self.assertTrue(self.user.profile.following.filter(pk=self.user2.pk).exists())

        response = self.client.post(reverse('follow', args=[self.user2.pk]), {'next': '/'})
        self.assertEqual(response.status_code, 302)
        self.assertFalse(self.user2.profile.followers.filter(pk=self.user.pk).exists())
        self.assertFalse(self.user.profile.following.filter(pk=self.user2.pk).exists())


    def test_user_set_profile_picture(self):
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.post(reverse('setpicture', args=[self.profile_picture.pk]), {'next': '/'})
        self.assertEqual(response.status_code, 302)
        updated_user = User.objects.get(pk=self.user.pk)
        self.assertEqual(updated_user.profile.image, self.profile_picture.image)


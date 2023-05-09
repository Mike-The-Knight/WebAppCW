from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from datetime import timedelta
from django.utils import timezone

from .models import Comment, Review, Post

class CommentTestCase(TestCase):
    def test_comment_str(self):
        user = User.objects.create(username='testuser')
        comment = Comment(author=user, text="Test Comment")
        self.assertEqual(str(comment), "Test Comment")

class ReviewTestCase(TestCase):
    def test_review_str(self):
        user = User.objects.create(username='testuser')
        review = Review(author=user, title="Test Review", text="Test Review Text", rating=3)
        self.assertEqual(str(review), "Test Review")

class PostTestCase(TestCase):
    def test_post_str(self):
        user = User.objects.create(username='testuser')
        post = Post(title="Test Post", type="RECIPE", description="Test Description", author=user)
        self.assertEqual(str(post), "Test Post")

class PostListViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post1 = Post.objects.create(title='Test Post 1', description='Test Description 1', type='RECIPE',
                                         author=self.user, date_posted=timezone.now() - timedelta(days=2))
        self.post2 = Post.objects.create(title='Test Post 2', description='Test Description 2', type='RECIPE',
                                         author=self.user, date_posted=timezone.now() - timedelta(days=1))

    def test_post_list_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/home.html')

    def test_post_list_view_queryset(self):
        response = self.client.get(reverse('home'))
        posts = response.context['posts']
        self.assertEqual(len(posts), 2)
        self.assertEqual(posts[0].title, 'Test Post 2')
        self.assertEqual(posts[1].title, 'Test Post 1')

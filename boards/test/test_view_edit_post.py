from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from ..models import Board, Post, Topic
from ..views import PostUpdateView


class PostUpdateViewTestCase(TestCase):
	def setUp(self):
		self.board = Board.objects.create(name="Django", description="I am tired")
		self.username = 'von'
		self.password = '124'
		user = User.objects.create_user(username=self.username, email = 'von@yahoo.com', password=self.password)
		self.topic = Topic.objects.create(subject='The Case of Sherlock', board=self.board, starter=user)
		self.post = Post.objects.create(message='This is the curious case of Jekyll and Hyde', topic=self.topic, created_by=user)
		self.url = reverse('edit_post', kwargs={'pk': self.board.pk, 'topic_pk': self.topic.pk, 'post_pk': self.post.pk})


class LoginRequiredPostUpdateViewTests(PostUpdateViewTestCase):
	def test_redirection(self):
		login_url = reverse('login')
		response = self.client.get(self.url)
		self.assertRedirects(response, '{login_url}?next={url}'.format(login_url=login_url, url=self.url))


class UnauthorizedPostUpdateViewTests(PostUpdateViewTestCase):
	def setUp(self):
		super().setUp()
		username = 'chinelo'
		password = '421'
		user = User.objects.create_user(username=username, email='chinelo@yahoo.com', password=password)
		self.client.login(username=username, password=password)
		self.response = self.client.get(self.url)

	def test_status_code(self):
		self.assertEquals(self.response.status_code, 404)
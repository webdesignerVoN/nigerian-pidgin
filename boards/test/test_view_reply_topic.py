from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from ..models import Board, Post, Topic
from ..views import reply_topic

class ReplyTopicTestCase(TestCase):
    '''
    Base test case to be used in all `reply_topic` view tests
    '''
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Na here we dey.')
        self.username = 'von'
        self.password = '123'
        user = User.objects.create_user(username=self.username, email='von@yahoo.com', password=self.password)
        self.topic = Topic.objects.create(subject='Hello, suckers', board=self.board, starter=user)
        Post.objects.create(message='I really am tired', topic=self.topic, created_by=user)
        self.url = reverse('reply_topic', kwargs={'pk': self.board.pk, 'topic_pk': self.topic.pk})
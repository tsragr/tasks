from django.test import TestCase
from ..models import User


class UserTest(TestCase):
    """ Test module for User model """

    def setUp(self):
        User.objects.create(
            name='Maxim', age=25)
        User.objects.create(
            name='Misha', age=24)

    def test_user(self):
        user_maxim = User.objects.get(name='Maxim')
        user_misha = User.objects.get(name='Misha')

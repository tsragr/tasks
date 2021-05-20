import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import User
from ..serializers import UserSerializer

# initialize the APIClient app
client = Client()


class GetAllUsersTest(TestCase):
    """ Test module for GET all users API """

    def setUp(self):
        User.objects.create(
            name='Oleg', age=55)
        User.objects.create(
            name='Olga', age=18)
        User.objects.create(
            name='Katya', age=30)
        User.objects.create(
            name='Marina', age=21)

    def test_get_all_users(self):
        # get API response
        response = client.get(reverse('get_post_users'))
        # get data from db
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleUserTest(TestCase):
    """ Test module for GET single user API """

    def setUp(self):
        self.oleg = User.objects.create(
            name='Oleg', age=55)
        self.olga = User.objects.create(
            name='Olga', age=18)
        self.katya = User.objects.create(
            name='Katya', age=30)
        self.marina = User.objects.create(
            name='Marina', age=21)

    def test_get_valid_single_user(self):
        response = client.get(
            reverse('get_delete_update_user', kwargs={'pk': self.oleg.pk}))
        user = User.objects.get(pk=self.oleg.pk)
        serializer = UserSerializer(user)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_user(self):
        response = client.get(
            reverse('get_delete_update_user', kwargs={'pk': 666}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewUserTest(TestCase):
    """ Test module for inserting a new user """

    def setUp(self):
        self.valid_payload = {
            'name': 'Oleg',
            'age': 55,
        }
        self.invalid_payload = {
            'name': '',
            'age': 4,
        }

    def test_create_valid_user(self):
        response = client.post(
            reverse('get_post_users'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_user(self):
        response = client.post(
            reverse('get_post_users'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleUserTest(TestCase):
    """ Test module for updating an existing user record """

    def setUp(self):
        self.oleg = User.objects.create(
            name='Oleg', age=55)
        self.olga = User.objects.create(
            name='Olga', age=18)
        self.valid_payload = {
            'name': 'Maxim',
            'age': 25,
        }
        self.invalid_payload = {
            'name': '',
            'age': 4,
        }

    def test_valid_update_user(self):
        response = client.put(
            reverse('get_delete_update_user', kwargs={'pk': self.oleg.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_user(self):
        response = client.put(
            reverse('get_delete_update_user', kwargs={'pk': self.oleg.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleUserTest(TestCase):
    """ Test module for deleting an existing user record """

    def setUp(self):
        self.oleg = User.objects.create(
            name='Oleg', age=55)
        self.olga = User.objects.create(
            name='Olga', age=18)

    def test_valid_delete_user(self):
        response = client.delete(
            reverse('get_delete_update_user', kwargs={'pk': self.oleg.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_user(self):
        response = client.delete(
            reverse('get_delete_update_user', kwargs={'pk': 666}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

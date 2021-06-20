from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import SpongeBob



# Create your tests here.

class PostModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_post = SpongeBob.objects.create(
            author = test_user,
            title = 'Sponge',
            body = 'A yellow sea sponge'
        )
        test_post.save()
        
    def test_blog_content(self):
        post = SpongeBob.objects.get(id=1)

        self.assertEqual(str(post.author), 'tester')
        self.assertEqual(post.title, 'Sponge')
        self.assertEqual(post.body, 'A yellow sea sponge')
class APITest(APITestCase):
    def test_list(self):
        response = self.client.get(reverse('posts_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create(self):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        url = reverse('posts_list')
        data = {
            "title":"Sponge",
            "body":"A yellow sea sponge",
            "author":test_user.id,
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, test_user.id)

        self.assertEqual(SpongeBob.objects.count(), 1)
        self.assertEqual(SpongeBob.objects.get().title, data['title'])

    def test_update(self):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_post = SpongeBob.objects.create(
            author = test_user,
            title = 'Sponge',
            body = 'A yellow sea sponge'
        )

        test_post.save()

        url = reverse('posts_detail',args=[test_post.id])
        data = {
            "title":'Sponge',
            "author":test_post.author.id,
            "body":test_post.body,
        }

        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK, url)

        self.assertEqual(SpongeBob.objects.count(), test_post.id)
        self.assertEqual(SpongeBob.objects.get().title, data['title'])


    def test_delete(self):

        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_post = SpongeBob.objects.create(
            author = test_user,
            title = 'Sponge',
            body = 'A yellow sea sponge'
        )

        test_post.save()

        post = SpongeBob.objects.get()

        url = reverse('posts_detail', kwargs={'pk': post.id})


        response = self.client.delete(url)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT, url)


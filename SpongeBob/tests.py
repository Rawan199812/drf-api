from django.test import TestCase
from django.contrib.auth import get_user_model


# Create your tests here.
from .models import SpongeBob

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


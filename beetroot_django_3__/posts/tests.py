from django.test import TestCase

# Create your tests here.
from .models import Post

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='just a test')
    
    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name,'just a test')
    
    def test_post_list_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'just a test')
        self.assertTemplateUsed(response,'home.html')

    # def test_post_detail_view(self):
    #     response = self.client.get('/post/1/')
    #     no_response = self.client.get('/post/100000/')
    #     self.assertEqual(response.status_code,200)
    #     self.assertEqual(no_response.status_code,404)
    #     self.assertContains(response,'just a test')
    #     self.assertTemplateUsed(response,'post_detail.html')
    
    def test_post_create_view(self):
        response = self.client.post('/post/new/',{'text':'New post'})
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'New post')
        self.assertTemplateUsed(response,'post_new.html')
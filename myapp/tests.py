from django.test import TestCase
from myapp.models import Post
# Create your tests here.
class PostTestcase(TestCase):
	def setUp(self):
		Post.objects.all()
	def test_post(self):
		post=Post.object.get(tag_slug)
		self.assertEqual(tag_slug)
		
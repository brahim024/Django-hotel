from django.db import models
from django.conf import settings
from django.utils.text import slugify
# Create your models here.
class Image(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='created',on_delete=models.CASCADE)
	title=models.CharField(max_length=150)
	slug=models.SlugField(max_length=100,blank=True)
	url=models.URLField()
	description=models.TextField(blank=True)
	created=models.DateTimeField(auto_now=True,db_index=True)
	user_like=models.ManyToManyField(settings.AUTH_USER_MODEL,
										related_name='image_likes',blank=True)
	def __str__(self):
		return self.title


	def save(self,*args,**kwargs):
		if not self.slug:
			self.slug=slugify(self.title)
		super().save(*args,**kwargs)

from django.db import models

# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length=200)
	pub_data = models.DateTimeField()
	body = models.TextField()
	image = models.ImageField(upload_to = 'images/')
	def __str__(self):   
		return self.title # 타이틀을 리턴시켜줌 

	def summary(self):
		return self.body[:20]

class Post(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):   
		return self.title # 타이틀을 리턴시켜줌 

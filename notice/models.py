from django.db import models

# Create your models here.
class Post(models.Model):
	writer = models.CharField(max_length=100)
	post_date = models.DateTimeField(auto_now_add=True)
	post_title = models.CharField(max_length=100)
	post_contents = models.TextField(blank=True,help_text='Post Contents')
	
	class Meta:
		ordering = [' -post_date']

	def __str__(self):
		return self.post_title

	def get_abolute_url(self):
		return reverse('post-detail', args=[str(self.id)])

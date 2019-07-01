from django.db import models

# Create your models here.
class Profile(models.Model):
	name = models.CharField(max_length=120, null=False)
	description = models.TextField(default = 'description default text')
	department = models.CharField(max_length=120, null=False)
	def __unicode__(self):
		return self.name


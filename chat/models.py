from django.db import models

# Create your models here.
class chat(models.Model):
	question = models.CharField(max_length=120, null=False)
	answer = models.CharField(max_length=120, null=False)
	published_date = models.DateTimeField(blank=True, null=True)
	def __unicode__(self):
		return self.name
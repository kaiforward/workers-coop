from django.db import models
from tinymce import models as tinymce_models
# Create your models here.

class HomeText(models.Model):
	# product to assign new choosable attributes to.
	description = tinymce_models.HTMLField()

	def __str__(self):
		return "Home Page Text"

class AboutText(models.Model):
	# product to assign new choosable attributes to.
	description = tinymce_models.HTMLField()

	def __str__(self):
		return "About Page Text"

class MembersAgreement(models.Model):
	# product to assign new choosable attributes to.
	description = tinymce_models.HTMLField()

	def __str__(self):
		return "Members Agreement"
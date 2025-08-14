from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	ACCOUNT_TYPE_CHOICES = [('D', 'Doctor'), ('P', "Patient")]

	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField(unique=True)
	account_type = models.CharField(max_length=1, choices=ACCOUNT_TYPE_CHOICES)
	profile_image = models.ImageField(upload_to="accounts/profile_images")
	address = models.TextField()


from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
# from django.contrib.auth.models import User

class User(AbstractBaseUser):
	phone_number = models.CharField(max_length=11, unique=True)
	username = models.CharField(max_length=100,unique=True)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	objects = UserManager()

	USERNAME_FIELD = 'phone_number'
	REQUIRED_FIELDS = [ 'username',]

	def __str__(self):
		return self.username

	@property
	def is_staff(self):
		return self.is_admin
    
	# def has_

class OtpCode(models.Model):
	phone_number = models.CharField(max_length=11, unique=True)
	code = models.PositiveSmallIntegerField()
	created = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.phone_number} - {self.code} - {self.created}'
class Relation(models.Model):
	from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
	to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.from_user} following {self.to_user}'





class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	age = models.PositiveSmallIntegerField(default=0)
	bio = models.TextField(null=True, blank=True)
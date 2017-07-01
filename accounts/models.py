#accounts/models.py
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class Profile(models.Model):
	# user = models.ForeignKey(User) # 이건 배드케이스라고 함!!
	# user = models.OneToOneField(User)
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	phone_number = models.CharField(max_length=20)
	address = models.CharField(max_length=50) 
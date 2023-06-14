from django.db import models
from django.contrib.auth.models import User

class UserRegistrationModel(User):
    password_confirmation = models.CharField(max_length=50)

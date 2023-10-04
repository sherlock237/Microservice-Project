from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_id = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
            return self.email_id
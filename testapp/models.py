from django.db import models

# Create your models here.
class Test(models.Model):
    test_name = models.CharField(max_length=255)
    test_text = models.TextField(max_length=255)
    
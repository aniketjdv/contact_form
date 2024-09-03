from django.db import models
from django.utils import timezone
# Create your models here.
class Contact_Enquriy(models.Model):
    en_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    message=models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self) :
        return self.name
from django.db import models

# Create your models here.
class BloodInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    phono = models.CharField(max_length=15)
    email = models.EmailField()
    blood_group = models.CharField(max_length=10)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.blood_group}"

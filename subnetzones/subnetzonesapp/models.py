from django.db import models

class subnetmodel(models.Model):
    subnet = models.CharField(max_length=30)
    zone = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.subnet} {self.zone}"
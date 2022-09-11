from django.db import models

# Create your models here.


class Request(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f"Name: {self.name},   Number: {self.number},   Address: {self.address}"


class Advertise(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField(default="")
    image = models.ImageField(upload_to="media",blank = False, null = False)

    def __str__(self):
        return self.title

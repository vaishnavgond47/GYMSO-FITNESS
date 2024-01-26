from django.db import models

# Create your models here.


class Feedback(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Membership(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    number = models.CharField(max_length=13)
    message = models.CharField(max_length=250)

    def __str__(self):
        return self.name

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=15)
    age = models.IntegerField()
    city = models.CharField(max_length=15)


class SignUp(models.Model):
    email = models.EmailField()
    number = models.IntegerField()
    username = models.CharField(max_langth=10)
    password = models.CharField(max_length=15)
    password_check = models.CharField(max_length=15)

class login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=15)





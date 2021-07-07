from django.db import models

class Book(models.Model):
    bookid = models.CharField(max_length=9)
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre= models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    photo = models.CharField(max_length=2083)
    adminid = models.CharField(max_length=9)  

class Admin(models.Model):
    adminid = models.CharField(max_length=9)
    name = models.CharField(max_length=100)
    logid = models.CharField(max_length=100)
    password= models.CharField(max_length=100)

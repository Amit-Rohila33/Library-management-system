from re import A
from statistics import mode
from django.db import models

# Create your models here.



class IB(models.Model):
    Book_id= models.AutoField(primary_key=True)
    BookName = models.CharField(max_length=500)
    WriterName = models.CharField(max_length=500)
    stname = models.CharField(max_length=500)
    stemail = models.CharField(max_length=500)
    stdept = models.CharField(max_length=500)
    DateIssued = models.DateField()

class RB(models.Model):
    Book_id= models.AutoField(primary_key=True)
    BookName = models.CharField(max_length=500)
    WriterName = models.CharField(max_length=500)
    stname = models.CharField(max_length=500)
    stemail = models.CharField(max_length=500)
    stdept = models.CharField(max_length=500)
    Datereturned = models.DateField()

class ABB(models.Model):
    Book_id= models.AutoField(primary_key=True)
    BookName = models.CharField(max_length=500)
    WriterName = models.CharField(max_length=500)
    stname = models.CharField(max_length=500)
    stemail = models.CharField(max_length=500)
    stdept = models.CharField(max_length=500)
    Dateretreived= models.DateField()



class NAB(models.Model):
    Book_id= models.AutoField(primary_key=True)
    BookName = models.CharField(max_length=500)
    WriterName = models.CharField(max_length=500)
    DateAdded= models.DateField()
    

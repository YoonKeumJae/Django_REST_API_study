from django.db import models

class Book(models.Model):
    bid = models.IntegerField(primary_key=True) #book id
    title = models.CharField(max_length=50) #book title
    author = models.CharField(max_length=50) #book author
    category = models.CharField(max_length=50) #book category
    pages = models.IntegerField() #book pages
    price = models.IntegerField() #book price
    published_date = models.DateField() #book published date
    description = models.TextField() #book description
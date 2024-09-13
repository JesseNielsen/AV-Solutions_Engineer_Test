from django.db import models

# TO-DO
# Review the model below. You should not need to create any more models or modify this file, though you are welcome
# to if you want to add additional properties and functionality to the app. 
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()

    def __str__(self):
        
        return self.title

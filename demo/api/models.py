from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30, default='')
    price = models.FloatField()
    description = models.TextField(default='')
    count= models.IntegerField()
    category_id=models.IntegerField()

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count,
            'category_id': self.category_id
        }

class Category(models.Model):
    name= models.CharField(max_length=30, default='')


    def to_json(self):
        return{
            'id': self.id,
            'name': self.name
        }









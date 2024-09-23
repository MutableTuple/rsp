from django.db import models
import uuid

# FoodItem

class FoodItem(models.Model):
    imageUrl = models.TextField(max_length=2000, null= True, blank=True)
    image = models.ImageField(default="https://royalspice.nl/wp-content/uploads/2021/11/Chicken-Tikka-Balti.webp", null=True, blank=True)
    name = models.CharField(max_length=450, null=True, blank=True)
    non_vegetarian = models.BooleanField(null=True,default=False)
    description = models.TextField(max_length=4500, null=True, blank=True)
    quantity = models.IntegerField(default= 1)
    added = models.DateTimeField(auto_now_add=True)
    energy = models.FloatField(null=True, blank=True)
    protien = models.FloatField(null=True, blank=True)
    fat = models.FloatField(null=True, blank=True)
    carbs = models.FloatField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    ingredients_added = models.ManyToManyField("Ingredients", null=True, blank=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.name


class Ingredients(models.Model):
    name=models.CharField(max_length=200, default="salt")
    def __str__(self):
        return self.name
    
class Drinks(models.Model):
    imageUrl = models.TextField(max_length=2000, null= True, blank=True)
    image = models.ImageField(default="https://royalspice.nl/wp-content/uploads/2021/11/Fernandes-Blauw.webp", null=True, blank=True)
    name = models.CharField(max_length=450, null=True, blank=True)
    description = models.TextField(max_length=4500, null=True, blank=True)
    quantity = models.IntegerField(default= 1)
    added = models.DateTimeField(auto_now_add=True)
    energy = models.FloatField(null=True, blank=True)
    protien = models.FloatField(null=True, blank=True)
    fat = models.FloatField(null=True, blank=True)
    sat_fat = models.FloatField(null=True, blank=True)
    carbs = models.FloatField(null=True, blank=True)
    sugars = models.FloatField(null=True, blank=True)
    sodium = models.FloatField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    ingredients_added = models.ManyToManyField("Ingredients", null=True, blank=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.name


    
class Desserts(models.Model):
    imageUrl = models.TextField(max_length=2000, null= True, blank=True)
    image = models.ImageField(default="https://royalspice.nl/wp-content/uploads/2021/11/Fernandes-Blauw.webp", null=True, blank=True)
    name = models.CharField(max_length=450, null=True, blank=True)
    description = models.TextField(max_length=4500, null=True, blank=True)
    quantity = models.IntegerField(default= 1)
    added = models.DateTimeField(auto_now_add=True)
    energy = models.FloatField(null=True, blank=True)
    protien = models.FloatField(null=True, blank=True)
    fat = models.FloatField(null=True, blank=True)
    sat_fat = models.FloatField(null=True, blank=True)
    carbs = models.FloatField(null=True, blank=True)
    sugars = models.FloatField(null=True, blank=True)
    sodium = models.FloatField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    ingredients_added = models.ManyToManyField("Ingredients", null=True, blank=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.name

class Sides(models.Model):
    imageUrl = models.TextField(max_length=2000, null= True, blank=True)
    image = models.ImageField(default="https://royalspice.nl/wp-content/uploads/2021/11/Fernandes-Blauw.webp", null=True, blank=True)
    name = models.CharField(max_length=450, null=True, blank=True)
    description = models.TextField(max_length=4500, null=True, blank=True)
    quantity = models.IntegerField(default= 1)
    added = models.DateTimeField(auto_now_add=True)
    energy = models.FloatField(null=True, blank=True)
    protien = models.FloatField(null=True, blank=True)
    fat = models.FloatField(null=True, blank=True)
    sat_fat = models.FloatField(null=True, blank=True)
    carbs = models.FloatField(null=True, blank=True)
    sugars = models.FloatField(null=True, blank=True)
    sodium = models.FloatField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    ingredients_added = models.ManyToManyField("Ingredients", null=True, blank=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.name

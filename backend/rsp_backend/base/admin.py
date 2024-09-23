from django.contrib import admin

from .models import FoodItem, Ingredients, Sides, Desserts, Drinks
# Register your models here.
admin.site.register(FoodItem)
admin.site.register(Ingredients)
admin.site.register(Sides)
admin.site.register(Desserts)
admin.site.register(Drinks)

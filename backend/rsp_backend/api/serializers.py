from rest_framework import serializers

from base.models import FoodItem, Ingredients, Sides, Desserts, Drinks


        
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model =Ingredients
        fields = "__all__"
        
class FoodItemSerializer(serializers.ModelSerializer):
    ingredients_added = IngredientSerializer(many = True)
    class Meta:
        model =FoodItem
        fields = "__all__"
        
class SidesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sides
        fields = "__all__"
        
class DessertsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desserts
        fields = "__all__"

class DrinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drinks
        fields = "__all__"
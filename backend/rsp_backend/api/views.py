# from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import FoodItemSerializer, SidesSerializer, DessertsSerializer, DrinksSerializer
from base.models import FoodItem, Sides, Desserts, Drinks

@api_view(['GET'])
# to use jwt
# @permission_classes([IsAuthenticated])

def getRoutes(request):
    routes=[
        {"GET":"/api/dishes"},
        {"GET":"/api/dishes/id"},
        {"GET":"/api/sides"},
        {"GET":"/api/sides/id"},
        
        # for auth
        {"POST":"/api/users/token"},
        {"POST":"/api/users/token/refresh"},
    ]
    return Response(routes)

@api_view(["GET"])
def getFoodItems(request):
    fooditems = FoodItem.objects.all()
    serializer = FoodItemSerializer(fooditems, many=True) #turns into json
    # return serialzied data
    return Response(serializer.data)

# single food items
@api_view(["GET"])
def getFoodItem(request,pk):
    fooditem = FoodItem.objects.get(id=pk)
    serializer = FoodItemSerializer(fooditem, many=False) #turns into json
    # return serialzied data
    return Response(serializer.data)

# post

@api_view(["POST"])
def editDishName(request,pk):
    dish = FoodItem.objects.get(id=pk)
    data = request.data
    print("DATA", data)
    # food_name, created = FoodItem.objects.get_or_create(name)
    # print(food_name)
    # # name.save()
    serializer = FoodItemSerializer(dish, many=False)
    return Response(serializer.data)
    
    
# sides
@api_view(["GET"])
def getSides(request):
    sides = Sides.objects.all()
    serializer = SidesSerializer(sides, many=True) #turns into json
    # return serialzied data
    return Response(serializer.data)


@api_view(["GET"])
def getDesserts(request):
    desserts = Desserts.objects.all()
    serializer = SidesSerializer(desserts, many=True) #turns into json
    # return serialzied data
    return Response(serializer.data)

@api_view(["GET"])
def getDrinks(request):
    drinks = Drinks.objects.all()
    serializer = SidesSerializer(drinks, many=True) #turns into json
    # return serialzied data
    return Response(serializer.data)
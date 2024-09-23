from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('', views.getRoutes),
    path('alldishes/', views.getFoodItems),
    path('sides/', views.getSides),
    path('drinks/', views.getDrinks),
    path('desserts/', views.getDesserts),
    path('dish/<str:pk>', views.getFoodItem),
    path('edit-dish/<str:pk>', views.editDishName),
    # auth
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

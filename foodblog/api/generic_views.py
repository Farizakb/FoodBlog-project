from multiprocessing import context
from django.http import JsonResponse
from blog.models import Recipe,Catagory
from .serializers import CatagoryRecipeSerializer, CatagorySerializer, RecipeCreateSerializer,RecipeReadCatagorySerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly,IsAdminUser


class GenericApiSerializer:
    
    def get_serializer_class(self):
        return self.serializer_classes[self.request.method]


class RecipeApiView(GenericApiSerializer,ListCreateAPIView):
    queryset = Recipe.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_classes = {
        "GET": RecipeReadCatagorySerializer,
        "POST": RecipeCreateSerializer,
        
    }
    
     
        
class RecipeReadUpdateDeleteView(GenericApiSerializer,RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_classes = {
        "GET": RecipeReadCatagorySerializer,
        "PUT": RecipeCreateSerializer,
        "PATCH": RecipeCreateSerializer,
    }
    
    
    
class CatagoryApiView(GenericApiSerializer,ListCreateAPIView):
    queryset = Catagory.objects.all()
    serializer_classes = {
        "GET": CatagoryRecipeSerializer,
        "POST": CatagorySerializer,
        
    }
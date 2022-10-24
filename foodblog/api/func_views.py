# from multiprocessing import context
# from django.http import JsonResponse
# from rest_framework.views import APIView
# from blog.models import Recipe,Catagory
# from .serializers import CatagoryRecipeSerializer, RecipeCreateSerializer,RecipeReadCatagorySerializer


# class RecipeApiView(APIView):
    
#     def get(self, request, *args, **kwargs):
#         recipes = Recipe.objects.all()
#         serializer = RecipeReadCatagorySerializer(recipes,context={'request':request} , many=True)
#         return JsonResponse(serializer.data ,safe = False)
    
#     def post(self, request, *args, **kwargs):
#         form_data = request.data
#         serializer = RecipeCreateSerializer(data = form_data,context={'request':request})
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data ,safe = False, status = 201)
#         return JsonResponse(serializer.errors ,safe = False , status = 400)
        
        
# class RecipeReadUpdateDeleteView(APIView):
    
#     def get(self, request, *args, **kwargs):
#         pass
    
#     def put(self, request, *args, **kwargs):
#         id = kwargs["pk"]
#         recipe = Recipe.objects.get(id=id)
#         recipe_data = request.data
#         serializer = RecipeCreateSerializer(data = recipe_data,  instance=recipe,context={'request':request})
#         serializer.is_valid(raise_exception = True)
#         serializer.save()
#         return JsonResponse(serializer.data, safe =False, status =200)
    
#     def patch(self, request, *args, **kwargs):
#         id = kwargs["pk"]
#         recipe = Recipe.objects.get(id=id)
#         recipe_data = request.data
#         serializer = RecipeCreateSerializer(data = recipe_data, partial = True, instance=recipe,context={'request':request})
#         serializer.is_valid(raise_exception = True)
#         serializer.save()
#         return JsonResponse(serializer.data, safe =False, status =200)
    
#     def delete(self, request, *args, **kwargs):
#         pass
    
    
    
# class CatagoryApiView(APIView):
    
#     def get(self, request, *args, **kwargs):
#         catagories = Catagory.objects.all()
#         serializer = CatagoryRecipeSerializer(catagories,context={'request':request} , many=True)
#         return JsonResponse(serializer.data ,safe = False)
    
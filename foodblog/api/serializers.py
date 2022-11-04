from rest_framework import serializers
from blog.models import Recipe, Catagory
from drf_yasg.utils import swagger_serializer_method




class RecipeCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
            'short_description',
            'description',
            'image',
            'tags',
            # 'author',
            'catagory',
            'created_at',
            'updated_at',
        )
    def validate(self, attrs):
        request = self.context['request']
        attrs['author'] = request.user
        return super().validate(attrs)



class CatagoryRecipeSerializer(serializers.ModelSerializer):
    recipes = serializers.SerializerMethodField()
    
    class Meta:
        model = Catagory
        fields =(
            'id',
            'title',
            'image',
            'recipes',
        ) 
    @swagger_serializer_method(serializer_or_field=RecipeCreateSerializer)
    def get_recipes(self,obj):
        serializer = RecipeCreateSerializer(obj.recipe.all(),context = self.context,many =True)
        return serializer.data 
    

        
class CatagorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Catagory
        fields =(
            'id',
            'title',
            'image',
        )
        
        
class RecipeReadCatagorySerializer(serializers.ModelSerializer):
    catagory = CatagorySerializer()
    
    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
            'short_description',
            'description',
            'image',
            'tags',
            'author',
            'catagory',
            'created_at',
            'updated_at',
        )
        
        



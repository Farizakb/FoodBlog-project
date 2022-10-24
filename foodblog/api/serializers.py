from rest_framework import serializers
from blog.models import Recipe, Catagory


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





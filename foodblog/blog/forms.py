from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model =Recipe
        fields = ('title', 'short_description','catagory','image','cover_image','tags',)
        
        # widgets = {
        #     "title": forms.TextInput(attrs={'placeholder': 'Title','class':'form-control'}),
        #     "short_description": forms.Textarea(attrs={'placeholder': 'short_description','class':'form-control'}),
        #     "catagory": forms.SelectMultiple(attrs={'placeholder': 'catagory','class':'form-control'}),
        #     "image": forms.FileInput(attrs={'placeholder': 'image','class':'form-control'}),
        #     "cover_image": forms.FileInput(attrs={'placeholder': 'cover_image','class':'form-control'}),
        #     "tags": forms.SelectMultiple(attrs={'placeholder': 'Title','class':'form-control'}),
        # }
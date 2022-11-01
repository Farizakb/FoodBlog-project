from django.shortcuts import HttpResponse, redirect, render,get_list_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic import ListView, DetailView, TemplateView, CreateView,UpdateView 
from django.utils.translation import gettext_lazy as _
# Create your views here.
from .models import Recipe, Catagory
from .forms import RecipeForm

class RecipeListView(ListView):
    model = Recipe
    paginate_by = 2
    context_object_name = "recipes"
    template_name = "blog/recipes.html"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query_cat = self.request.GET.get('cat')
        if query_cat:
            queryset =  queryset.filter(catagory = query_cat)
        return queryset
    
    

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'blog/recipe_det.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Catagory.objects.all()
        return context
    
    
    
class CreateRecipe(LoginRequiredMixin,CreateView):
    template_name = 'blog/create_recipe.html'
    form_class = RecipeForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self) -> str:
        messages.add_message(self.request,messages.SUCCESS, _("Yeni resept yaradildi"))
        return super().get_success_url()



class UpadateRecipe(UpdateView):
    model = Recipe
    template_name = 'blog/create_recipe.html'
    form_class = RecipeForm

    def get_success_url(self) -> str:
        messages.add_message(self.request,messages.SUCCESS, _("Yen resept yaradildi"))
        return super().get_success_url()
    




@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {
        "recipes":recipes
    }
    return render(request, 'blog/recipes.html',context)

@login_required
def stories_list(request):
    return render(request,'blog/stories.html')


@login_required
def like_recipe(request,id):
    request.session["liked_recipes"] = request.session.get("liked_recipes","") + str(id) + "," 
    messages.success(request,"Recipe like edildi")
    return redirect('recipes')




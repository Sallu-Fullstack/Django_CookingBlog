from django.shortcuts import render, redirect
from .models import Category, Recipe
from django.contrib import messages
import random


def homepage(request):
    limitNumber = 5
    categories = Category.objects.all()[:limitNumber]
    latest = Recipe.objects.all().order_by('-id')[:limitNumber]
    thai = Recipe.objects.filter(category='Thai')[:limitNumber]
    american = Recipe.objects.filter(category='American')[:limitNumber]
    chinese = Recipe.objects.filter(category='Chinese')[:limitNumber]
    food = {'latest': latest, 'thai': thai, 'american': american, 'chinese': chinese}
    context = {'title': 'Cooking Blog - Home', 'categories': categories, 'food': food}
    return render(request, 'index.html', context)

def exploreCategories(request):
    limitNumber = 20
    categories = Category.objects.all()[:limitNumber]
    context = {'title': 'Cooking Blog - Categories', 'categories': categories}
    return render(request, 'categories.html', context)

def exploreCategoriesById(request, id):
    limitNumber = 20
    categoryById = Recipe.objects.filter(category=id)[:limitNumber]
    context = {'title': 'Cooking Blog - Categories', 'categoryById': categoryById}
    return render(request, 'categories.html', context)

def exploreRecipe(request, id):
    recipe = Recipe.objects.get(id=id)
    context = {'title': 'Cooking Blog - Recipe', 'recipe': recipe}
    return render(request, 'recipe.html', context)

def searchRecipe(request):
    searchTerm = request.POST.get('searchTerm')
    recipe = Recipe.objects.filter(name__icontains=searchTerm)
    context = {'title': 'Cooking Blog - Search', 'recipe': recipe}
    return render(request, 'search.html', context)

def exploreLatest(request):
    limitNumber = 20
    latestRecipes = Recipe.objects.filter()[:limitNumber]
    context = {'title': 'Cooking Blog - Categories', 'latestRecipes': latestRecipes}
    return render(request, 'explore-latest.html', context)

def exploreLatest(request):
    limitNumber = 20
    latestRecipes = Recipe.objects.filter()[:limitNumber]
    context = {'title': 'Cooking Blog - Categories', 'latestRecipes': latestRecipes}
    return render(request, 'explore-latest.html', context)

# Displaying Random Recipes More with specific numbers.
# def exploreRandom(request):
#     try:
#         recipes = []
#         count = Recipe.objects.count()
#         limitNumber = 5
#         random_indices = random.sample(range(count), limitNumber)
#         for index in random_indices:
#             recipe = Recipe.objects.all()[index]
#             recipes.append(recipe)
#         return render(request, 'explore-random.html', {'title': 'Cooking Blog - Explore Latest', 'recipes': recipes})
#     except Exception as e:
#         error_message = str(e) or "Error Occurred"
#         return render(request, 'error.html', {'message': error_message})


def exploreRandom(request):
    try:
        count = Recipe.objects.count()
        random_index = random.randint(0, count - 1)
        recipe = Recipe.objects.all()[random_index]
        return render(request, 'explore-random.html', {'title': 'Cooking Blog - Explore Latest', 'recipe': recipe})
    except Exception as e:
        return render(request, 'error.html', {'message': e.message or "Error Occurred"})


def searchRecipe(request):
    try:
        search_term = request.POST.get('searchTerm', '')
        recipes = Recipe.objects.filter(name__icontains=search_term)
        return render(request, 'search.html', {'title': 'Cooking Blog - Search', 'recipes': recipes})
    except Exception as e:
        return render(request, 'error.html', {'message': str(e) or "Error Occurred"})



def submit_recipe(request):
    info_errors_obj = request.session.get('infoErrors')
    info_submit_obj = request.session.get('infoSubmit')
    return render(request, 'submit-recipe.html', {'title': 'Cooking Blog - Submit Recipe', 'infoErrorsObj': info_errors_obj, 'infoSubmitObj': info_submit_obj})

# Image Encripted Method Want to Explore More About it!
# def submit_recipe_on_post(request):
#     if request.method == "POST":
#         try:
#             if request.FILES:
#                 image_upload_file = request.FILES['image']
#                 new_image_name = str(datetime.now()) + image_upload_file.name
#                 upload_path = os.path.join(settings.MEDIA_ROOT, 'uploads', new_image_name)

#                 with open(upload_path, 'wb+') as destination:
#                     for chunk in image_upload_file.chunks():
#                         destination.write(chunk)

#             else:
#                 new_image_name = None

#             new_recipe = Recipe(
#                 name=request.POST.get('name'),
#                 description=request.POST.get('description'),
#                 email=request.POST.get('email'),
#                 ingredients=request.POST.get('ingredients'),
#                 category=request.POST.get('category'),
#                 image=new_image_name,
#             )
#             new_recipe.save()
#             messages.success(request, 'Recipe has been added.')
#             return redirect('submit_recipe')
#         except Exception as error:
#             messages.error(request, error)
#             return redirect('submit_recipe')
#     # return render(request, 'submit-recipe.html')

def create_recipe(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        email = request.POST.get('email')
        # ingredients_list = request.POST.get('ingredients')
        category = request.POST.get('category')
        image = request.FILES.get('image')

        ingredient_list = []
        for ingredient in request.POST.getlist('ingredients'):
            if ingredient.strip():
                ingredient_list.append(ingredient.strip())
        ingredients = ','.join(ingredient_list)

        recipe = Recipe(name=name, description=description, email=email, ingredients=ingredients,
                        category=category, image=image)
        recipe.save()

        return redirect('homepage')
    else:
        return render(request, 'submit-recipe.html')

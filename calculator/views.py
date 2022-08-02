from django.shortcuts import render, reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def home(request):
    template_name = 'calculator/home.html'
    pages = {
        'Показать рецепт омлета': reverse('omlet'),
        'Показать рецепт пасты': reverse('pasta'),
        'Показать рецепт бутерброда': reverse('buter'),
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def omlet(request):
    template_name = 'calculator/index.html'
    servings = int(request.GET.get('servings', 1))
    context = {
      'recipe': DATA['omlet'],
        'servings': servings
    }
    return render(request, template_name, context)

def pasta(request):
    template_name = 'calculator/index.html'
    servings = int(request.GET.get('servings', 1))
    context = {
      'recipe': DATA['pasta'],
        'servings': servings
    }
    return render(request, template_name, context)

def buter(request):
    template_name = 'calculator/index.html'
    servings = int(request.GET.get('servings', 1))
    context = {
      'recipe': DATA['buter'],
        'servings': servings
    }
    return render(request, template_name, context)


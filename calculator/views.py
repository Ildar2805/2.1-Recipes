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
    context = {
        'data': DATA
    }
    return render(request, template_name, context)


def dish(request, dish):
    template_name = 'calculator/index.html'
    servings = int(request.GET.get('servings', 1))
    data = {}
    for key, value in DATA[f'{dish}'].items():
        data[key] = value * servings
    context = {
      'recipe': data,
        'servings': servings
    }
    return render(request, template_name, context)




from django.shortcuts import render
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from string import ascii_uppercase
from MainApp.utils import flatten_list
from MainApp.models import Country, Languages


def render_main(request):
    return render(request, 'index.html')


def render_country_list(request):
    countries = Country.objects.all()
    paginator = Paginator(countries, per_page=25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'title': 'Countries',
        'alphabet': ' '.join(ascii_uppercase),
        'page_obj': page_obj
    }
    return render(request, 'country_list.html', context)


def render_country_by_name(request, name):
    # Надо переделать в ForeignKey
    item = Country.objects.get(name=name)
    languages = Languages.objects.filter(country=name)
    context = {
        'item': item,
        'languages': languages
    }
    return render(request, 'country.html', context)


def render_countries_by_first_letter(request, letter):
    countries = Country.objects.all()
    countries_by_letter = [i for i in countries if i.name[0].lower() == letter.lower()]
    context = {
        'letter': letter,
        'items': countries_by_letter
    }
    return render(request, 'countries_by_letter.html', context)


def render_countries_by_language(request, language):
    countries_by_language = Languages.objects.filter(name=language)
    return render(request, 'countries_by_language.html', {'items': countries_by_language})


def render_languages(request):
    languages = Languages.objects.all()
    languages = sorted(set([i.name for i in languages]))
    context = {
        'title': 'Languages',
        'items': languages
    }
    return render(request, 'languages.html', context)

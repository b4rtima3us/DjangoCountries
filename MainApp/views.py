import ast

from django.shortcuts import render
from MainApp.utils import flatten_list
from string import ascii_uppercase
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
with open(f'{BASE_DIR}/country_list.json', 'r', encoding='utf-8') as file:
    countries = ast.literal_eval(file.read())


def render_main(request):
    return render(request, 'index.html')


def render_country_list(request):
    context = {
        'title': 'Countries',
        'alphabet': ' '.join(ascii_uppercase),
        'countries': countries
    }
    return render(request, 'country_list.html', context)


def render_country_by_name(request, name):
    item = next((i for i in countries if i['country'] == name), None)
    if item:
        return render(request, 'country.html', {'item': item})


def render_countries_by_first_letter(request, letter):
    countries_by_letter = [i for i in countries if i['country'][0].lower() == letter.lower()]
    context = {
        'letter': letter,
        'countries': countries_by_letter
    }
    return render(request, 'countries_by_letter.html', context)


def render_countries_by_language(request, language):
    countries_by_language = [i for i in countries if language in i['languages']]
    context = {
        'language': language,
        'countries': countries_by_language
    }
    return render(request, 'countries_by_language.html', context)


def render_languages(request):
    languages = sorted(set(flatten_list([i['languages'] for i in countries])))
    context = {
        'title': 'Languages',
        'languages': languages
    }
    return render(request, 'languages.html', context)

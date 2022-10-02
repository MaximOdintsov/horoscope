from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
zodiac_dict = {
    'aries': "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).",
    'taurus': "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).",
    'gemini': "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
    'cancer': "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).",
    'leo': "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).",
    'virgo': "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
    'libra': "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
    'scorpio': "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
    'sagittarius': "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).",
    'capricorn': "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
    'aquarius': "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
    'pisces': "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)."
}

types_list = ['fire', 'earth', 'air', 'water']
types_dict = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}


def types_of_zodiac_sign(request, types):
    if types != 'types':  # проверка, правильно ли введен адрес
        return HttpResponseNotFound('Такой страницы не существует')

    type_elements = ''
    for type_element in types_list:
        link = reverse("types_sign_name", args=[types, type_element])
        type_elements += f'<li> <a href="{link}"> {type_element.title()} </a> </li>'

    response = f'''
    <ul>
        {type_elements}
    </ul>
    '''
    return HttpResponse(response)


def get_info_about_the_type_of_zodiac_sign(request, types, types_sign_zodiac):
    type_elements = types_dict.get(types_sign_zodiac)
    description_elements = ''
    for sign in type_elements:
        redirect_path = reverse("horoscope_name", args=[sign])
        description_elements += f'<li> <a href="{redirect_path}"> {sign.title()} </a> </li>'

    response = f'''
    <ul>
        {description_elements}
    </ul>
    '''
    return HttpResponse(response)


def index(request):
    zodiacs = list(zodiac_dict)
    li_elements = ''
    for sign in zodiacs:
        redirect_path = reverse("horoscope_name", args=[sign])
        li_elements += f'<li> <a href="{redirect_path}"> {sign.title()} </a> </li>'
    response = f'''
    <ol>
        {li_elements}
    </ol>    
    '''

    return HttpResponse(response)


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac, None)  # key = sign_zodiac

    if description:  # if the key is found, then this function is executed
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f'Такого знака зодиака - "{sign_zodiac}" не существует!')


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'Знака зодиака с порядковым номером {sign_zodiac} не существует :(')

    name_zodiac = zodiacs[sign_zodiac-1]
    redirect_url = reverse("horoscope_name", args=[name_zodiac])
    return HttpResponseRedirect(redirect_url)
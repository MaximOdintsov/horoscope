from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

import datetime

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

dates_dict = {
    'aries': ['3/21', '4/20'],
    'taurus': ['4/21', '5/21'],
    'gemini': ['5/22', '6/21'],
    'cancer': ['6/22', '7/22'],
    'leo': ['7/23', '8/21'],
    'virgo': ['8/22', '9/23'],
    'libra': ['9/24', '10/23'],
    'scorpio': ['10/24', '11/22'],
    'sagittarius': ['11/23', '12/22'],
    'capricorn': ['12/23', '1/20'],
    'aquarius': ['1/21', '2/19'],
    'pisces': ['2/20', '3/20'],
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

    redirect_path_for_types = reverse("types_name", args=['types'])
    types_zodiac = f'<h4> <a href="{redirect_path_for_types}"> Types of zodiac signs </a> </h4>'

    response = f'''
    <br> 
    <ol>
        {types_zodiac}
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


def date_input(date1, date2, date3):  # * - обязательный аргумент

    sign = None
    dt1 = datetime.datetime.strptime(date1, "%m/%d")
    dt2 = datetime.datetime.strptime(date2, "%m/%d")
    dt3 = datetime.datetime.strptime(date3, "%m/%d")
    if dt1 <= dt3 <= dt2:
        sign = True
    else:
        sign = False
    return sign


def get_info_by_date(request, month, day):
    if (1 <= month <= 12) and (1 <= day <= 31):
        for key in dates_dict:
            # print(key)
            description = dates_dict.get(key)

            date1 = description[0]
            date2 = description[1]

            sign = date_input(date1, date2, f'{month}/{day}')

            if sign == True:
                redirect_url = reverse("horoscope_name", args=[key])
                return HttpResponseRedirect(redirect_url)

        redirect_url = reverse("horoscope_name", args=['capricorn'])
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound('Неправильно введена дата!')
# print(date_init('3/10'))
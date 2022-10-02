from django.urls import path
from . import views  # . - это импорт из той же директории


# здесь создается конфигурация URL
urlpatterns = [
    path('', views.index),
    path('<int:month>/<int:day>', views.get_info_by_date),
    path('<str:types>/', views.types_of_zodiac_sign, name='types_name'),
    path('<str:types>/<str:types_sign_zodiac>', views.get_info_about_the_type_of_zodiac_sign, name='types_sign_name'),
    path('<int:sign_zodiac>', views.get_info_about_sign_zodiac_by_number),
    path('<str:sign_zodiac>', views.get_info_about_sign_zodiac, name='horoscope_name'),
]
import unittest
from django.test import TestCase
from django.urls import reverse

from .models import Quiz

# для запуска определенного тест пишем
# python manage.py test путь_к_файлу
# например python manage.py test quizes.tests

# setUpTestData() вызывается каждый раз перед запуском теста на уровне
# настройки всего класса. Вы должны использовать данный метод для создания
# объектов, которые не будут модифицироваться/изменяться в каком-либо из
# тестовых методов.

class QuizModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Quiz.objects.create(name='Умножение', topic='Математика',
                            number_of_questions=3,
                            time=3, required_to_pass=60,
                            difficulty='легко')
#     тут мы создаем тестовую запись для модели

    def test_name_quiz(self):
        name_quiz = Quiz.objects.get(id=1)
        name_verbose_name = name_quiz._meta.get_field('name').verbose_name
        name_max_lenght = name_quiz._meta.get_field('name').max_length
        print(name_verbose_name)
        print(name_max_lenght)
        print('****************************')
        self.assertEqual(name_verbose_name, 'Название')
        self.assertEqual(name_max_lenght, 120)

    def test_quiz_get_absolute_url(self):
        quiz = Quiz.objects.get(id=1)
#     просто проверка получения записи

    def test_urls(self):
        response = self.client.get('')
        response_2 = self.client.get('/1/')
        response_3 = self.client.get('/1/data/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_2.status_code, 200)
        self.assertEqual(response_3.status_code, 200)

        print(list(response.template_name)[0])

        print(response.status_code)
        print('*******', response_2.status_code)
        print('*******', response_3.status_code)




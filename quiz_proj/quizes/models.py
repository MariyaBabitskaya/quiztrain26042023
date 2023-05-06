from django.db import models
import random

from django.core.exceptions import ValidationError
import re

DIFF_CHOICES = (
    ('легко', 'легко'),
    ('средне', 'средне'),
    ('тяжело', 'тяжело')
)

def validate_topic(value):
    txt = re.findall(r'[а-яА-ЯёЁ]', value)
    if len(value) != len(txt):
        raise ValidationError('Вводите только русские буквы')
    if value[0] != value[0].upper():
        raise ValidationError('Введите название с большой буквы')

def validate_name(val):
    txt = re.findall(r'[^a-zA-Z]', val)
    if len(val) != len(txt):
        raise ValidationError('Не используйте латинские буквы')

class Quiz(models.Model):
    name = models.CharField(max_length=120, verbose_name='Название', validators=[validate_name])
    topic = models.CharField(max_length=120, verbose_name='Тема квиза', validators=[validate_topic])
    number_of_questions = models.IntegerField(verbose_name='Количество вопросов')
    time = models.IntegerField(help_text='длительность в минутах', verbose_name='Время выполнения')
    #параметр в скобках это текст подсказка рядом с полем
    required_to_pass = models.IntegerField(help_text='верность в %', verbose_name='Процент прохождения')
    difficulty = models.CharField(max_length=6, choices=DIFF_CHOICES, verbose_name='Сложность')

    def __str__(self):
        return f'{self.name} -- {self.topic}'

    # это первый вариант
    # def get_questions(self):
    #     return self.question_set.all()[:self.number_of_questions]
    #здесь тоже связь с моделью, в данном случае Question,
    #благодаря связи ворен кей в данный файл импорт не нужен
    #напоминание, что перед сет это имя вторичной модели
    #здесь ограничение вывода вопросов количеством вопросов

    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        # функция shuffle перемешивает порядок последовательности
        return questions[:self.number_of_questions]
# допустим мы задали число вопросов 3, а вопросов прописано 4
#     на странице будут выводиться рандомно 3 вопроса

    class Meta:
        verbose_name = 'Квиз'
        verbose_name_plural = 'Квизы'
from django.core.exceptions import ValidationError
import re

def validate_topic(value):
    if value != '[a-zA-Zа-яА-ЯёЁ]+':
        raise ValidationError('Вводите только русские буквы')
from django.db import models
from quizes.models import Quiz
from django.contrib.auth.models import User


class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name='Квиз')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    score = models.FloatField(verbose_name='Процент выполнения')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.pk} - {self.user} - {self.quiz} - {self.created_at}'

    class Meta:
        verbose_name = 'Результаты'
        verbose_name_plural = 'Результаты'
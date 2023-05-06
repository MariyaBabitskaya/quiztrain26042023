from django.db import models
from quizes.models import Quiz


class Question(models.Model):
    text = models.CharField(max_length=200, verbose_name='Текст вопроса')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name='Выберите квиз')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()
    #таким образов мы прокладываем связь к модели
    #лучше использовать этот способ
        # return self.answers.all()
    #это уже связь с полем Answer-question по его парметру
    #related name которое answers

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    text = models.CharField(max_length=200, verbose_name='Текст ответа')
    correct_field = models.BooleanField(default=False, verbose_name='Верно или не верно')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Выберите вопрос')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Вопрос:  {self.question.text}, ответ:  {self.text}, верность: {self.correct_field}"

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
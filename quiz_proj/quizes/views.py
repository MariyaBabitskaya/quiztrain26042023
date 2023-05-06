from django.http import JsonResponse
from django.shortcuts import render

from questions.models import Question, Answer
from .models import Quiz
from django.views.generic import ListView
from results.models import Result


class QuizListView(ListView):
    model = Quiz
    template_name = 'quizes/main.html'


def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'quizes/quiz.html', {'obj': quiz})
#здесь делаем ключ, отсылающий на объекты из переменной quiz

def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })



def save_quiz_view(request, pk):
    # print(request.POST)
    # так мы сможем посмотреть в PyCharm данные что мы отсылаем
    # будет словарь QueryDict
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
# ранее можно было написать request.is_ajax то есть это нас отсылает к коду
# в js, но на данный момент метод устарел и выбивает ошибку
        questions = []
        data = request.POST
        data_ = dict(data.lists())
        data_.pop('csrfmiddlewaretoken')
    #тут мы превращаем QueryDict в обычный словарь
        for k in data_.keys():
            question = Question.objects.get(text=k)
            questions.append(question)
        print(questions)
        # тут мы имеем все вопросы

        user = request.user
        # мы получаем имя юзера кто проходит квиз
        quiz = Quiz.objects.get(pk=pk)

        score = 0
        multiplier = 100 / quiz.number_of_questions
        results = []
        correct_answer = None

        for q in questions:
            a_selected = request.POST.get(q.text)
    #   таким вот образом мы из пары из словаря по ключу получаем
    # выбранный ответ
    #         print(a_selected) --> в консоль выведется ответ
            if a_selected != '': #то есть не пустой ответ
                question_answers = Answer.objects.filter(question=q)
                # здесь все ответы на конкретный вопрос
                for a in question_answers:
                    if a.correct_field:
                        score += 1
                        correct_answer = a.text
                    # else:
                    #     correct_answer = a.text
                    # if a_selected == a.text:
                    #     if a.correct_field: #то есть если ответ верный
                    #         score += 1
                    #         correct_answer = a.text
                    #     else:
                    #         if a.correct_field:
                    #             correct_answer = a.text

                results.append({str(q): {'correct_answer': correct_answer,
                                             'answered': a_selected}})
            else:
                results.append({str(q): 'Нет ответа'})

        score_ = score * multiplier
        Result.objects.create(quiz=quiz, user=user, score=score_)

        if score_ >= quiz.required_to_pass:
            return JsonResponse({'passed': True, 'score': score_,
                                 'results': results})
        else:
            return JsonResponse({'passed': False, 'score': score_,
                                 'results': results})
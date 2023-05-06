from django.urls import path
from .views import (
      QuizListView,
    quiz_view,
    quiz_data_view,
     save_quiz_view
)

app_name = 'quizes'
#если много приложений то такой аргумент очень полезен
#то есть это имя можно использовать в других файлах

urlpatterns = [
    path('', QuizListView.as_view(), name='main-view'),
    path('<pk>/', quiz_view, name='quiz-view'),
    path('<pk>/data/', quiz_data_view, name='quiz-data-view'),
    path('<pk>/save/', save_quiz_view, name='quiz-save-view'),
]
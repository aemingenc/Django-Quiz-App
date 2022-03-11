
from django.urls import path,include
from .views import QuizRead,QuizList,QuestionRead
urlpatterns = [
    
    path("",QuizList.as_view(),name="quiz_list"),
   
    path("<category>/" ,QuizRead.as_view(),name="quiz_read"),
    path("<category>/<quiz>/" ,QuestionRead.as_view(),name="quuestion_read")
]

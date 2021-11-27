from django.urls import path
from . import views

urlpatterns = [
    path('category/',views.CategoryApiView.as_view()),
    path('choices/',views.ChoiceApiView.as_view()),

    #question filtering by category, id, all
    path('questions/',views.QuestionApiView.as_view()),
    path('questions/category/<int:id>',views.QuestionCategory.as_view()),
    path('questions/<int:pk>',views.QuestionDetial.as_view()),

    #quiz filtering: id, category, all
    path('quizzes/',views.QuizApiView.as_view()),
    path('quizzes/category/<int:id>',views.QuizCategoryApi.as_view()),
    path('quizzes/<int:pk>',views.QuizDetail.as_view()),
]

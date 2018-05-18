from django.urls import path

from . import views

urlpatterns = [
    path('ask/<int:question_id>/', views.ask_question, name='ask question'),
    path('ask/<int:question_id>/answer/<int:answer_id>', views.answer_question, name='answer question'),
]
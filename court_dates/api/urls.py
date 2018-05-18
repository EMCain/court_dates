from django.urls import path

from . import views

urlpatterns = [
    path('ask/<int:question_id>/', views.ask_question),
    path('ask/<int:question_id>/answer/<int:response_id>', views.answer_question),
]
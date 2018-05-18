import json

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, reverse

from .models import Answer, Question
# Create your views here.

def ask_question(request, question_id):
    # TODO look up info 
    data = json.dumps({
        'question': 'this will be question text',
        'answers': ['yes', 'no']
    })
    return HttpResponse(data)

def answer_question(request, question_id, answer_id):
    # TODO specify POST???

    current_question = get_object_or_404(Question, id=question_id)
    answer = get_object_or_404(Answer, id=answer_id)
    next_question = current_question.respond(answer)
    next_url = reverse('ask question', kwargs={'question_id': next_question.id})
    data = json.dumps({
        'next': next_url
    })
    return HttpResponse(data)

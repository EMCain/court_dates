import json

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, reverse

from .models import Answer, Question
# Create your views here.

def ask_question(request, question_id):
    # TODO look up info 
    question = get_object_or_404(Question, id=question_id)

    data = json.dumps({
        'question': question.text,
        'answers': {a.id: a.text for a in question.answers.all()}
    })
    return HttpResponse(data)

def answer_question(request, question_id, answer_id):
    # TODO specify POST???
    # if there's a post this can be stateful (answers assigned to user) 

    current_question = get_object_or_404(Question, id=question_id)
    answer = get_object_or_404(Answer, id=answer_id)
    next_question = current_question.respond(answer)
    next_url = reverse('ask question', kwargs={'question_id': next_question.id})
    data = json.dumps({
        'next': next_url
    })
    return HttpResponse(data)

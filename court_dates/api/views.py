import json

from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def ask_question(request, question_id):
    # TODO look up info 
    data = json.dumps({
        'question': 'this will be question text',
        'answers': ['yes', 'no']
    })
    return HttpResponse(data)

def answer_question(request, question_id, response_id):
    # TODO specify POST???

    data = json.dumps({
        'next': 'path_to_next_url'
    })
    return HttpResponse(data)

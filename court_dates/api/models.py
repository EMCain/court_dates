from django.db import models

# Create your models here.

class Question(models.Model):
    text = models.TextField(max_length=255)

    def ask(self):
        return {
            'text': self.text,
            'options': [response.text for response in self.responses.all()]
        }

    def answer(self, response):
        if response in self.responses.all(): 
            return response.next_question
        else:
            raise ValueError('response does not belong to this question')
    

class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='responses')
    text = models.TextField(max_length=255)
    next_question = models.ForeignKey(Question, null=True, on_delete=models.CASCADE, related_name='parent_responses')
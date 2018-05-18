from django.db import models

# Create your models here.

class Question(models.Model):
    text = models.TextField(max_length=255)

    def ask(self):
        return {
            'text': self.text,
            'options': [answer.text for answer in self.answers.all()]
        }

    def respond(self, answer):
        if answer in self.answers.all(): 
            return answer.next_question
        else:
            raise ValueError('answer does not belong to this question')
    

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.TextField(max_length=255)
    next_question = models.ForeignKey(Question, null=True, on_delete=models.CASCADE, related_name='parent_answers')
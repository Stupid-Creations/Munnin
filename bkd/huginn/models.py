from django.db import models

class Question(models.Model):
    question = models.CharField(max_length = 1000)
    def __str__(self):
        return self.question

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    answer = models.CharField(max_length = 10000)
    def __str__(self):
        return self.answer


# import datetime
# from django.db import models
# from django.utils import timezone


# class OracleQuestion(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')

#     def __str__(self) -> str:
#         return self.question_text

# class OracleAnswer(models.Model):
#     oracle = models.ForeignKey(OracleQuestion, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     choice_text = models.CharField(max_length=200)
#     choice_text = models.CharField(max_length=200)
#     choice_text = models.CharField(max_length=200)
#     choice_text = models.CharField(max_length=200)
#     choice_text = models.CharField(max_length=200)

#     def __str__(self) -> str:
#         return self.choice_text

from django.db import models
import random
from django.urls import path

class OracleQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self) -> str:
        return self.question_text

class OracleAnswer(models.Model):
    oracle = models.ForeignKey(OracleQuestion, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)
    roll_value = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text
    
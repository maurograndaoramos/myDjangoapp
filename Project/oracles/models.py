from django.db import models

class OracleQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    category = models.CharField(max_length=200, default='General')
    description = models.TextField(blank=True)
    die = models.CharField(max_length=6, default='d20')

    def __str__(self) -> str:
        return self.question_text

class OracleAnswer(models.Model):
    oracle = models.ForeignKey(OracleQuestion, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)
    roll_value = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text
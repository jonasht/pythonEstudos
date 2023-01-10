from datetime import datetime
from time import timezone
from django.db import models

# Create your models here.
class Question(models.Model):
    # tem que ser no maximo 200 caracteres
    question_text = models.CharField(max_length=200)

    # data de PUBlicaçao
    pub_date = models.DateField('date published')

    def __str__(self) -> str:
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now()-datetime.datetime(day=1)
        
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.choice_text
    


    
 
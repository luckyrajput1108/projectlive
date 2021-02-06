# import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
        
#movie models are here
class MovieInfo(models.Model):
    Movie=models.CharField(max_length=100)
    Release_Year=models.DateTimeField(auto_now_add= True)
    Actor=models.CharField(max_length=50, help_text="add Hero/Actress name")

class LoginForm(models.Model):
    name=models.CharField(max_length=100)


class Review(models.Model):
    RATING_RANGE = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
        )
    rating = models.IntegerField(choices=RATING_RANGE,)

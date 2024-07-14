from django.db import models

# Create your models here.

# the Question class is a child-class of Model class (inheritance)
class Question(models.Model):

    # Automatically creates a primary key`id` field
    question_text = models.CharField(max_length=200)
    published_date = models.DateTimeField('Date Published')

    def __str__(self):
        return self.question_text
    
class Choice(models.Model):

    # cascade means that if a question gets deleted, the choice also gets deleted
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    




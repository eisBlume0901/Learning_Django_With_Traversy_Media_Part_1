from django.shortcuts import render

from .models import Question, Choice
# Create your views here.

# Get questions and display it for the user
def index(request):
    # Same with Laravel's Eloquent ORM which is used to query the database
    # In Laravel, it is like Question::latest('published_date')->get();
    # This is Django's ORM
    # - means descending order
    # [:5] means get the first 5 items only
    latest_question_list = Question.objects.order_by('-published_date')[:5]
    context = {'latest_question_list': latest_question_list}
    # The data is stored in the variable named context and then render it to the index.html file
    return render(request, 'polls/index.html', context)


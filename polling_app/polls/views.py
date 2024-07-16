from django.http import Http404
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


# Show specific question and choices
def detail(request, question_id):

    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

# Laravel counterpart
# public function show($id) {
#     $question = Question::find($id);
#     return view('polls.detail', compact('question'));
# }


# Get question and display results
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def get_object_or_404(Question, pk):
    try:
        return Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

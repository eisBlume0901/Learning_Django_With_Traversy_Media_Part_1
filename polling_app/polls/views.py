from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

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


def vote(request, question_id):
    print(request.POST['choice'])
    question = get_object_or_404(Question, pk=question_id)
    try:
        # request.POST is a dictionary-like object that lets you access submitted data by key name
        # request.POST['choice'] returns the ID of the selected choice as a string
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing with POST data.
        # This prevents data from being posted twice if a user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))



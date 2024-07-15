from django.contrib import admin
from .models import Question, Choice

admin.site.site_header = "Polling App Admin" #
admin.site.site_title = "Welcome to Polling App's Admin Area" # In Laravel, it is the header
admin.site.index_title = "Admin page"  # In Laravel, it is called @section('content') in the layout file
# Register your models here.

# TabularInline is a class that allows you to edit the choices on the same page as the question
# It is an automatic HTML table creator
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['published_date'], 'classes': 
                                       ['collapse']}),]  
    inlines = [ChoiceInline]

# This registers the Question and Choice models with the admin site
# Look at http://localhost:8000/admin/ to see the models
# admin.site.register(Question)
# admin.site.register(Choice)

# This one makes a relationship between the Question and Choice models
# A question can have many choices
admin.site.register(Question, QuestionAdmin)
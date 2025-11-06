from django.shortcuts import render

from myApp.models import TodoModel

# Create your views here.

#get the list of todos
def view_todo(request):
    todos = TodoModel.objects.all() #get all todos
    return render(request, "view_todo.html", {"todos": todos},)

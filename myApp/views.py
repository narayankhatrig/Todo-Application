from django.shortcuts import render
from django.http import HttpResponseRedirect

from myApp.models import TodoModel

# Create your views here.

#get the list of todos
def view_todo(request):
    todos = TodoModel.objects.all() #get all todos
    return render(request, "view_todo.html", {"todos": todos},)

#create the todos
def add_todo(request):
    #print(request.method, request.POST)
    if request.method == "GET":
        return render(request, "add_todo.html")
    else:
        TodoModel.objects.create(title=request.POST["title"], details=request.POST["details"])
        return HttpResponseRedirect("/") #takes to homepage
    
#delete todos
def delete_todo(request, pk):
    todo = TodoModel.objects.get(id=pk)
    todo.delete()
    return HttpResponseRedirect("/") #homepage

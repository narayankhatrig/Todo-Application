from django.shortcuts import render
from django.http import HttpResponseRedirect

from myApp.models import TodoModel

# Create your views here.

#get the list of todos
def view_todo(request):
    todos = TodoModel.objects.all() #get all todos
    return render(request, "css/view_todo.html", {"todos": todos},)

#create the todos
def add_todo(request):
    #print(request.method, request.POST)
    if request.method == "GET":
        return render(request, "css/add_todo.html")
    else:
        TodoModel.objects.create(title=request.POST["title"], details=request.POST["details"])
        return HttpResponseRedirect("/") #takes to homepage
    
#update todos
def update_todo(request, pk):
    if request.method == "GET":
        todo = TodoModel.objects.get(id=pk)
        return render(request, "css/update_todo.html", {"todo": todo},)
    else:
        todo = TodoModel.objects.get(id=pk)
        todo.title = request.POST["title"]
        todo.details = request.POST["details"]
        todo.save()
        return HttpResponseRedirect("/") #home
    
#delete todos
def delete_todo(request, pk):
    todo = TodoModel.objects.get(id=pk)
    todo.delete()
    return HttpResponseRedirect("/") #homepage


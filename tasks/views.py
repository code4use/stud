# from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic.list import ListView
from tasks.models import Task
# Create your views here.


class TaskListView(ListView):
    model = Task



# def index(request):
#    return HttpResponse("Hello, world. You're at the tasks index")


# def detail(request, task_id):
#    return HttpResponse("Это задание %s." % task_id)

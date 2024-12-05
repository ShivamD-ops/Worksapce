"""
Created by -> SHIVAM DEVASER
on-> 05-12-2024

this file changes->
added views for ->
1) create
2) read
3) update
4) delete
"""
from django.shortcuts import render,get_object_or_404
from .models import Task
from .forms import TaskForm
from django.http import HttpResponse,HttpResponseRedirect


def create_new_task(request):
    # 1-> fetch all tasks to display
    # 2-> get instance of form and render form
    # 3-> on submission if form is valid save to db
    # 4-> send context to front-end

    context = {}
    context['all_tasks'] = Task.objects.all()

    create_task_form = TaskForm(request.POST or None)
    if create_task_form.is_valid():
        create_task_form.save()
        return HttpResponseRedirect("/")
    context['create_task_form'] = create_task_form

    return render(request,"all_tasks_list.html",context)

def all_task_list(request):
    # 1-> fetch all tasks to display
    # 2-> send context to front-end
    context = {}
    context['all_tasks'] = Task.objects.all()

    return render(request,"all_tasks_list.html",context)

def task_detail_view(request,id):
    # 1-> fetch all task to display by id
    # 4-> send context to front-end
    context = {}
    context['task_data'] = Task.objects.get(id = id)
    print(context)
    return render(request,'task_detail.html',context)

def task_update_view(request,id):
    # 1-> fetch all tasks to display
    # 2-> get instance of form with id of perticular task
    # 3-> on submission if form is valid save to db
    # 4-> send context to front-end
    context = {}
    context['all_tasks'] = Task.objects.all()

    obj = get_object_or_404(Task,id = id)
    update_task_form = TaskForm(request.POST or None, instance = obj)
    if update_task_form.is_valid():
        update_task_form.save()
        return HttpResponseRedirect("/")
    context['update_task_form'] = update_task_form

    return render(request,'all_tasks_list.html',context)

def task_delete_view(request,id):
    # Delete the tasks
    context = {}
    obj = get_object_or_404(Task,id = id)

    obj.delete()
    return HttpResponseRedirect("/")
# Create your views here.

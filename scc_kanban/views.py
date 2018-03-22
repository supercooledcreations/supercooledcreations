# Import
# Django
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render, reverse
from django.views import View

# App
from .forms import AddTaskForm, UpdateTaskForm
from .models import Task

# Views
class TaskListView(View):

    def get(self, request, *args, **kwargs):
        template_name = 'scc_kanban/task_list.html'

        add_task_form = AddTaskForm()

        tasks = Task.objects.filter(user=request.user, parent_task=None).exclude(status__in=['outerspace', 'bin']).order_by('status')

        task_list = []
        for task in tasks:
            task_row = {'object': task, 'form': UpdateTaskForm(instance=task)}
            task_list.append(task_row)

        context = {'add_task_form': add_task_form, 'task_list': task_list}

        return render(request, template_name, context)

    def post(self, request, *args, **kwargs):

        success_redirect = HttpResponseRedirect(reverse('scc_kanban:task_list'))

        if request.POST['action'] == 'add_task':
            form = AddTaskForm(request.POST or None)

            if form.is_valid:
                form.instance.user = request.user
                form.instance.status = 'board'
                form.save()

        elif request.POST['action'] == 'update_task' and request.POST['task_id']:
            task = Task.objects.get(id=request.POST['task_id'])
            form = UpdateTaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return success_redirect

        else:
            return HttpResponseBadRequest('Request Action not Recognized')

        return success_redirect

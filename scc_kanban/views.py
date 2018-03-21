# Import
# Django
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.views import View

# App
from .forms import TaskForm
from .models import Task

# Views
class TaskListView(View):

    def get(self, request, *args, **kwargs):
        template_name = 'scc_kanban/task_list.html'

        add_task_form = TaskForm()

        task_list = Task.objects.filter(user=request.user, parent_task=None)

        context = {'add_task_form': add_task_form, 'task_list': task_list}

        return render(request, template_name, context)

    def post(self, request, *args, **kwargs):

        form = TaskForm(request.POST or None)
        if form.is_valid:
            form.instance.user = request.user
            form.instance.status = 'board'
            form.save()

        return HttpResponseRedirect(reverse('scc_kanban:task_list'))

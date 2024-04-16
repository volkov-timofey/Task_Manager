from django.forms import ModelForm

from task_manager.tasks.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'describe', 'status', 'executor', 'label']

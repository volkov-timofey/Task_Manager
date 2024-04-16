from django_filters import FilterSet, BooleanFilter, ChoiceFilter

from django.forms import CheckboxInput
from django.utils.translation import gettext_lazy as _

from task_manager.tasks.models import Task
from task_manager.labels.models import Label


class TaskFilter(FilterSet):
    my_tasks = BooleanFilter(widget=CheckboxInput,
                             method='filter_creator',
                             label=_('Только свои задачи'))

    def filter_creator(self, queryset, *args, **kwargs):
        is_my_tasks = args[-1]
        if is_my_tasks:
            creator = getattr(self.request, 'user', None)
            return queryset.filter(creator=creator)
        return queryset
        
    labels = [(label.id, label.name) for label in Label.objects.all()]
    
    label = ChoiceFilter(
        choices=labels,
        field_name='label',
        label=_('Метка'),
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'label', 'my_tasks']

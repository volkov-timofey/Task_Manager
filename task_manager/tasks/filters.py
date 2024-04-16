from django_filters import FilterSet, BooleanFilter, ModelChoiceFilter

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
    '''  
    label = ChoiceFilter(
        choices=[(label.id, label.name) for label in Label.objects.all()],
        field_name='labels',
        label=_('Метка'),
    )
    '''
    label = ModelChoiceFilter(
        queryset=Label.objects.all(),
        label=_('Метка'),
        field_name='label',
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'label', 'my_tasks']

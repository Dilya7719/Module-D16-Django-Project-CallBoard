from django_filters import FilterSet, ChoiceFilter, DateTimeFilter, CharFilter
from .models import Call, Respond
from django.forms import DateTimeInput


class CallFilter(FilterSet):
    call_header = CharFilter(
        field_name='call_header',
        lookup_expr='icontains',
        label='Поиск по словам в заголовке',
    )

    call_category = ChoiceFilter(
        choices=Call.CATEGORIES_LIST,
        field_name='call_category',
        label='Категория',
        empty_label='Любая',
    )

    call_create_date = DateTimeFilter(
        field_name='call_create_date',
        lookup_expr='gt',
        label='Позже даты',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )


class CallFilterForResponds(FilterSet):
    class Meta:
        model = Respond
        fields = ["respond_call", ]

    def __init__(self, *args, **kwargs):
        super(CallFilterForResponds, self).__init__(*args, **kwargs)
        self.filters['respond_call'].queryset = Call.objects.filter(call_author_id=kwargs['request'])
        self.filters['respond_call'].label = 'Выберите объявление'
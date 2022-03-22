import django_filters
from django.db.models.fields import DateField
from django_filters import CharFilter, DateFilter
from django_filters.filters import ChoiceFilter

from .models import *


class OrderFilter(django_filters.FilterSet):
    # #filtering with date
    # start_date = DateFilter(field_name ="date_created",lookup_expr='gte')
    # end_date = DateFilter(field_name ="date_created",lookup_expr='lte')
    note = CharFilter(field_name="note",lookup_expr='icontains')
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer','date_created']

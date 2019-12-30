from django_filters import FilterSet, DateFromToRangeFilter
from django_filters.widgets import RangeWidget

from api.models import Movie


class DateFilter(FilterSet):
    created_at = DateFromToRangeFilter(widget=RangeWidget(attrs={'type': 'date'}))

    class Meta:
        model = Movie
        fields = ['created_at']

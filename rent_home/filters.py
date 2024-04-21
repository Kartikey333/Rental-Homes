import django_filters as filters
from django_filters import FilterSet

from rent_home.models import Room, RoomType, House, Property_Type, Budget_Range, Area
from django import forms

class RoomFilter(filters.FilterSet):

    budget_range = filters.ModelMultipleChoiceFilter(
        field_name = "budget_range",
        queryset = Budget_Range.objects.all(),
        widget = forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Room
        fields = ["room_type","furnished","available","budget_range","room_for"]

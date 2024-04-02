import django_filters
from .models import *
from django_filters import CharFilter

class Apparelfilter(django_filters.FilterSet):
    category = CharFilter(field_name='category', lookup_expr='icontains')
    subcategory = CharFilter(field_name='subcategory', lookup_expr='icontains')
    designer = CharFilter(field_name='designer', lookup_expr='icontains')
    label = CharFilter(field_name='label', lookup_expr='icontains')
    color_subcategory = CharFilter(field_name='color_subcategory', lookup_expr='icontains')
    basic_color = CharFilter(field_name='basic_color', lookup_expr='icontains')
    material = CharFilter(field_name='material', lookup_expr='icontains')
    
    class Meta:
        model = Apparel
        fields = ['category', 'subcategory', 'designer', 'label', 'color_subcategory', 'basic_color', 'material']
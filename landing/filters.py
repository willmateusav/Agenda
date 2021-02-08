import django_filters
from django import forms
from .models import appointment

class appointmentFilter(django_filters.FilterSet):

    HOUR = (
        ('', 'Seleccione horario'),
        ('9-10', '9-10'),
        ('10-11', '10-11'),
        ('11-12', '11-12'),
        ('12-13', '12-13'),
        ('14-15', '14-15'),
        ('15-16', '15-16'),
        ('16-17', '16-17'),
        ('17-18', '17-18'),
        ('18-19', '18-19'),
    )

    DAY = (
        ('', 'Seleccione horario'),
        ('23 de febrero', '23 de febrero'),
        ('24 de febrero', '24 de febrero'),
    )

    first_name = django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Buscar nombre que contenga', 'size':30,}))
    email = django_filters.CharFilter(lookup_expr='icontains', widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Buscar email', 'size':30,}))
    date = django_filters.ChoiceFilter(choices=DAY, widget=forms.Select(attrs={'class': 'form-control'}))
    hour = django_filters.ChoiceFilter(choices=HOUR, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = appointment
        fields = '__all__'
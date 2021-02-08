from django import forms
from .models import appointment
from crispy_forms.helper import FormHelper # Crispy form
from crispy_forms.layout import Layout, Submit, Row, Column, Div, Field, MultiField, HTML# Crispy form
from crispy_forms.bootstrap import InlineRadios, InlineCheckboxes
from datetime import datetime # DATE

from django.forms.widgets import CheckboxSelectMultiple

from django.core.exceptions import ValidationError

class AppointmentForm(forms.ModelForm):

    error_css_class = 'error' # Style, red color in validation error
    required_css_class = "required" # Style

    # date = forms.ChoiceField(
    #     label="Día asistencia al evento",
    #     choices=(("23 de febrero", "23 de febrero"), ("24 de febrero", "24 de febrero")),
    #     widget=forms.RadioSelect,
    #     widget=CheckboxSelectMultiple(),
    #     required=True,
    # )

    all_is_accurate = forms.BooleanField(required=False,
                                      initial=False,
                                      label='Aceptas nuestra política de datos')

    def clean_email(self):
       first_name = self.cleaned_data.get("email", "")
       Email = ["willmateusav@gmail.com", "mir.do@hotmail.com", "jtrochez@gmail.com"]
       #for email in Email:
       if first_name not in Email:
            raise ValidationError("Correo electrónico no permitido.")
            #else
       return first_name

    class Meta:
        model = appointment
        fields = ['first_name', 'email', 'date', 'hour', 'all_is_accurate']
        labels = {
            'first_name': 'Nombre Completo',
            'email': 'Correo Electrónico',
            'date': 'Día asistencia al evento',
            'hour': 'Hora de ingreso',
            #'all_is_accurate': 'Sus datos personales han sido y están siendo tratados conforme a nuestra Política de Tratamiento de Datos Personales, marcando la casilla de verificación acepta nuestra política.'
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['email'].required = True
        self.fields['date'].required = True
        self.fields['hour'].requires = True
        self.fields['all_is_accurate'].requires = True
        self.fields['all_is_accurate'].label = "Sus datos personales han sido y están siendo tratados conforme a nuestra Política de Tratamiento de Datos Personales, marcando la casilla de verificación acepta nuestra política. Consulte nuestra Política de Tratamiento Datos, aquí."
        self.helper = FormHelper()
        self.helper.form_method = 'post' # get or post
        self.helper.layout = Layout(

                HTML("<center><img src='static/img/logo-260-wwe.png' width='150px' height='110px'></center>"),
                HTML("<br>"),
                HTML("<img src='static/img/awekinings.png' width='80%' height='50%'>"),
                HTML("<br>"),
                HTML("<br>"),

                Div(
                    Div(
                        Field('first_name', data_name="first_name", placeholder="Nombres y apellidos", css_class="input"),
                        css_class='col-sm-6', style='text-align: center; color: #fff;'
                    ),
                    Div(
                        Field('email', data_name="Email", placeholder="Coloca tu correo oficial", css_class="input"),
                        css_class='col-sm-6', style='text-align: center; color: #fff;'
                    ),
                    css_class='row'
                ),

                HTML("<br>"),

                Div(
                    Div(
                        #InlineRadios('date', id="date", style='text-align: center; color: #fff; font-weight: bold;'),
                        Field('date', id="date", data_name="date", css_class="select"),
                        css_class='col-sm-6', style='text-align: center; color: #fff;'
                    ),
                    Div(
                        Field('hour', id="hour", data_name="hour", css_class="select"),
                        css_class='col-sm-6 from-group', style='text-align: center; color: #fff;'
                    ),
                    css_class='row'
                ),

                Div(
                    Field('all_is_accurate', data_name="all_is_accurate", style='text-align: center; color: #fff;'),
                ),
                

                
                


        )
        self.helper.add_input(Submit('submit', 'Confirmar Asistencia', style='float: center; width: 15em;  height: 3em; position: absolute; top: 92%; left: 50%; -ms-transform: translate(-50%, -50%); transform: translate(-50%, -50%); color: #fff; background-color: rgb(92, 89, 177); font-weight: bold;')) 
        
    
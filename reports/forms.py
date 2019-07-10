from django import forms
from django.forms import ModelForm, DateInput, DateField
import datetime
from .models import Report
from leaflet.forms.widgets import LeafletWidget

class newReportForm(forms.ModelForm):
        class Meta:
                model = Report
                exclude = ['user']
                fields = [
                'user',
                'asunto',
                'imagen',
                'descripcion',
                'geom',
                ]

                labels = {
                'asunto':'Asunto',
                'imagen':'Imagen',
                'descripcion':'Descripción',
                'geom':'Seleccione la ubicación',
        }
                widgets = {
                'asunto': forms.TextInput(attrs={'class':'form-input','placeholder': 'Escriba el asunto'}),
                'imagen': forms.FileInput(attrs={'id':'foto','class':'form-input'}),
                'descripcion': forms.Textarea(attrs={'class':'form-textarea','placeholder': 'Descripción del problema'}), 
                'geom': LeafletWidget(attrs={'geom_type': 'POINT'})
}

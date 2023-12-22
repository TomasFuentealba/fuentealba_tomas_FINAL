from django import forms
from fuentealba_tomas_app.models import Inscrito, Institucion
from django.core.validators import RegexValidator

class FormInscrito(forms.ModelForm):
    observacion = forms.CharField(required=False)
    fecha_inscripcion=forms.DateField(widget=forms.TextInput(attrs={'class':'form-control','type':'date'}))
    hora_inscripcion=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'time'}))

    class Meta:
        model = Inscrito
        fields = '__all__'

class FormInstitucion(forms.ModelForm):

    class Meta:
        model = Institucion
        fields = '__all__'
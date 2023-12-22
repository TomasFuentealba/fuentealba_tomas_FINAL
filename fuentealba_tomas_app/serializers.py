from rest_framework import serializers
from fuentealba_tomas_app import models

class InscritoSerial(serializers.ModelSerializer):
    class Meta:
        model = models.Inscrito
        fields = '__all__'

class InstitucionSerial(serializers.ModelSerializer):
    class Meta:
        model = models.Institucion
        fields = '__all__'
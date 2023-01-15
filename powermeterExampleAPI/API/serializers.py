from .models import Medidor, Medicion
from rest_framework import serializers


class MedidorSerializerMin(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medidor
        fields = ['url', 'llave', 'nombre']
        read_only_fields = ['llave', 'nombre']
        lookup_field = 'llave' 
        extra_kwargs = {
            'url': {'lookup_field': 'llave'},
        }

class MedicionSerializerMin(serializers.ModelSerializer):
    class Meta:
        model = Medicion
        fields = ['fecha_y_hora', 'consumo']


class MedidorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medidor
        fields = ['url', 'llave', 'nombre']
        lookup_field = 'llave' 
        extra_kwargs = {
            'url': {'lookup_field': 'llave'},
        }

class MedicionSerializer(serializers.HyperlinkedModelSerializer):

    medidor = MedidorSerializerMin(read_only = False, required = False)

    class Meta:
        model = Medicion
        fields = ['url', 'fecha_y_hora', 'consumo', 'medidor']
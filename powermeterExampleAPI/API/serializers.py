from .models import Medidor, Medicion
from rest_framework import serializers


class MedidorSerializerMin(serializers.HyperlinkedModelSerializer):
    """
        Versión minimizada de MedidorSerializer.
        En este caso es identica, pero no suele ser el caso.
        
        Si se requiere personalizar el acceso a los campos,
        es más adecuado usar serializadores independientes.

        Por la escalabilidad.
    """
    class Meta:
        model = Medidor
        fields = ['url', 'llave', 'nombre']
        read_only_fields = ['llave', 'nombre']
        lookup_field = 'llave' 
        extra_kwargs = {
            'url': {'lookup_field': 'llave'},
        }

class MedicionSerializerMin(serializers.ModelSerializer):
    """
        Versión minimizada de MedicionSerializer.
        Con solo la fecha_y_hora y el consumo.
    """
    class Meta:
        model = Medicion
        fields = ['fecha_y_hora', 'consumo']


class MedidorSerializer(serializers.HyperlinkedModelSerializer):
    """
        Serializador de el medidor y sus datos relevantes a consultar.
    """
    
    class Meta:
        model = Medidor
        fields = ['url', 'llave', 'nombre']
        lookup_field = 'llave' 
        extra_kwargs = {
            'url': {'lookup_field': 'llave'},
        }

class MedicionSerializer(serializers.HyperlinkedModelSerializer):
    """
        Serializador de la medicion y sus datos relevantes a consultar.
    """

    medidor = MedidorSerializerMin(read_only = False, required = False)

    class Meta:
        model = Medicion
        fields = ['url', 'fecha_y_hora', 'consumo', 'medidor']
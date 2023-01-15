from django.utils.decorators import method_decorator

from .models import Medidor, Medicion

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import MedidorSerializer, MedicionSerializer, MedicionSerializerMin

from .custom_schemas.medidor_schemas import (
                                                medidor_list_schema,
                                                medidor_retrieve_schema,
                                                medidor_create_schema,
                                                medidor_max_consumo_schema,
                                                medidor_min_consumo_schema,
                                                medidor_total_consumo_schema,
                                                medidor_media_consumo_schema,
                                                medidor_agregar_medicion_schema,
                                            )

from .custom_schemas.medicion_schemas import (
                                                medicion_list_schema,
                                                medicion_retrieve_schema,
                                            )

@method_decorator(name='list', decorator=medidor_list_schema)
@method_decorator(name='retrieve', decorator=medidor_retrieve_schema)
@method_decorator(name='create', decorator=medidor_create_schema)
@method_decorator(name='max_consumo', decorator=medidor_max_consumo_schema)
@method_decorator(name='min_consumo', decorator=medidor_min_consumo_schema)
@method_decorator(name='total_consumo', decorator=medidor_total_consumo_schema)
@method_decorator(name='media_consumo', decorator=medidor_media_consumo_schema)
@method_decorator(name='agregar_medicion', decorator=medidor_agregar_medicion_schema)
class MedidorViewSet(viewsets.ModelViewSet):
    """
    Esta vista permite **ver y dar de alta a los medidores registrados**.

    - Url de acceso a medidor particular.
    - Su **llave**.
    - Su **nombre**.
    
    ## Acciones (por medidor):

    - Agregar **mediciones** (una a una).
    - Obtener máximo **consumo**.
    - Obtener mínimo **consumo**.
    - Obtener total **consumo**.
    - Obtener media **consumo**.
    """

    queryset = Medidor.objects.all().order_by('nombre', 'llave')
    serializer_class = MedidorSerializer
    lookup_field = 'llave'
    http_method_names = ['get', 'head', 'post']

    @action(detail=True, methods=['get'], name='Máximo consumo')
    def max_consumo(self, request, llave):
        """
            Regresa el consumo máximo del medidor.
        """
        
        current_object = self.get_object()
        return Response({
                        "nombre" : current_object.nombre,
                        "llave" : current_object.llave,
                         "max_consumo" : current_object.max_consumo,
                         })

    @action(detail=True, methods=['get'], name='Mínimo consumo')
    def min_consumo(self, request, llave):
        """
            Regresa el consumo mínimo del medidor.
        """
        current_object = self.get_object()
        return Response({
                        "nombre" : current_object.nombre,
                        "llave" : current_object.llave,
                         "min_consumo" : current_object.min_consumo,
                         })
    
    @action(detail=True, methods=['get'], name='Consumo total')
    def total_consumo(self, request, llave):
        """
            Regresa el consumo total del medidor.
        """

        current_object = self.get_object()
        return Response({
                        "nombre" : current_object.nombre,
                        "llave" : current_object.llave,
                         "total_consumo" : current_object.total_consumo,
                         })

    @action(detail=True, methods=['get'], name='Promedio de consumo')
    def media_consumo(self, request, llave):
        """
            Regresa el consumo medio del medidor.
        """

        current_object = self.get_object()
        return Response({
                        "nombre" : current_object.nombre,
                        "llave" : current_object.llave,
                         "media_consumo" : current_object.media_consumo,
                         })

    @action(detail=True, methods=['get', 'post'], name='Agregar medición')
    def agregar_medicion(self, request, llave):
        """
            Agrega una medición con su fecha y consumo.
        """

        print(self.get_object())
        print(request.data)
        current_object = self.get_object()
        
        if request.method == 'GET':
            self.serializer_class = MedicionSerializerMin
            return Response({
                            'mensaje':'Use POST para ingresar la medición',
                            'mediddor_actual': {
                                "nombre" : current_object.nombre,
                                "llave" : current_object.llave,
                            },
                            })

        if request.method == 'POST':
            serializer = MedicionSerializerMin(data=request.data)
            if serializer.is_valid():
                try:
                    Medicion.objects.create(**serializer.validated_data, medidor=current_object)
                    current_object.actualizar_data()
                    current_object.save()
                except:
                    return Response({
                        'error' : 'El recurso no se ha podido crear correctamente.'
                    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                else:
                    return Response({
                        'mensaje' : 'Se ha agregado la medición correctamente.',
                        'mediddor_actual': {
                                "nombre" : current_object.nombre,
                                "llave" : current_object.llave,
                        },
                        'medición': serializer.validated_data
                    }, status=status.HTTP_201_CREATED)
   
            return Response({
                'error': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(name='list', decorator=medicion_list_schema)
@method_decorator(name='retrieve', decorator=medicion_retrieve_schema)
class MedicionViewSet(viewsets.ModelViewSet):
    """
    Esta vista permite **ver las mediciones registradas**.

    - Url de acceso a medición particular.
    - Su **fecha y hora**.
    - Su **consumo**.
    - El **medidor** que registro la medición. Con:
        - Url de acceso al medidor particular.
        - La **llave**.
        - El **nombre**.
    """
    
    queryset = Medicion.objects.all().order_by('medidor__nombre', 'fecha_y_hora')
    serializer_class = MedicionSerializer
    http_method_names = ['get', 'head']
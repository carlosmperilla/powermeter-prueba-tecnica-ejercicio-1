from .models import Medidor, Medicion
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import MedidorSerializer, MedicionSerializer, MedicionSerializerMin


class MedidorViewSet(viewsets.ModelViewSet):
    queryset = Medidor.objects.all().order_by('nombre', 'llave')
    serializer_class = MedidorSerializer
    lookup_field = 'llave'
    http_method_names = ['get', 'head', 'post']

    @action(detail=True, methods=['get'], name='Maximo consumo')
    def max_consumo(self, request, llave):
        current_object = self.get_object()
        return Response({
                        "nombre" : current_object.nombre,
                        "llave" : current_object.llave,
                         "max_consumo" : current_object.max_consumo,
                         })

    @action(detail=True, methods=['get'], name='Minimo consumo')
    def min_consumo(self, request, llave):
        current_object = self.get_object()
        return Response({
                        "nombre" : current_object.nombre,
                        "llave" : current_object.llave,
                         "min_consumo" : current_object.min_consumo,
                         })
    
    @action(detail=True, methods=['get'], name='Consumo total')
    def total_consumo(self, request, llave):
        current_object = self.get_object()
        return Response({
                        "nombre" : current_object.nombre,
                        "llave" : current_object.llave,
                         "total_consumo" : current_object.total_consumo,
                         })

    @action(detail=True, methods=['get'], name='Promedio de consumo')
    def media_consumo(self, request, llave):
        current_object = self.get_object()
        return Response({
                        "nombre" : current_object.nombre,
                        "llave" : current_object.llave,
                         "media_consumo" : current_object.media_consumo,
                         })

    @action(detail=True, methods=['get', 'post'], name='Agregar medición')
    def agregar_medicion(self, request, llave):
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
            })

class MedicionViewSet(viewsets.ModelViewSet):
    queryset = Medicion.objects.all().order_by('medidor__nombre', 'fecha_y_hora')
    serializer_class = MedicionSerializer
    http_method_names = ['get', 'head']
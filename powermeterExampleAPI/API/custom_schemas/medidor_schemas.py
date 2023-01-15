from drf_yasg.utils import swagger_auto_schema

medidor_list_schema = swagger_auto_schema(
    operation_summary="Obtiene los medidores",
    operation_description='Permite visualizar los medidores.',
    tags=['Medidores - Visualización']
)

medidor_retrieve_schema = swagger_auto_schema(
    operation_summary="Obtiene un medidor por su llave",
    operation_description='Permite visualizar un medidor por su llave única.',
    tags=['Medidores - Visualización']
)

medidor_create_schema = swagger_auto_schema(
    operation_summary="Da de alta un medidor",
    operation_description='Da de alta un medidor con su llave y nombre.',
    tags=['Medidores - Creación']
)

medidor_max_consumo_schema = swagger_auto_schema(
    operation_summary="Regresa el medidor y su consumo máximo",
    operation_description='Regresa el medidor y su consumo máximo',
    tags=['Medidores - Visualización - Acciones']
)

medidor_min_consumo_schema = swagger_auto_schema(
    operation_summary="Regresa el medidor y su consumo mínimo",
    operation_description='Regresa el medidor y su consumo mínimo',
    tags=['Medidores - Visualización - Acciones']
)

medidor_total_consumo_schema = swagger_auto_schema(
    operation_summary="Regresa el medidor y su consumo total",
    operation_description='Regresa el medidor y su consumo total',
    tags=['Medidores - Visualización - Acciones']
)

medidor_media_consumo_schema = swagger_auto_schema(
    operation_summary="Regresa el medidor y su consumo medio",
    operation_description='Regresa el medidor y su consumo medio',
    tags=['Medidores - Visualización - Acciones']
)

medidor_media_consumo_schema = swagger_auto_schema(
    operation_summary="Regresa el medidor y su consumo medio",
    operation_description='Regresa el medidor y su consumo medio',
    tags=['Medidores - Visualización - Acciones']
)

medidor_agregar_medicion_schema = swagger_auto_schema(
    operation_summary="Añade una medición al medidor (POST)",
    operation_description='Añade una medición al medidor **(POST)**\n'+
                          'Muestra el medidor actual **(GET)**',
    tags=['Medidores - Creación - Acciones']
)
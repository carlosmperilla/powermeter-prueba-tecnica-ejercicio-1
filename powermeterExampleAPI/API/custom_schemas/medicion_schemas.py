from drf_yasg.utils import swagger_auto_schema

medicion_list_schema = swagger_auto_schema(
    operation_summary="Obtiene las mediciones",
    operation_description='Permite visualizar los mediciones.',
    tags=['Mediciones - Visualización']
)

medicion_retrieve_schema = swagger_auto_schema(
    operation_summary="Obtiene una medición por su id",
    operation_description='Permite visualizar una medición por su id.',
    tags=['Mediciones - Visualización']
)
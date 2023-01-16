# powermeter-prueba-tecnica-ejercicio-1
Resolución prueba técnica. Ejercicio 1. Powermeter API.

## Diagrama UML
El diagrama es solo esquemático, respecto a los accesos que se poseen en la API.
Python suele tener un enfoque más de acceso público entre aplicaciones.

Por ejemplo, **actualizar_max_consumo()** es un método no accesible directamente por el usuario desde la API. Pero **actualizar_data()**, es accesible mediante el endpoint **/agregar_medicion** que activa este método.

<img src="https://raw.githubusercontent.com/carlosmperilla/powermeter-prueba-tecnica-ejercicio-1/main/UML_Models.jpg" alt="UML Models" width="600"/>

## Implementar y probar
Ejecutando el siguiente script se puede descargar, construir el contenedor e implementar la API.

```sh
 git clone https://github.com/carlosmperilla/powermeter-prueba-tecnica-ejercicio-1.git
 cd powermeter-prueba-tecnica-ejercicio-1
 docker build -t carlos/apipowermeter .
 docker run -p 8000:8000 carlos/apipowermeter
```

## Funcionamiento API
El endpoint a la Browsabe API (que puede usarse desde el navegador) es:
>http://localhost:8000/api/

### Acceso a medidores
http://localhost:8000/api/Medidores/

### ¿Cómo dar de alta medidores?
Usando el método POST en http://localhost:8000/api/Medidores/

### Acceso a mediciones
http://localhost:8000/api/Mediciones/

### Acciones a medidores
Usando el medidor de ejemplo. Y su llave **EJEMPLO286822662**
En la **Browsable API** se encuentran en:

http://localhost:8000/api/Medidores/EJEMPLO286822662

En el botón **Extra Actions**.

#### Obtener el máximo consumo
http://localhost:8000/api/Medidores/EJEMPLO286822662/max_consumo/

#### Obtener el mínimo consumo
http://localhost:8000/api/Medidores/EJEMPLO286822662/min_consumo/

#### Obtener el total consumo
http://localhost:8000/api/Medidores/EJEMPLO286822662/total_consumo/

#### Obtener el consumo promedio
http://localhost:8000/api/Medidores/EJEMPLO286822662/media_consumo/

#### Agregar medición
Usando el método POST.

http://localhost:8000/api/Medidores/EJEMPLO286822662/agregar_medicion/

## Documentación API
Gracias a la **Browsable API de Django REST Framework** se puede documentar en la misma.

Pero además de eso, posee documentación estándar **Swagger y ReDoc**.
### Swagger
http://localhost:8000/api/swagger/
### ReDoc
http://localhost:8000/api/redoc/

## Superusuario para el administrador
Por defecto uso en desarrollo:
> Username: Carlos
> Password: 12345

## Mejoras que realizaría
- Implementar el sistema de testing de Django, para asegurarse del buen funcionamiento de la API. Sobre todo cuando se creen nuevas acciones.
- Implementar acciones PUT, PATCH y DELETE.
- Poder dar de baja a los medidores (no borrarlos, porque genera perdida de información). Al crearse por defecto están de alta.
- Poder agregar varias mediciones, en lugar de una a una.
- Agregar atributo de última actualización a los medidores.
- Verificar que las fechas sean acordes y coherentes. Al igual que los consumos por zona.
- Integrar coordenadas geográficas a cada medidor. Para separar por zonas.
- Limitar de forma realista los atributos de los modelos (como no sabía de qué tamaño sería la llave, puso uno arbitrario lo suficientemente grande para funcionar).


# Contexto de la Aplicación

Esta aplicación es un backend desarrollado para la gestión de propiedades inmobiliarias y el sistema de “likes” de usuarios sobre dichas propiedades. El proyecto está estructurado de manera modular para facilitar el mantenimiento y la escalabilidad, utilizando buenas prácticas de desarrollo y separación de responsabilidades.

### Características principales

- Gestión de propiedades: permite crear, consultar, actualizar y eliminar propiedades.
- Sistema de likes: los usuarios pueden dar “me gusta” a las propiedades.
- Arquitectura limpia: separación clara entre controladores (API), servicios, repositorios y modelos.
- Conexión a base de datos MySQL para el almacenamiento de la información.
- Ejemplos de peticiones y respuestas en formato JSON.
- Pruebas unitarias para asegurar la calidad del código.

### Tecnologías utilizadas

- Python 3.10+
- FastAPI para la creación de endpoints (en caso de usar API REST)
- SQLAlchemy/MySQL Connector para la gestión de la base de datos
- Estructura basada en servicios y repositorios

### Estructura del proyecto

- `app/api/`: Controladores y manejadores de rutas.
- `app/core/`: Configuración y excepciones personalizadas.
- `app/database/`: Lógica de conexión a la base de datos.
- `app/dependencies/`: Inyección de dependencias para los endpoints.
- `app/models/`: Definición de modelos de datos.
- `app/repositories/`: Acceso y manipulación de datos en la base de datos.
- `app/services/`: Lógica de negocio.
- `examples/`: Ejemplos de peticiones y respuestas.
- `tests/`: Pruebas unitarias.
# Prueba Habi
Requerimientos
Habi desea tener dos microservicios. El primero para que los usuarios externos puedan
consultar los inmuebles disponibles almacenados en la base de datos. El segundo para que los
usuarios puedan darle “Me gusta” a un inmueble en específico.

No funcionales
● Se espera que entregues código fácil de mantener, fácil de leer, y autodocumentado.
● Se espera que el código siga una guía de estilos definida (ej. PEP8 para Python).
● Los microservicios deben construirse para ser consumidos en una arquitectura REST.
Funcionales (historias de usuario)
Servicio de consulta
● Los usuarios pueden consultar los inmuebles con los estados: “pre_venta”, “en_venta” y
“vendido” (los inmuebles con estados distintos nunca deben ser visibles por el usuario).
● Los usuarios pueden filtrar estos inmuebles por: Año de construcción, Ciudad, Estado.
● Los usuarios pueden aplicar varios filtros en la misma consulta.
● Los usuarios pueden ver la siguiente información del inmueble: Dirección,
Ciudad, Estado, Precio de venta y Descripción.
Servicio de “Me gusta”
● Los usuarios pueden darle me gusta a un inmueble en específico y esto debe quedar
registrado en la base de datos.
● Los “Me gusta” son de usuarios registrados, y debe quedar registrado en la base de
datos el histórico de “me gusta” de cada usuario y a cuáles inmuebles.

Instrucciones para la prueba técnica
1. El código debe quedar almacenado en un repositorio de git.
2. Como tu primer commit, incluye un README detallando la tecnologías que vas a utilizar
y cómo vas a abordar el desarrollo.
3. Si tienes dudas escríbelas en el REAME y resuelvelas tú mismo, junto con la razón de
porque las resolviste de esa manera.
4. En el correo que recibiste la prueba deben estar las credenciales de acceso para
conectarse a la base de datos.
5. El primer requerimiento (Servicio de consulta) es práctico, por lo tanto se espera el
código funcional.
6. En el primer requerimiento, crear un archivo JSON con los datos que esperas que
lleguen del front con los filtros solicitados por el usuario.
7. En el primer requerimiento, el estado actual de un inmueble es el último estado
insertado en la tabla “status_history” para dicho inmueble.
8. Se espera que no modifiques ningún registro en la base de datos, pero si necesitas una
mayor cantidad de registros, puedes agregar nuevos.
9. La información de otros registros puede que tenga inconsistencias, recuerda manejar
esas excepciones.
10. El segundo requerimiento (Servicio de “Me gusta”) es conceptual. No existe el modelo
en la base de datos para soportar esta información.
11. En el segundo requerimiento se espera que tu extiendas este modelo con un diagrama
de Entidad-Relación para soportar esta información. Por lo tanto no se espera que
escribas código del microservicio, ni modifiques la base de datos. Únicamente el
diagrama y el código SQL para extender el modelo, junto con la explicación de porque
lo modificaste de esa forma (incluyelo en el README).
12. Tu código debe tener pruebas unitarias.
13. Recuerda divertirte haciendo este reto, si tienes bloqueos, continúa con otra parte.
14. Al terminar la prueba, responde al mismo correo desde el cual se te envió la prueba con
el enlace al repositorio.

Segundo ejercicio:
Se tiene un arreglo myArray que contiene bloques de números. Los bloques pueden ser de
cualquier largo, los números contenidos están en el rango de 1 a 9 y se separan por un cero
para definir los bloques. Se deben ordenar los números de los bloques individualmente de
menor a mayor e imprimir las secuencias separando los bloques por un espacio. Por ejemplo,
para el arreglo: (1,3,2,0,7,8,1,3,0,6,7,1) la respuesta esperada es:
123 1378 167
El arreglo y su longitud están definidos en la sección de código predefinido. Asumir que este
código predefinido puede variar (valores y longitud del arreglo) y se debe tener en cuenta lo
siguiente al programar:
- El número de bloques es variable.
- Un cero marca el final de un bloque y el inicio de otro. El inicio del arreglo se asume como el
inicio de un bloque y el final de un arreglo se asume como el final de un bloque (Por lo tanto un
cero al inicio o al final del arreglo de hecho implicarían un bloque sin elementos)

- Un bloque puede no contener elementos, en cuyo caso se imprimirá una x. Por ejemplo, para
(2,1,0,0,3,4) se imprimiría.
12 X 34

## Project Structure

```
Prueba Habi/
├── main.py
├── requirements.txt
├── app/
│   ├── api/
│   │   ├── likes_handler.py
│   │   └── property_handler.py
│   ├── core/
│   │   └── config.py
│   ├── database/
│   │   └── connection.py
│   ├── dependencies/
│   │   └── dependencies.py
│   ├── models/
│   │   └── property.py
│   ├── repositories/
│   │   ├── likes_repository.py
│   │   └── property_repository.py
│   └── services/
│       ├── likes_service.py
│       └── property_service.py
├── examples/
│   ├── request.json
│   └── response.json
└── tests/
    ├── test_likes_service.py
    └── test_property_repository.py
```

## Features
- Property management (CRUD operations)
- Likes system for properties
- Modular codebase with clear separation of concerns
- Example request/response JSON files
- Unit tests for core functionality

## Getting Started

### Prerequisites
- Python 3.10+
- Install dependencies:

```bash
pip install -r requirements.txt
```

### Running the Application

```bash
python main.py
```

### Running Tests

```bash
pytest tests/
```

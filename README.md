# Test backend

## Introducción
- **auth**: Contiene los servicios de autenticación de usuarios
- **db**: Contiene los archivos de base de datos, incluyendo `db.py` y `utils.py`.
- **routers**: Contiene los archivos de enrutamiento, incluyendo `__init__.py`, `endpoints.py`, `__init__.py` y `routers.py`.
- **services**: Contiene los archivos de servicio, incluyendo `products_service.py`.
- **utils**: Contiene los archivos de utilidades, incluyendo `schemas.py`.
- **docker-compose.yml**: Define la configuración de Docker Compose para el proyecto.
- **Dockerfile**: Define la imagen de Docker para el proyecto.
- **init.sql**: Contiene el script SQL para inicializar la base de datos.
- **main.py**: Es el punto de entrada principal del proyecto.
- **README.md**: Este archivo readme.
- **requirements.txt**: Contiene los requisitos de dependencia del proyecto.

## Instalación
Para instalar el proyecto, siga estos pasos:

1. Clone el repositorio del proyecto
2. Ejecute el comando 
`docker compose up --build`

## Uso
La aplicación se puede acceder en la siguiente URL:

- http://localhost:9000

## Documentación
Para obtener más información sobre el proyecto, consulte la siguiente documentación:

- Docker Compose
- Dockerfile
- SQL

El proyecto cuenta con su propia documentación en los enlaces
- `http://localhost:9000/docs`
- `http://localhost:9000/redoc`


## Licencia
El proyecto Intellimetrica está licenciado bajo la licencia MIT. Para obtener más información, consulte el archivo LICENSE en el repositorio del proyecto.


## Siguientes Pasos

1. Asegúrate de tener configuradas las variables de entorno adecuadamente en tu entorno de desarrollo.
2. Verifica que todas las rutas y métodos en tu API funcionen correctamente.
3. Asegúrate de que el servicio de notificaciones esté enviando los correos electrónicos como se espera.

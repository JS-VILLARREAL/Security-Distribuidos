# Nombre del Proyecto

Security

## Requisitos Previos

Asegúrate de tener instalado lo siguiente antes de comenzar:

- Python (versión 3.9.13)

## Configuración del Entorno

1. Clona el repositorio:

    ```bash
    git clone https://github.com/JS-VILLARREAL/Security-Distribuidos.git
    ```

2. Crea un entorno virtual dentro de la carpeta ya clonada:

    ```bash
    py -m venv venv
    ```

3. Entra al entorno virtual previamente creado:

    ```bash
    .venv\Script\activate
    ```

4. Instala las dependencias del proyecto:

    ```bash
    pip install -r requirements.txt
    ```

## Configuración de la Base de Datos en la Carpeta Corhuila

Para configurar la base de datos en la carpeta `corhuila`, sigue estos pasos:

1. Abre el archivo `corhuila/settings.py` en tu editor de código.

2. Modifica los valores según las especificaciones de tu base de datos. Por ejemplo, si estás utilizando Mysql, podrías tener algo como:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'nombre_de_tu_base_de_datos',
            'USER': 'tu_usuario',
            'PASSWORD': 'tu_contraseña',
            'HOST': 'localhost',
            'PORT': '',
        }
    }
    ```

3. Guarda el archivo `settings.py`.

Recuerda proporcionar los detalles específicos de tu base de datos, como el nombre de la base de datos, el usuario, la contraseña, el host y el puerto. Asegúrate de seguir las recomendaciones de seguridad al manejar información confidencial como contraseñas.

¡Listo! Has configurado la base de datos en la carpeta `corhuila`. Ahora puedes continuar con otros pasos de configuración según sea necesario.

---
5. Realiza las migraciones de la base de datos:

    ```bash
    py manage.py makemigrations
    py manage.py migrate
    ```

## Ejecutar el Proyecto

1. Ejecutar el servidor

```shell
py manage.py runserver
```

2. Accede a la interfaz Swagger para explorar la API:

    - Localmente: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

    Swagger proporciona una interfaz interactiva que te permite probar y explorar fácilmente los puntos finales de la API. ¡Disfruta de tu experiencia con el proyecto de seguridad!
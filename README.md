# Nombre del Proyecto

Security

## Requisitos Previos

Asegúrate de tener instalado lo siguiente antes de comenzar:

- Python (versión 3.9.13)

## Configuración del Entorno

1. Crea un entorno virtual:

    ```bash
    pip install
    pipenv shell
    ```

3. Instala las dependencias del proyecto:

    ```bash
    pipenv install -r requirements.txt
    ```

4. Configura las variables de entorno:

    ```bash
    cp .env.example .env
    ```

    Ajusta las variables en el archivo `.env` según sea necesario.

5. Realiza las migraciones de la base de datos:

    ```bash
    python manage.py migrate
    ```

## Ejecutar el Proyecto

```bash
py manage.py runserver

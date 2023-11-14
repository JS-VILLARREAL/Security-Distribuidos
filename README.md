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

5. Realiza las migraciones de la base de datos:

    ```bash
    py manage.py makemigrations
    py manage.py migrate
    ```

## Ejecutar el Proyecto

```shell
py manage.py runserver

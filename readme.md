Empty Readme

# our_module

## Descripción

`our_module` es un proyecto que tiene como objetivo proporcionar un entorno listo para usar utilizando contenedores Docker.

## Características

- [Contenedores Docker]

    Odoo como contenedor independiente: Ejecuta la aplicación Odoo en un entorno aislado.
    PostgreSQL como base de datos separada: Gestión de la base de datos con persistencia de datos.


- [Persistencia de Datos]

    Configuración de volúmenes para asegurar la persistencia de datos en la base de datos PostgreSQL y los archivos de Odoo.
- [Manejo de Dependencias]

    Automatización del manejo de dependencias del sistema operativo y de Odoo a través de la imagen de Docker.
    Configuración personalizable de Python para agregar librerías adicionales en los módulos personalizados.

- [Soporte para Bases de Datos PostgreSQL]

    Integración con PostgreSQL como backend de la base de datos.
    Configuración inicial automatizada de usuario, contraseña y base de datos a través de variables de entorno.

## Requisitos previos

Antes de iniciar con el proyecto, asegúrate de cumplir con los siguientes requisitos:

Docker y Docker Compose instalados:
        Asegúrate de tener Docker instalado en tu máquina. Puedes descargarlo e instalarlo desde la página oficial de Docker.
        Docker Compose también debe estar configurado. Generalmente, ya está incluido con Docker Desktop.

    Verifica las versiones instaladas ejecutando los siguientes comandos:

    docker --version
    docker-compose --version

Conexión a Internet estable:

    Necesitarás una conexión para descargar las imágenes de Docker necesarias (por ejemplo, odoo y postgres).

Configuración del archivo .env:

    Prepara un archivo .env con las variables de entorno requeridas para el proyecto, como:

    WEB_HOST=odoo_16
    WEB_IMAGE_NAME=odoo:16.0
    WEB_PORT=8085
    WEBSOCKET_PORT=8086

    DB_IMAGE=postgres:15
    DB_HOST=postgres_15
    DB_PORT=5445
    DB_NAME=postgres
    DB_USER=odoo_db
    DB_PASSWD=odoo_db

Permisos de red y puertos:

    Verifica que los puertos necesarios estén disponibles:
        Puerto 8069: interfaz web de Odoo.
        Puerto 8072: conexión a la base de datos PostgreSQL.

Editor de texto o IDE:

    Recomendable tener un editor para modificar los archivos del proyecto, como:
    Visual Studio Code

## Instalación

Sigue estos pasos para instalar y configurar el proyecto:

Clona el Repositorio Comienza clonando el repositorio en tu máquina local:

    git clone https://github.com/Honcito/our_module.git
    cd our_module

Configura las Variables de Entorno Crea y personaliza un archivo .env basado en el ejemplo proporcionado en el proyecto:

    cp .env

Asegúrate de configurar correctamente los valores de las siguientes variables:

    WEB_HOST=odoo_16
    WEB_IMAGE_NAME=odoo:16.0
    WEB_PORT=8085
    WEBSOCKET_PORT=8086

    DB_IMAGE=postgres:15
    DB_HOST=postgres_15
    DB_PORT=5445
    DB_NAME=postgres
    DB_USER=odoo_db
    DB_PASSWD=odoo_db

Inicia los Contenedores con Docker Compose Construye e inicia los contenedores necesarios (Odoo y PostgreSQL) ejecutando:

    docker-compose up --build

Accede a la Interfaz de Odoo Una vez que los contenedores estén en ejecución, abre tu navegador web y accede a Odoo ingresando la siguiente URL:

    http://localhost:8069

    Configura Odoo en el Navegador
        - Al acceder por primera vez, Odoo te pedirá que crees una base de datos.
        - Proporciona la siguiente información:
            - Nombre de la base de datos: Puede ser cualquier nombre (por ejemplo, my_database).
            - Correo Electrónico Administrador: Un correo que utilizarás como usuario administrador.
            - Contraseña Administrador: Define una contraseña segura para el usuario administrador.
        - Haz clic en "Crear Base de Datos" para finalizar.

    Comienza a Usar Odoo Una vez que la base de datos esté configurada, podrás explorar la interfaz de Odoo, instalar módulos, y personalizar las funcionalidades según tus necesidades.

Apagado y Reinicio del Proyecto

Para detener los contenedores:

    docker-compose down

Para reiniciarlos:

    docker-compose up

 

# Desafío Sr. Full Stack Developer

API en donde se pueda detectar si existe mutación enviando la secuencia de ADN mediante un JSON.



## Características


- Integrado con Pipenv para la gestión de paquetes.
- Despliegue rápido a heroku con `$ pipenv run deploy`.
- Uso de `.env` archivo.
- Integración de SQLAlchemy para la abstracción de bases de datos.

## Instalación Local(automática si está usando gitpod)

> Importante: El boiplerplate está hecho para Python 3.7 pero puede cambiarlo fácilmente`python_version` en el Pipfile.

Los siguientes pasos se ejecutan automáticamente dentro de gitpod, si está haciendo una instalación local, debe hacerlo manualmente:

```sh
Crear una carpeta .env donde va a copiar lo que se encuentra dentro de .env.example;
pipenv install;
mysql -u root -e "CREATE DATABASE example";
pipenv run init;
pipenv run migrate;
pipenv run upgrade;
pipenv run start (para correr la app en local)
```

## Significado de las carpetas

Todo el codigo de la API esta escrito en `./src/`.

- src/main.py (es donde se deben codificar sus puntos finales)
- src/models.py (tablas de base de datos y lógica de serialización)
- src/mutant.py (Funcion que permite ver si una persona es mutante o no)
- src/admin.py (modelos al administrador y administracion sus datos fácilmente)

Para obtener una explicación más detallada, busque el tutorial dentro de la `docs` carpeta.

## Recuerde migrar cada vez que cambie sus modelos

Tienes que migrar y actualizar las migraciones para cada actualización que realices en tus modelos:
```
$ pipenv run migrate (to make the migrations)
$ pipenv run upgrade  (to update your databse with the migrations)
```


# Instalación manual para Ubuntu y Mac

⚠️ Asegúrate de que tienes  `python 3.6+` y `MySQL` instalado en su ordenador y MySQL se está ejecutando, a continuación, ejecute los siguientes comandos:
```sh
$ pipenv install (para instalar paquetes pip)
$ pipenv run migrate (para crear la base de datos)
$ pipenv run start (para iniciar el servidor web del matraz)
```


## Deploy to Heroku

This template is 100% compatible with Heroku[https://www.heroku.com/], just make sure to understand and execute the following steps:

```sh
// Install heroku
$ npm i heroku -g
// Login to heroku on the command line
$ heroku login -i
// Create an application (if you don't have it already)
$ heroku create <your_application_name>
// Commit and push to heroku (commited your changes)
$ git push heroku main
```
:warning: For a more detailed explanation on working with .env variables or the MySQL database [read the full guide](https://github.com/4GeeksAcademy/flask-rest-hello/blob/master/docs/DEPLOY_YOUR_APP.md).

Antes de ejecutar la pagina se deben poner los siguientes comandos.

pip install djangorestframework

pip install --upgrade pip

python -m pip install Pillow

python manage.py migrate

python manage.py runserver

Para entrar al admin se entra por la siguiente URL http://127.0.0.1:8000/admin/

Usuario: alejandro

Contraseña: 12345678

La base de datos es sql lite, asì que se almacenara de forma local.

Desde la pagina web se pueden crear productos y categorias, tambien pueden modificarlas pero no se pueden eliminar.

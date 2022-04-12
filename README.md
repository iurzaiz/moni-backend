# moni-backend
Prueba para entrar a trabajar en la empresa Moni S.A

El proyecto esta dockerizado y desarrollado en Django con Postgres

Instrucciones para correrlo:

Dentro de la carpeta frontend se encuentra el archvio index.html

Crear superusuario con el siguiente comando:
sudo docker-compose run web python ./backend/manage.py createsuperuser

Para correr el proyecto backend ejecutar docker-compose up
Copiar archivo example.env y renombrarlo como .env, ponerle las variables necesarias

Consigna: 
Se debe desarrollar sitio web en el que se registran pedido de préstamos de usuarios que acceden a el.
El usuario no necesita registrarse para solicitar un préstamo.
Para definir si al usuario se le aprueba o no el préstamo usaremos una API
El formulario de pedido de préstamos el usuario debe ingresar dni, nombre y apellido, genero, email y monto solicitado.
El usuario luego de ingresar los datos debe recibir la respuesta negativa o positiva en la misma página que ingresó sus datos.
Contemplar casos de datos ingresados con errores.
También se debe desarrollar un sitio de administración en el que se puedan ver los pedidos de préstamo, con la opción de editarlos y eliminarlos. A este sitio solo pueden acceder usuarios administradores. No usar admin de Django.


CORS esta deshabilitado pero:

En el caso de error que la peticion no sea aprobada por CORS la extension llamada "Moesif Orign & CORS Changer"
Enlace a la extensión desde Google Chrome: https://chrome.google.com/webstore/detail/moesif-origin-cors-change/digfbfaphojjndkpccljibejjbppifbc
Habilitarla para la pagina en cuestion


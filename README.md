# Script_Pag_Sep
Repositorio para realizar la descarga de los libros de la página de la SEP de la clase Seguridad Informática.

Para el uso de este script se requiere tener instalada la última versión de Python.

Para las librerías se requiere tener BeautifulSoup y requests.

Iniciando actualizamos el Ubuntu con los comandos sudo apt update y sudo apt upgrade.


pasamos a realizar la instalación de Git con el comando:
```
sudo apt install git
```

Luego instalamos Python en el servidor con el comando siguiente,para que pueda ejecutar el script que teníamos de la clase anterior:
```
sudo apt install python
```
Comprobamos que tenemos la ultima versión de python en el servidor con el comando:
```
python3 --version
```
Para la instalacion de las librerias se ocupa "pip" (un sistema de gestión de paquetes) por lo que se necesita instalar si no se cuenta con el.
```
sudo apt-get install python3-pip
```
Estando dentro del servidor le instalamos las líbrerias que vamos a ocupar (BeautifulSoup y Requests) con los siguientes comandos:
```
pip install requests
pip install beautifulsoup4
```
Creamos una llave SSH para la conexión con el servidor, esta se genera y guarda el archivo en el servidor:
```
ssh-keygen -t rsa -b 4096 -C "Correo@usuario.com"
```
Buscamos la llave que acabamos de crear y la copiamos:
```
cat ~/.ssh/id_rsa.pub
```
Guardamos en la cuenta de github la llave que generamos.

Estando en github entramos al repositorio en donde esta el script de la clase y dando click en el botón Code obtenemos el SSH para poder clonar el repositorio en el servidor: 
```
git clone git@github.com:Bananas-En-Pijamas/Script_Pag_Sep.git
```
y procedemos a clonar el repositorio en el servidor

Ya con el repositorio clonado procedemos a buscar la carpeta y el Script.

Y ejecutamos el script:
```
python3 Script.py
```
# Calificacion 
9/10 el script hace lo que tiene que hacer pero estaria mejor que pusieran un indicador de que esta haciendo

o en que parte del proceso se encuentra. 

# Mejora Del Codigo 

•	Como primer cambio fue quitar la librería shutil.

•	Además de también reducir líneas de código declarando las carpetas temporal y libros, en vez de hacerlo uno por uno declare las dos juntas

•	Realice dentro de una función llamada obtener_enlaces_validos, la solicitud http a la página y a la misma función pedir como parámetros los url´s de la página el base_url y el main_url.

•	Añadi con ciertos parámetros los enlaces que han sido validados y los retornamos en la misma función.

•	Cree otro método llamado Descargar_imagenes el cual lleva como parámetros la url base y la extensión validada de la imagen que se descargaran de cada url.

•	En la misma función coloque el procedimiento donde se crearán las subcarpetas donde contendrán las imágenes de los libros correspondientes al url del libro en cuestión, además de también todas las consultas y llamadas del url y carpetas del proyecto.

•	Dentro de un if ingrese los parámetros de base_url, main_url, y un join del url que será la respectiva para cada libro de la pagina.

•	Al igual de las variables aquí mismo declare las 3 funciones de arriba.

Para probarlo ingresa en tu terminal la siguiente instruccion

```
python3 MejoraCodigo.py
```

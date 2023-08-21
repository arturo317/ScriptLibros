import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Crear carpetas si no existen
for folder in ["libros", "temporal"]:# 1. reduci las lineas de codigo en una sola en el cual se creen las dos carpetas si es que no existen
    if not os.path.exists(folder):
        os.makedirs(folder)

def obtener_enlaces_validos(base_url, main_url):# 2. validamos los enlaces de la pagina en la cual realizara la descarga
# Realizar solicitud HTTP a la página principal    
    response = requests.get(main_url)
    soup = BeautifulSoup(response.content, "html.parser")
# Encontrar y almacenar enlaces
    enlaces_validos = []
    for enlace in soup.find_all("a", href=True):
        if "2023/" in enlace["href"] and enlace["href"].endswith(".htm"):# 3. reasignamos los valores que toman cada link de cada imagen
            # Extraer el nombre de la carpeta de cada enlace y almacenarlo
            enlaces_validos.append(enlace["href"].split("/")[-1].split(".")[0][-5:])
    
    return enlaces_validos # 4. hacemos retomar el valor del enlace valido 

def descargar_imagenes(image_base_url, enlaces_validos):# 5. creo un metodo que descargara las imagenes y tendra por parametros la base del url y si en enlace es valido
    for folder_name in enlaces_validos:
        subfolder_path = os.path.join("libros", folder_name)
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)
# Descargar y guardar las imágenes en la carpeta "temporal"
        for image_number in range(401):
            image_download_url = image_base_url.format(folder_name, str(image_number).zfill(3))
            image_response = requests.get(image_download_url)
            if image_response.status_code == 200:
                image_path = os.path.join("temporal", f"{folder_name}_{image_number:03d}.jpg")
                with open(image_path, "wb") as f:
                    f.write(image_response.content)
# Mover archivos de la carpeta temporal a las subcarpetas correspondientes en "libros"
def mover_archivos_a_carpetas():
    temporal_folder = "temporal"
    libros_folder = "libros"
 # Listar los archivos en la carpeta temporal
    for file_name in os.listdir(temporal_folder):
        if file_name.endswith(".jpg"):
# Obtener la cadena de 5 letras del nombre de archivo
            folder_name = file_name.split("_")[0]
# Obtener la ruta completa del archivo en temporal
            temp_file_path = os.path.join(temporal_folder, file_name)
# Obtener la ruta completa de la subcarpeta en libros
            subfolder_path = os.path.join(libros_folder, folder_name)
# Crear la subcarpeta si no existe
            if not os.path.exists(subfolder_path):
                os.makedirs(subfolder_path)
# Mover el archivo a la subcarpeta en libros
            new_file_path = os.path.join(subfolder_path, file_name)
            os.rename(temp_file_path, new_file_path)

if __name__ == "__main__":# 5 declaramos dentro del if los metodos creado arriba repectivamente con sus variables url y sus parametros 
    base_url = "https://www.conaliteg.sep.gob.mx/"
    main_url = urljoin(base_url, "primaria.html")
    image_base_url = urljoin(base_url, "2023/c/{}/{}.jpg")

    enlaces_validos = obtener_enlaces_validos(base_url, main_url)
    descargar_imagenes(image_base_url, enlaces_validos)
    mover_archivos_a_carpetas()# 6. elimine la libreria shutil, y mandamos los temporales a la carpeta libros por otro metodo
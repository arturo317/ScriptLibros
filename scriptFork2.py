import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Crear carpetas si no existen
for folder in ["libros", "temporal"]:
    if not os.path.exists(folder):
        os.makedirs(folder)

def obtener_enlaces_validos(base_url, main_url):
    response = requests.get(main_url)
    soup = BeautifulSoup(response.content, "html.parser")

    enlaces_validos = []
    for enlace in soup.find_all("a", href=True):
        if "2023/" in enlace["href"] and enlace["href"].endswith(".htm"):
            # Extraer el nombre de la carpeta de cada enlace y almacenarlo
            enlaces_validos.append(enlace["href"].split("/")[-1].split(".")[0][-5:])
    
    return enlaces_validos

def descargar_imagenes(image_base_url, enlaces_validos):
    for folder_name in enlaces_validos:
        subfolder_path = os.path.join("libros", folder_name)
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)

        for image_number in range(401):
            image_download_url = image_base_url.format(folder_name, str(image_number).zfill(3))
            image_response = requests.get(image_download_url)
            if image_response.status_code == 200:
                image_path = os.path.join("temporal", f"{folder_name}_{image_number:03d}.jpg")
                with open(image_path, "wb") as f:
                    f.write(image_response.content)

def mover_archivos_a_carpetas():
    temporal_folder = "temporal"
    libros_folder = "libros"

    for file_name in os.listdir(temporal_folder):
        if file_name.endswith(".jpg"):
            folder_name = file_name.split("_")[0]
            temp_file_path = os.path.join(temporal_folder, file_name)
            subfolder_path = os.path.join(libros_folder, folder_name)
            if not os.path.exists(subfolder_path):
                os.makedirs(subfolder_path)
            new_file_path = os.path.join(subfolder_path, file_name)
            os.rename(temp_file_path, new_file_path)

if __name__ == "__main__":
    base_url = "https://www.conaliteg.sep.gob.mx/"
    main_url = urljoin(base_url, "primaria.html")
    image_base_url = urljoin(base_url, "2023/c/{}/{}.jpg")

    enlaces_validos = obtener_enlaces_validos(base_url, main_url)
    descargar_imagenes(image_base_url, enlaces_validos)
    mover_archivos_a_carpetas()

   

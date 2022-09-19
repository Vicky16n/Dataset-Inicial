## Llamada a las librerías necesarias para descargarse las imágenes con el driver de google
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import io
from PIL import Image
import time

## Se debe agregar el path donde se encuentra el archivo de "chromedriver"
PATH = "D:\\WebScraping\chromedriver.exe"

## Esta dirección se la alamacena en una variable llamada "wd"
wd = webdriver.Chrome(PATH)

## Se crea una función que permitirá obtener la dirección de cada imagen. Para ello, se pasa por parámetro la variable que contiene el path, el tiempo de delay
## y el máximo de imágenes que se van a buscar. 
def get_images_from_google(wd, delay, max_images):
	def scroll_down(wd):
		wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(delay)

	## Aquí se debe pegar la URL de la página donde se van a buscar las imágenes. Necesariamente deben ser imágenes del buscardor de google.
	url = "https://www.google.com/search?q=outfits+c%26a+hombres&tbm=isch&ved=2ahUKEwjJ7v2cuI76AhXnYTABHcNVDVcQ2-cCegQIABAA&oq=outfits+c%26a+hombres&gs_lcp=CgNpbWcQAzIGCAAQHhAIMgYIABAeEAgyBggAEB4QCDIGCAAQHhAIMgYIABAeEAgyBggAEB4QCFD4TliNUmCCU2gAcAB4AIABkQGIAZoCkgEDMC4ymAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=jrgeY8nvKufDwbkPw6u1uAU&bih=723&biw=1495&client=opera-gx&hs=Hsd"
	wd.get(url)

	image_urls = set()
	skips = 0

	## Se especifica que mientras no se alcance el límite de las imágenes especificadas, se seguirá deslizando la página hacia abajo. 
	while len(image_urls) + skips < max_images:
		scroll_down(wd)

		thumbnails = wd.find_elements(By.CLASS_NAME, "Q4LuWd")

		## Se recorre con un bucle for cada una de las imágenes para abrirlas
		for img in thumbnails[len(image_urls) + skips:max_images]:
			try:
				img.click()
				time.sleep(delay)
			except:
				continue
			
			## Si se continúa sin ningun error, se abre la imagen y se busca su "src" donde se especifica su URL.
			images = wd.find_elements(By.CLASS_NAME, "n3VNCb")
			for image in images:
				if image.get_attribute('src') in image_urls:
					max_images += 1
					skips += 1
					break
				
				## Al encontrar la información de la imagen, se la extrae mediante la función "get_attribute", de donde se obtiene la URL de la imagen
				if image.get_attribute('src') and 'http' in image.get_attribute('src'):
					image_urls.add(image.get_attribute('src'))
					print(f"Found {len(image_urls)}")

	return image_urls

## La función para la descarga de las imágenes, tiene 3 parámetros donde se obtiene la dirección donde se descargará la imagen, la URL y el nombre de la imagen. 
def download_image(download_path, url, file_name):
	try:
		image_content = requests.get(url).content
		image_file = io.BytesIO(image_content)
		image = Image.open(image_file)
		file_path = download_path + file_name

		## Se debe especificar el formato con el que la imagen se descargará, en este caso, es con un formato JPEG.
		with open(file_path, "wb") as f:
			image.save(f, "JPEG")

		print("Success")
	except Exception as e:
		print('FAILED -', e)

## Para obtener la URL de cada imagen, se llama a la función y se pasa por parámetro la variable que contiene el path, el número donde inicia y donde finaliza la búsqueda
## de las imágenes. 
urls = get_images_from_google(wd, 1,203)

## Se crea un contador que permite recorrer todo el array de URLs obtenidas y se llama a la función de descarga especificando los parámetros establecidos como el 
## nombre de la carpeta donde se guardarán las imágenes, la URL y el nombre, que en este caso será el número de la imagen más una abreviatura de la marca.
for i, url in enumerate(urls):
	download_image("cya/", url, str(i) +"cya"+ ".jpg")

wd.quit()
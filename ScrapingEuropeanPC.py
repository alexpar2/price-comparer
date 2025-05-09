
import pandas as pd
import numpy as np

import requests

from bs4 import BeautifulSoup

def scrapingEuropeanPC (busqueda):

    base_url = 'https://www.europeanpc.es/todo?texto='
    base_url_imagen = 'https://www.europeanpc.es/'
    busqueda.replace(" ", "+")
    url = base_url + busqueda

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'} 

    data = requests.get(url, headers=headers).content

    soup = BeautifulSoup(data, 'lxml')

    productos = []
    nombres = []
    precios = []
    imagenes = []
    enlaces = []
 
    # Iteramos sobre los elementos <p> cuya clase coincide con "product-name"
    for p in soup.find_all(['p'], class_=['product-name'], limit=10):
      # El nombre de los productos se encuentran enlaces, luego guardamos todos los
      # enlaces que se encuentran en estos <p> ya filtrados
      links = p.findAll('a')
      for a in links: # Recorremos estos enlaces para obtener los nombres
        nombres.append(a.get_text().strip())  # Añadimos a la lista de nombres
        enlace_imagen = base_url_imagen + a.get('href')
        enlaces.append(enlace_imagen)

    # Iteramos sobre los elementos <div> cuya 
    # clase coincide con "productinfo-precio"
    for div in soup.find_all(['div'], class_=['productinfo-precio'], limit=10):
      # El precio de los productos es el contenido estos div
      precios.append(div.get_text().strip())

    # Iteramos sobre los elementos <img> cuya
    # clase coincide con "productinfo-main-image"
    for img in soup.find_all(['img'], class_=['productinfo-main-image'], limit = 10):
       # La imagen de los productos es el contenido de src
       imagenes.append(img.get('src'))

    
    for i in range(10):
      nombre = nombres[i]
      precio = precios[i]
      imagen = imagenes[i]
      enlace = enlaces[i]
      productos.append({"nombre": nombre, "precio":precio, "imagen":imagen, "enlace":enlace})

    

    return productos




import pandas as pd
import numpy as np

import requests

from bs4 import BeautifulSoup

def busqueda_ho (busqueda):

    base_url = 'https://hardwareonline.com/module/iqitsearch/searchiqit?s='
    busqueda.replace(" ", "+")
    url = base_url + busqueda

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'} 

    data = requests.get(url, headers=headers).content

    soup = BeautifulSoup(data, 'lxml')

    productos = []
    enlaces =  []
    imagen = []
    nombres = []
    precios = []
 
    # Iteramos sobre los elementos <p> cuya clase coincide con "product-name"
    for p in soup.find_all(['h2'], class_=['h3 product-title'], limit=10) :
      # El nombre de los productos se encuentran enlaces, luego guardamos todos los
      # enlaces que se encuentran en estos <p> ya filtrados
      links = p.findAll('a')
      for a in links: # Recorremos estos enlaces para obtener los nombres
        enlaces.append(a.get('href'))
        nombres.append(a.get_text().strip())  # Añadimos a la lista de nombres

    # Iteramos sobre los elementos <div> cuya 
    # clase coincide con "productinfo-precio"
    for div in soup.find_all(['div'], class_=['product-price-and-shipping'],limit=10):
      # El precio de los productos es el contenido estos div
      precios.append(div.get_text().strip().replace("\xa0", ""))

    for img in soup.find_all(['img'], class_='img-fluid js-lazy-product-image lazy-product-image product-thumbnail-first', limit = 10):
      imagen.append(img.get('data-src'))

    for i in range(10):
      productos.append({"nombre": nombres[i], "enlace": enlaces[i], "imagen": imagen[i], "precio":precios[i]})

    return productos

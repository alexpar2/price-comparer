import requests
import json


def busqueda_api(termino):

    params = {
    'api_key': 'XXX',
    'type': 'search',
    'amazon_domain': 'amazon.es',
    'search_term': termino
  }

    # make the http GET request to Rainforest API
    api_result = requests.get('https://api.rainforestapi.com/request', params)

    # print the JSON response from Rainforest API
    data = api_result.json()

    # El módulo risky frisky te avisa si te quedan pocos créditos
    #risky_frisky = data["request_info"]["credits_remaining"]
    #if risky_frisky <= 50:
    #  print("Cuidado que te quedan pocos créditos")

    search_results = data["search_results"][:10]

    datos_recolectados = []


    #almaceno los datos de los primeros 10 resultados en datos_recolectados
    for resultado in search_results:       
        titulo = resultado["title"]
        precio = resultado["price"]["raw"]
        imagen = resultado["image"]
        enlace = resultado["link"]
        datos_recolectados.append({"nombre": titulo, "precio": precio, "imagen": imagen, "enlace":enlace})

  
    return datos_recolectados
    



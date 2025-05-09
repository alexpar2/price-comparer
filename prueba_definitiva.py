from prueba_api_def import busqueda_api
from ScrapingEuropeanPC import scrapingEuropeanPC
from ScrapingHardwareOnline import busqueda_ho


def busqueda(termino):
    resultados = []

    res_api = busqueda_api(termino)
    res_scrapper = scrapingEuropeanPC(termino)
    res_scrapper2 = busqueda_ho(termino)

    resultados.append({"api": res_api, "europa": res_scrapper, "ho": res_scrapper2})

    """
    for resultado in resultados:
        print("API:")
        for i, dato in enumerate (resultado["api"], 1):
            titulo = dato["nombre"]
            precio = dato["precio"]
            imagen = dato["imagen"]
            enlace = dato["enlace"]
            print(f"\n\n\nPRODUCTO NUMERO {i}\n\nNombre: {titulo}\n Precio: {precio}\n Imagen: {imagen}\n Enlace: {enlace}")

        print("\n\n\nEuropean PC:\n\n")
        for i, dato in enumerate (resultado["europa"], 1):
            titulo = dato["nombre"]
            precio = dato["precio"]
            imagen = dato["imagen"]
            enlace = dato["enlace"]
            print(f"\n\n\nPRODUCTO NUMERO {i}\n\nNombre: {titulo}\n Precio: {precio}\n Imagen: {imagen}\n Enlace: {enlace}")

        print("\n\n\n Hardware Online:\n\n")
        for i, dato in enumerate (resultado["ho"], 1):
            titulo = dato["nombre"]
            precio = dato["precio"]
            imagen = dato["imagen"]
            enlace = dato["enlace"]
            print(f"\n\n\nPRODUCTO NUMERO {i}\n\nNombre: {titulo}\n Precio: {precio}\n Imagen: {imagen}\n Enlace: {enlace}")
            """


        
    return resultados

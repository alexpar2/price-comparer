from flask import Flask, render_template, request
from jinja2 import Environment, FileSystemLoader
import requests
from prueba_api_def import busqueda_api
from ScrapingEuropeanPC import scrapingEuropeanPC
from ScrapingHardwareOnline import busqueda_ho

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")


@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    if request.method == 'POST':
        termino = request.form['termino']

        api = busqueda_api(termino)
        europa = scrapingEuropeanPC(termino)
        ho = busqueda_ho(termino)

 
        return render_template('resultados1.html', api=api, europa=europa, ho=ho)
    return render_template('index.html')




if __name__ == "__main__":
    app.run()
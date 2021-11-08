import re
from bs4 import BeautifulSoup
import requests
import pandas as pd



url= 'https://farmacorp.com/collections/salud-y-medicamentos/Salud-Respiratoria-y-Gripe'
page = requests.get(url)

htmlText=page.text

# Comprobamos que la petición nos devuelve un Status Code = 200

statusCode= page.status_code
if statusCode == 200:

    # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
    soup = BeautifulSoup(page.text,'html.parser')
    # Obtenemos todos los divs donde están las entradas
    entradas = soup.find_all('div', {'class': 'productitem--info'})

    # Recorremos todas las entradas para extraer
    #MEDICAMENTO
    #IMAGEN
    #PRECIO
    #CATEGORIA

    for h, entrada in enumerate(entradas):
        #medicamento = entrada.find('a')
        medicamento=entrada.find('h2',{'class': 'productitem--title'}).getText()
        precio = entrada.find('span',{'class':'money'}).getText()
        # Imprimo el Medicamento , Precio de las entradas
        print(h + 1, medicamento,precio)
else:
    # Si ya no existe la página y me da un 400
    print ("Status Code %d" % statusCode)

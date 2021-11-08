import re
from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime

#Funcion para limpiar los espacios y saltos de linea
def __limpiarTexto(texto):
    #Limpiamos saltos de linea, tabulaciones, dobles espacios
    nuevoTexto=texto.replace('\n','').replace('\r','').replace('\t','').replace('  ','')
    return (nuevoTexto)

url= 'https://farmacorp.com/collections/salud-y-medicamentos/Salud-Respiratoria-y-Gripe'
page = requests.get(url)

htmlText=page.text

# Comprobamos que la petición nos devuelve un Status Code = 200
statusCode= page.status_code

if statusCode == 200:
    #Capturamos la fecha de hoy para incluin el el dataset
    fechahoy= datetime.today().strftime('%Y-%m-%d %H:%M')
    # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
    soup = BeautifulSoup(page.text,'html.parser')
    # Obtenemos todos los divs donde están las entradas
    entradas = soup.find_all('div', {'class': 'productitem--info'})

    # Recorremos todas las entradas para extraer
    #MEDICAMENTO
    #IMAGEN
    #PRECIO
    #CATEGORIA
    listadoMedicamentos=list()
    listadoPrecios=list()

    for h, entrada in enumerate(entradas):
        medicamento=entrada.find('h2',{'class': 'productitem--title'}).getText()
        precio = entrada.find('span',{'class':'money'}).getText()
        # Imprimo el Medicamento , Precio de las entradas
        medicamento_textoLimpio=__limpiarTexto(medicamento)
        precio_textoLimpio=__limpiarTexto(precio)
        # Aderiamos los datos a cada lista
        listadoMedicamentos.append(medicamento_textoLimpio)
        listadoPrecios.append(precio_textoLimpio)
else:
    # Si ya no existe la página y me da un 400
    print ("Status Code %d" % statusCode)

df=pd.DataFrame({'Fecha':fechahoy,'Medicamento':listadoMedicamentos,'Precio':listadoPrecios},index=list(range(1,25)))
df.to_csv('MedicamentosScraper.csv')





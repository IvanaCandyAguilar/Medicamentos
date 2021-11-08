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
#Inicializamos las listas
listadoMedicamentos=list()
listadoPrecios=list()
#Capturamos la fecha de hoy para incluir el el dataset
fechahoy= datetime.today().strftime('%Y-%m-%d %H:%M')

#Iteramos por pagina en la web
for pagina in range(1,7):

    #asignamos la direccion url a utilizar como objeto de estudio
    #url= 'https://farmacorp.com/all'
    url= 'https://farmacorp.com/collections/all/salud-respiratoria-y-gripe?page='+str(pagina)
    page = requests.get(url)
    #print(url)
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
            #PRECIO

        for h, entrada in enumerate(entradas):
            # Extraemos mediante una busqueda los datos de medicamento y precio
            medicamento=entrada.find('h2',{'class': 'productitem--title'}).getText()
            precio = entrada.find('span',{'class':'money'}).getText()
            # Limpiamos los textos de Medicamento y Precio
            medicamento_textoLimpio=__limpiarTexto(medicamento)
            precio_textoLimpio=__limpiarTexto(precio)
            # Aderiamos los datos a cada lista
            listadoMedicamentos.append(medicamento_textoLimpio)
            listadoPrecios.append(precio_textoLimpio)
    else:
        # Si ya no existe la página y me da un 400
        print ("Status Code %d" % statusCode)

#creamos el dataframe
df=pd.DataFrame({'FechaCaptura':fechahoy,'NombreMedicamento':listadoMedicamentos,'PrecioUnitario':listadoPrecios})
#convertimos el dataframe en csv
df.to_csv('PreciosMedicamentosBolivia.csv')






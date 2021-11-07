from bs4 import BeautifulSoup
import requests
import pandas as pd

url= 'https://resultados.as.com/resultados/futbol/primera/clasificacion/'
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')

#EQUIPOS
equipo = soup.find_all('span',class_='nombre-equipo')

lista_equipos = list()

count=0

for i in equipo:
    if count<20:
        lista_equipos.append(i.text)
    else:
        break
    count += 1



#PUNTOS

pt = soup.find_all('td',class_='destacado')

lista_puntos = list()

countj=0

print(pt)

for j in pt:
    if countj<20:
        lista_puntos.append(j.text)
    else:
        break
    countj +=1

print(lista_puntos)

df=pd.DataFrame({'Nombre':lista_equipos,'Puntos':lista_equipos},index=list(range(1,21)))

print(df)

df.to_csv('Clasificacion.csv',index=False)



#url = 'https://www.promofarma.com'
#page = requests.get(url)
#soup = BeautifulSoup(page.content,'html.parser')

#medicamento = soup.find_all('h3',data_='productName')

#ListaMedicamentos = list()
#<h3 itemprop="name" data-qa-ta="productName">Star Care Mascarilla FFP2 Negra 10uds</h3>
#count=0
#for i in medicamento:
#    if count<20:
#        ListaMedicamentos.append(i.text)
#    else:
 #       break
  #  count+=1

#print(medicamento)

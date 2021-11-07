from bs4 import BeautifulSoup
import requests
import pandas as pd

url= 'https://farmacorp.com/collections/salud-y-medicamentos/Salud-Respiratoria-y-Gripe'
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')

#IMAGEN
#PRECIO
#CATEGORIA

#MEDICAMENTO

medicamento=soup.find_all('h2', class_="productitem--title")

lista_medicamentos = list()

count=0

for i in medicamento:
    if count<20:
            med= i.text
            med= med.replace('\n','')
            med =med.replace('  ','')
            lista_medicamentos.append(med)

    else:
        break
count +=1

#print(lista_medicamentos)

#PRECIO

precio=soup.find_all('span', class_="money")

lista_precios = list()

countj=0

for j in precio:
    if countj<20:
            precio= j.text
            precio= precio.replace('\n','')
            precio =precio.replace('  ','')
            precio = precio.replace(',','.')
            lista_precios.append(precio)
    else:
        break
countj +=1

print(lista_precios)



#df=pd.DataFrame({'Medicamento':lista_medicamentos,'Precio':lista_precios},index=list(range(1,20)))

#print(df)

#df.to_csv('Clasificacion.csv',index=False)



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

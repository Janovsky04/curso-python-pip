"""LA POBLACIÓN TOTAL EN los añ0s AÑO 2022, 2020 y 2015"""



#----- modulo para leer el acrhivo csv --------
import csv

# funcion abrir archivo
def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter= ',')

    #nombre de las columnas se encuentra en la primera fila
    header = next(reader)

    sum=0
    sum1=0
    sum2=0
    data = []
    for row in reader:
      iterable = zip(header, row) # une los valores de la listas en tuplas
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
      
      num=int(country_dict.get('2022 Population',0))
      sum=sum + num
      
      num1=int(country_dict.get('2020 Population',0))
      sum1=sum1 + num1
      
      num2=int(country_dict.get('2015 Population',0))
      sum2=sum2 + num2
           

    return sum, sum1, sum2

# correr archivo como script desde la terminal
if __name__ == '__main__':
  a, b, c = read_csv('./app/data.csv')
  
  print(f'La población mundial en el año 2015 es de {c} de habitantes')
  print(f'La población mundial en el año 2020 es de {b} de habitantes')
  print(f'La población mundial en el año 2022 es de {a} de habitantes')
  
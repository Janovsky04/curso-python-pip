#Reto: graficando la población de un país

import matplotlib.pyplot as plt
import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter= ',')

    #nombre de las columnas se encuentra en la primera fila
    header = next(reader)

    data = []
    for row in reader:
      iterable = zip(header, row) # une los valores de la listas en tuplas
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)


    return data


def generate_bar_chart(labels, values):

  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()


if __name__ == '__main__':

  data = read_csv('./app/data.csv')
  labels=[]
  values=[]
  list_arg=data[8]

  for  clave in list_arg:
    if clave == '2015 Population' or clave == '2020 Population' or clave=='2022 Population':
      labels.append(clave)
      num= list_arg.get(clave,0)
      values.append(int(num))
  
  

  print(labels)
  print(values)
  generate_bar_chart(labels, values)

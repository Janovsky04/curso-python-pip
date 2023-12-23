"""

def get_population():
  keys=['col', 'bol']
  values=[300, 400]
  return keys, values


A="Hola"

"""


#Ejercicio. Consiste en crear una función que reciba como parámetro una lista de palabras y retorne una lista con las que cumplan con la condición.

#Se imprimió en el main

def population_by_country(data, country):
  result = list(filter(lambda item: item['Country'] == country, data))
  return result



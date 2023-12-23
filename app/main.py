import utils

data = [{
    'Country': 'Colombia',
    'Population': 500
}, {
    'Country': 'Bolivia',
    'Population': 300
}]


def run():
  #Imprimiendo la llave y el valor
  keys, values = utils.get_population()
  print(keys, values)

  #Imprimiendo una variable
  print(utils.A)

  #Introducimos el país de forma dinámica.
  country = input('Type Country => ')

  result = utils.population_by_country(data, country)
  print(result)


#Si es ejecutado desde la terminal pues que ejecute el método run pero si es ejecutado desde otro archivo pues esto no se va a ajecutar

if __name__ == '__main__':
  run()

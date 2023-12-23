import cuarenta_utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('./app/data.csv')
  country = input('Type Country => ')
  

  result = cuarenta_utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = cuarenta_utils.get_population(country)
    charts.generate_bar_chart(labels, values)

if __name__=='__main__':
  run()

  
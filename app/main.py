import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('data.csv')
  country = input('Type Country => ')

  result = utils.population_by_country(data, country.title())

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels ,values)

  data_latam = list(filter(lambda item: item['Continent'] == 'South America', data))
  labels, values = utils.world_population_percentage(data_latam)
  charts.generate_pie_chart(labels, values)


if __name__ == '__main__':
  run()

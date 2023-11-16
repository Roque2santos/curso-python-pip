def get_population(datos_pais):
  poblacion = {}
  for label, value in datos_pais.items():
    if label[0:4].isdigit():
      poblacion[label[0:4]] = int(value)

  labels = poblacion.keys()
  values = poblacion.values()
  return labels,values

def population_by_country(data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country,data))
  return result


def world_population_percentage(data):
  countries = []
  porcentajes = []
  
  for dato in data:
    countries.append(dato['Country/Territory'])
    porcentajes.append(dato['World Population Percentage'])

  return countries, porcentajes
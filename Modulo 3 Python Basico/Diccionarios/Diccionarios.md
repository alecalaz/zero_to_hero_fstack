similares a las listas, pero se utilizan "Keys" en vez de indices

ej
my_dic = {
palabra : "Word"
}

print(my_dic[palabra])

output
Word

el metodo get para obtener keys de un diccionario para que no retorne error si el key no existe

print(my_dic.get(color))

Output
none

Metodo items para obtener ambos

for country, capital in europe_capitals_by_country.items():

  print(f'{country} : {capital}')


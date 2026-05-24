course_information = {
	'title': 'Introduction to DBs',
	'description': 'Here we review the basics of SQL Databases',
	'length_in_minutes': 600,
}

print(course_information['description'])

course_information = {
	'title': 'Introduction to DBs',
	'description': 'Here we review the basics of SQL Databases',
	'length_in_minutes': 600,
}

print(course_information.get('description'))


europe_capitals_by_country = {
	'spain' : 'madrid',
	'france' : 'paris',
	'germany' : 'berlin',
	'norway' : 'oslo',
}

for country, capital in europe_capitals_by_country.items():
  print(f'{country} : {capital}')

#iterando keys
europe_capitals_by_country = {
	'spain' : 'madrid',
	'france' : 'paris',
	'germany' : 'berlin',
	'norway' : 'oslo',
}

for country in europe_capitals_by_country.keys():
  print(country)

#iterando values
europe_capitals_by_country = {
	'spain' : 'madrid',
	'france' : 'paris',
	'germany' : 'berlin',
	'norway' : 'oslo',
}

for capital in europe_capitals_by_country.values():
  print(capital)

#Agregar datos
user_data = {
	'full_name': 'John Snow',
	'email': 'j.snow@gmail.com',
}

user_data['password'] = 'WinterIsComing2023'
print(user_data)

#eliminar datos
student_information = {
	'first_name': 'Harry',
	'last_name': 'Potter',
	'age': 17,
}

deleted_item = student_information.pop('last_name')
print(student_information)
print(f'Deleted item: {deleted_item}')

#Dic gatos de la casa

gatos = [
    {"name" : "Gonzalo",
   "age" : 3,
   "color": "Gris",
   "peso": "4 kilos"},
   {"name": "Nina",
    "age": 1,
    "color": "Blanca y negro",
    "peso": "2 kilos"},
    {"name": "Luly",
    "age": 10,
    "color": "gris",
    "peso": "4 kilos"}
]
#iterando usando values
for key, value in gatos[2].items():
    print(f"{key} : {value}")
gatos[2]['Vacunas'] = "Si"
print(gatos[2])
#solicitar un texto y contar cuantas veces aparece un caracter en el texto
def count_characters(string, char):
    count = 0
    for letter in string:
        if letter == char:
            count += 1
    return f"Se a encontrado {count} veces el caracter"

print(count_characters("Lyfter es una academia excelente de programacion", "a")) # Se a encontrado 2 veces el caracter

#Cree una función que reciba una lista de palabras y un número n, y retorne una nueva lista con solo las palabras que tengan más de n letras
def words_longer_than_n(words_list, n):
    longer_than_n = []
    for word in words_list:
        if len(word) > n:
            longer_than_n.append(word)
    return longer_than_n

word_list = ["cielo","sol","maravilloso","día"]

print(words_longer_than_n(word_list, int(input("Ingrese el numero de letras minimas en la palabra: "))))

#Cree una función que reciba un string y retorne cuántas vocales contiene
def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for letter in string:
        if letter in vowels:
            count += 1
    return count
print(count_vowels("Lyfter es una academia excelente de programacion"))

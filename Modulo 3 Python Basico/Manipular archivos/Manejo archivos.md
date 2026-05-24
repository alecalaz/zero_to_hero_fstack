Si no se especifica el modo de apertura por defecto es read only
r read
w write crea archivos si no existe
a append crea archivos si no existe
x crear crea archivos si no existe

funcion read para archivos de texto manejables
funcion readlines() texto mas grande


---Write---

write()
writelines()


--append--

def append_to_file(path, extra_text):

    with open(path, 'a', encoding='utf-8') as file:

        # Añadimos un salto de línea antes del nuevo texto para no pegarlo al anterior

        file.write("\\n" + extra_text)

  

additional_text = "Hechas, pues, estas prevenciones, no quiso aguardar más tiempo a poner en efeto su pensamiento..."

  

append_to_file('quijote_capitulo2.txt', additional_text)



rutas relativas y absolutas

# Ejemplo usando una ruta absoluta en Windows
# Evitamos este tipo de ruta para que nuestro código sea portable
absolute_file = open('C:\\Users\\Documents\\Projects\\quijote.txt')

# Ejemplo usando una ruta relativa 
# Se busca en la misma carpeta donde ejecutamos el script
relative_file = open('quijote.txt')


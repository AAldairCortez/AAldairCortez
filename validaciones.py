""" Ejemplo 1 
import re
texto = "En esta cadena se encuentra una palabra mágica"
resultado = re.search('mágica', texto)
print (resultado) """


""" Ejemplo 1.2 
import re
texto = "En esta cadena se encuentra una palabra mágica"
resultado = re.search('mágica', texto)
print (resultado) """


""" Ejemplo 2
import re
texto = "En esta cadena se encuentra una palabra mágica"
palabra = "magica"
encontrado = re.search('mágica', texto)
print (encontrado)
if encontrado:
    print("Se ha encontrado la palabra:", palabra)
else:
    print("No se ha encontrado la palabra:", palabra) """


""" Ejemplo 2.1
import re
texto = "En esta cadena se encuentra una palabra mágica"
palabra = "Hola"
encontrado = re.search('mágica', texto)
print (encontrado)
if encontrado:
    print("Se ha encontrado la palabra:", palabra)
else:
    print("No se ha encontrado la palabra:", palabra) """

""" Ejemplo 3 
import re
texto = "En esta cadena se encuentra una palabra mágica"
encontrado = re.search('mágica', texto)
# Posición donde empieza la coincidencia
print( encontrado.start() ) 
# Posición donde termina la coincidencia
print( encontrado.end() )  
# Tupla con posiciones donde empieza y termina la coincidencia
print( encontrado.span() )   
# Cadena sobre la que se ha realizado la búsqueda
print( encontrado.string )   """


""" Ejemplo 4  
import re 
texto = "Hola mundo "
resultado = re.match('Hola', texto)
print(resultado) """


""" Ejemplo 5 
import re
texto = "Vamos a dividir esta cadena"
resultado = re.split(' ', texto)
print(resultado)
 """


""" Ejmeplo 6 
import re
texto = "Hola amigo"
resultado = re.sub('amigo', 'amiga', texto)
print(resultado) """


""" Ejemplo 7 
import re 
texto = "hola adios hola hola"
resultado = re.findall('hola', texto)
print (resultado)
 """

""" Ejemplo 7.1
import re 
texto = "hola adios hola hola"
resultado = len(re.findall('hola', texto))
print (resultado) """

""" Ejemplo 7.2 
import re 
texto = "hola adios hello bye"
resultado = re.findall('hola|hello', texto)
print (resultado) """


import re 
texto = "hla hola hoola hooola hooooola"
resultado = len(re.findall('o', texto))
print (resultado) 








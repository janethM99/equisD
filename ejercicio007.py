"""
STRING Y mas
"""

esto_es_string="HOLA como estas"
esto_es_otro_string = "MUNDO"

#concatenar
print (esto_es_string+ '' + esto_es_otro_string)
#hola mundo

#MAYUS
print(esto_es_string.upper())

#minus
print(esto_es_string.lower())
#minus
print(esto_es_string.capitalize())
#primera letra de cada palabra
print(esto_es_string.title())
#dice la longitud del string
print(len(esto_es_string))

#buscar un caracter y muestra su ubicacion en indice 
print(esto_es_string.find('e'))
#rebanar!!!!! o slice
print(esto_es_string[0:2])#ho tu le dices que inicie un cero
print(esto_es_string[:2]) #ho el asume que inicia en cero
print(esto_es_string[5:9])

#radar
variable = 'radar'
print(variable[::])
print(variable[:-1])
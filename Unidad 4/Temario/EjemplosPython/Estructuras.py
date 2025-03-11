print("LISTAS")
# Ejemplo de una lista. Pilotos oficiales de Ferrari en 2014.
Ferrari2014 = ["Fernando Alonso", "Kimi Raikkonen"]
print(Ferrari2014)

# Ejemplo de otra lista. Pilotos oficiales de Ferrari en 2013.
Ferrari2013 = ["Fernando Alonso", "Felipe Massa"]
print(Ferrari2013)

# Acceder a un elemento de la lista.
print(Ferrari2014[1])

# pop: Extraemos a Kimi (que está en la posición número 1) de la lista. Alonso está en la posición 0.
Ferrari2014.pop(1)
print(Ferrari2014)

# append: Añadimos a Kimi al final de la lista
Ferrari2014.append("Kimi Raikkonen")
print(Ferrari2014)

# del:Eliminamos el elemento de la primera posición de la lista (Fernando)
del (Ferrari2014[0])

# insert: Añadimos a Fernando en la primera posición
Ferrari2014.insert(0, "Fernando Alonso")
print(Ferrari2014)

# extend: Juntamos los pilotos del 2013 y los del 2014. Fernando estará repetido.
Ferrari2014.extend(Ferrari2013)
print(Ferrari2014)

# remove: Borramos la primera vez que aparece Fernando Alonso
Ferrari2014.remove("Fernando Alonso")
print(Ferrari2014)

print("DICCIONARIOS")
diccionario = {'Piloto 1': 'Fernando Alonso', 'Piloto 2': 'Kimi Raikkonen', 'Piloto 3': 'Felipe Massa'}
print(diccionario)

# get(): Devuelve el valor que corresponde con la key introducida.
print(diccionario.get('Piloto 1'))

# pop(): Devuelve el valor que corresponde con la key introducida, y luego borra la key y el valor.
print(diccionario.pop('Piloto 1'))
print(diccionario)

# update(): Actualiza el valor de una determinada key o lo crea si no existe.
diccionario.update({'Piloto 4': 'Lewis Hamilton'})
diccionario.update({'Piloto 2': 'Sebastian Vettel'})
print(diccionario)

# "key" in diccionario: devuelve verdadero (True) o falso (False) si la key existe en el diccionario.
print("Piloto 1" in diccionario)
print("piloto 1" in diccionario)
print("Sebastian Vettel" in diccionario)

# "definición" in diccionario.values(): devuelve verdadero (True) o falso (False)
# si la definición existe en el diccionario.
print("Sebastian Vettel" in diccionario.values())

# del diccionario['key']: Elimina el valor (y el key) asociado a la key indicada.
del diccionario['Piloto 2']
print(diccionario)

print("CONJUNTOS")
lista = ['Fernando', 'Fernando', 'Felipe']
print(lista)

lista = list(set(lista))
print(lista)

divisas={'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

divisa = input("Introduce una divisa (Euro, Dollar, Yen): ").capitalize()

if divisa in divisas:
    print(f"El símbolo del {divisa} es {divisas[divisa]}")
else:
    print(f"La divisa {divisa} no está disponible.")
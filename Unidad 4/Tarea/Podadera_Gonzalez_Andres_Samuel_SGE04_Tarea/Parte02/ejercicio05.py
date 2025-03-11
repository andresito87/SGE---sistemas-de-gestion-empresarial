def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("Error: El número no puede ser negativo.")
            else:
                return valor  # Sale del bucle cuando el valor es válido
        except ValueError:
            print("Error: Debes ingresar un número entero válido.")

veces_a_imprimir=pedir_entero("¿Cuántas veces deseas imprimir tu nombre? ")
nombre=input("¿Cuál es tu nombre? ")

for i in range(veces_a_imprimir):
    print(f"{nombre}")
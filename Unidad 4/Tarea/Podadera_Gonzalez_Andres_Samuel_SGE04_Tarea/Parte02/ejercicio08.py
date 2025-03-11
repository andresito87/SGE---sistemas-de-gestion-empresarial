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

edad=pedir_entero("¿Cuál es tu edad? ")
for i in range(1,edad+1):
    print(f"Has cumplido {i} años")
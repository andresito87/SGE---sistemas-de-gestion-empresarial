def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)  # Llamada recursiva

def pedir_entero_positivo(mensaje):
    while True:
        try:
            num = int(input(mensaje))
            if num < 0:
                print("Error: Debes ingresar un número entero positivo.")
            else:
                return num
        except ValueError:
            print("Error: Entrada no válida. Debes ingresar un número entero.")

# Solicitar el número validado
num = pedir_entero_positivo("Introduce un número entero positivo: ")
print(f"El factorial de {num} es {factorial(num)}")
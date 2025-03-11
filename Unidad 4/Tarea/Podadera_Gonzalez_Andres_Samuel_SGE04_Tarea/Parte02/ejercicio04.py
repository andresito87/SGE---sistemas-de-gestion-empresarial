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

def pedir_flotante(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("Error: El número no puede ser negativo.")
            else:
                return valor  # Sale del bucle cuando el valor es válido
        except ValueError:
            print("Error: Debes ingresar un número válido.")

# Solicitar los datos con validación
horas_trabajadas = pedir_entero("¿Cuántas horas de trabajo? ")
coste_por_hora = pedir_flotante("¿Cuál es el coste por hora? ")

# Calcular el salario
salario = horas_trabajadas * coste_por_hora
print(f"El salario total es: {salario:.2f}€")

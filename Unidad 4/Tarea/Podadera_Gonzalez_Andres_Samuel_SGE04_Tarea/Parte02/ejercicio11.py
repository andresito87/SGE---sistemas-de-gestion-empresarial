nombre=input("¿Cuál es tu nombre? ")
edad=input("¿Cuál es tu edad? ")
direccion=input("¿Cuál es tu dirección? ")
telefono=input("¿Cuál es tu número de teléfono? ")

datos_usuario={'nombre':nombre,
               'edad':edad,
               'direccion':direccion,
               'telefono':telefono}

print(f"{datos_usuario['nombre']} tiene {datos_usuario['edad']} años, vive en {datos_usuario['direccion']} y su número de teléfono es {datos_usuario['telefono']}")
nombre = []
while True:
    Nombre = input("Nombre: ")
    if Nombre == "fin":
        break
    Telefono = input("Tu numero de telefono: ")
    linea = {}
    linea["Nombre"] = Nombre
    linea["Tu numero de telefono"]= Telefono
    nombre.append(linea)
for linea in nombre:
    print(nombre)
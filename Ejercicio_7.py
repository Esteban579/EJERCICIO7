#Ejercicio de clase 7

lista_coches = []
while True:
    Marca = input("Marca del coche: ")
    if Marca == "fin":
        break
    Modelo = input("Modelo del coche: ")
    Combustible = input("Combustible del coche: ")
    Cilindrada = input("Cilindrada del coche: ")
    linea = {}
    linea["Marca del coche"] = Marca
    linea["Modelo"]= Modelo
    linea["Combustible"] = Combustible
    linea["Cilindrada"] = Cilindrada
    lista_coches.append(linea)
for linea in lista_coches:
    print(lista_coches)
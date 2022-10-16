numeros = []
num1 = numeros.append(input("Añade un numero: "))
num2 = numeros.append(input("Añade un numero: "))
num3 = numeros.append(input("Añade un numero: "))
if numeros[0] == 0:
    print("Error")
elif numeros[0] < numeros[1] < numeros[2]:
    print("Los números están en orden ascendente")
else:
    print("Los números no están en orden ascendente")
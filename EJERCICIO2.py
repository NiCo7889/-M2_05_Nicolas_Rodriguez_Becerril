numeros = []
num1 = numeros.append(input("Añade un numero: "))
num2 = numeros.append(input("Añade un numero: "))
num3 = numeros.append(input("Añade un numero: "))
if numeros[0] < numeros[1] < numeros[2]:
    print("Están en orden ascendente")
elif numeros[0] == 0:
    print("Error")
else:
    print("No están en orden ascendente")
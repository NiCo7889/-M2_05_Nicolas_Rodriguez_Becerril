num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce un número: "))
num3 = int(input("Introduce un número: "))
if num1 == 0:
   print("Error")
elif num1 < num2 < num3:
   print("Están en orden ascendente. ")
else:
   print("No están en orden ascendente. ")
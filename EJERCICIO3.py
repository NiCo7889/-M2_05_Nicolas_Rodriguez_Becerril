frase = input("Introduce una frase: ")
conteo = {}
for letra in frase:
  if letra not in conteo:
    conteo[letra] = 1
  elif frase == ".":
     break
#Añadiendo esto al programa se podría ver el número de veces que aparece cada caracter en la frase:
   #for k, v in conteo.items():
     #print("{}: {}".format(k, v))
    
print("La letra 'a' aparece:", frase.count('a'), "veces")
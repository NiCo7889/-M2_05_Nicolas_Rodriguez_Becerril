frase = "A ver cuantos caracteres hay en esta frase."
conteo = {}
for letra in frase:
  if letra not in conteo:
    conteo[letra] = 1
  else:
    conteo[letra] += 1

for k, v in conteo.items():
  print("{}: {}".format(k, v))

print("La letra 'a' aparece:", 'A ver cuantos caracteres hay en esta frase.'.count('a'), "veces")
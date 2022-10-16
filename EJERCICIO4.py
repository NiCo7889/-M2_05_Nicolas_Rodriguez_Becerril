lista_palabras = ["hamburguesa", "pizza", "pasta"]
for palabra in lista_palabras: 
  print(palabra, ",", "longitud:", len(palabra))
longitud_mayor = 0
palabra_mas_larga = None
for palabra in lista_palabras: 
    if len(palabra) >= longitud_mayor:
        longitud_mayor = len(palabra)
        palabra_mas_larga = palabra
      
print("la palabra con más caracteres es:", palabra_mas_larga)
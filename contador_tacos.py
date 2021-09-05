def contar_tacos(familia, menu = True):

    pastel = 500/5
    botana_Lu = 390/5
    botana_Bren = 500/5

    orden = {
      "taco normal": 0,
      "enchiloso": 0}

    print(f"Calculando los tacos de la familia de {familia[0]} ...")

    while menu == True:
      
      try: 
        taco_n = input("Tacos normales: ")
        orden["taco_normal"] = int(taco_n)

        taco_e = input("Tacos enchilosos: ")
        orden["enchiloso"] = int(taco_e)

        menu = False

      except ValueError:
        print('Por favor utiliza numeros enteros para indicar cuantos tacos, no palabras')
    
    cuenta = (orden["taco_normal"] * 40) + (orden["enchiloso"] * 50) + pastel + botana_Lu + botana_Bren - familia[1]
    respuesta = (f"La cuenta de {familia[0]} es de: ${cuenta}\n")
    
    return respuesta

if __name__ == '__main__':
    
    familias = [("Wendy",500),("Debbie",290),("Brendis",500),("Lu",390),("Papas",0)]
    
    for familia in familias:
        
        x = contar_tacos(familia)
        print(x)

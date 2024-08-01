print("Bienvenidos a la isla del Tesoro\nTu mision es en contrar el tesoro")
iz_der = input("Porfavor indicame si elijes izquierda o derecha?")
if iz_der == "derecha":
    print("Caiste en un hollo.\nEl juego ha Terminado")

if iz_der == "izquierda":
    nad_espe = input("Quieres nadar o esperar?\n")
    if nad_espe == "nadar":
        print("Lo siento fuiste atacado por una carpa muy enojada.\nEl juego ha termiando.")
        
    if nad_espe == "esperar":
        puertaColor = input("Que color de puerta eliges roja, Azul o Amarilla")
        if puertaColor == "roja":
            print("Fuiste quemado por fuego.\nEl juego ha terminado.")
         
        if puertaColor == "azul":
            print("Fuiste comido por bestias.\nEl Juego ha termiando")
             
        if puertaColor == "amarilla":
            print("¡Tu Ganaste!")

        else:
            print("El juego ha terminado")    
             
            
        
    
    









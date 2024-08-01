print("Bienvenidos a la isla del Tesoro\nTu mision es en contrar el tesoro")
iz_der = input("Porfavor indicame si elijes Izquierda \"izq\" o Derecha \"der\"?\n")
if iz_der == "der":
    print("Caiste en un hollo.\nEl juego ha Terminado")

if iz_der == "izq":
    nad_espe = input("Quieres Nadar \"nd\" o Esperar? \"sp\"\n")
    if nad_espe == "nd":
        print("Lo siento fuiste atacado por una carpa muy enojada.\nEl juego ha termiando.")
        
    if nad_espe == "sp":
        puertaColor = input("Elige un color de puerta Roja, Azul o Amarilla\n")
        if puertaColor == "Roja":
            print("Fuiste quemado por fuego.\nEl juego ha terminado.")
         
        elif puertaColor == "Azul":
            print("Fuiste comido por bestias.\nEl Juego ha termiando")
             
        elif puertaColor == "Amarilla":
            print("¡Tu Ganaste!")
        
        else:
            print("El juego ha terminado")    


print('''

                         vv
                     vvv^^^^vvvvv
                 vvvvvvvvv^^vvvvvv^^vvvvv
        vvvvvvvvvvv^^^^^^^^^^^^^vvvvv^^^vvvvv
    vvvvvvv^^^^^^^^^vvv^^^^^^^vvvvvvvvvvv^^^vvv
  vvvv^^^^^^vvvvv^^^^^^^vv^^^^^^^vvvv^^^vvvvvv
 vv^^^^^^^^vvv^^^^^vv^^^^vvvvvvvvvvvv^^^^^^vv^
 vvv^^^^^vvvv^^^^^^vvvvv^^vvvvvvvvv^^^^^^vvvvv^
  vvvvvvvvvv^^^v^^^vvvvvv^^vvvvvvvvvv^^^vvvvvvvvv
   ^vv^^^vvvvvvv^^vvvvv^^^^^^^^vvvvvvvvv^^^^^^vvvvvv
     ^vvvvvvvvv^^^^vvvvvv^^^^^^vvvvvvvv^^^vvvvvvvvvv^v
        ^^^^^^vvvv^^vvvvv^vvvv^^^v^^^^^^vvvvvv^^^^vvvvv
 vvvv^^vvv^^^vvvvvvvvvv^vvvvv^vvvvvv^^^vvvvvvv^^vvvvv^
vvv^vvvvv^^vvvvvvv^^vvvvvvv^^vvvvv^v##vvv^vvvv^^vvvvv^v
 ^vvvvvv^^vvvvvvvv^vv^vvv^^^^^^_____##^^^vvvvvvvv^^^^
    ^^vvvvvvv^^vvvvvvvvvv^^^^/\@@@@@@\#vvvv^^^
         ^^vvvvvv^^^^^^vvvvv/__\@@@@@@\^vvvv^v
             ;^^vvvvvvvvvvv/____\@@@@@@\vvvvvvv
             ;      \_  ^\|[  -:] ||--| | _/^^
             ;        \   |[   :] ||_/| |/
             ;         \\ ||___:]______/
             ;          \   ;=; /
             ;           |  ;=;|
             ;          ()  ;=;|
            (()          || ;=;|
                        / / \;=;\
''')


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


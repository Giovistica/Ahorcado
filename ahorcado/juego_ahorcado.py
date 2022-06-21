from funciones import*
from obtener_palabra import selecionador_palabra
#Juego de ahorcado


juego_activo=True

def jugar():
    
    global juego_activo
    
    while juego_activo:

        palabra=selecionador_palabra()
        palabra_escondida=ocultador_palabra(palabra)
        
        
        conjunto_de_letras=[]
        
        vidas=7

        while True:

            letra=ingresa_letra()
            conjunto_de_letras.append(letra)

            if letra in palabra:
                print("MUY BIEN!!")
                for i in range(len(palabra)):
                    if letra==palabra[i]:
                        palabra_escondida[i]=letra               
                        
                

            else:
                print(" La ", letra, " no esta en la palabra ")
                vidas-=1
                print("Te quedan", vidas, "vidas")
                if vidas==0:
                    print("PERDISTE el juego")
                    print("La palabra era:  ", palabra)
                    break
                else:
                    print("Intentalo de nuevo :)")    
            

            if "".join(palabra_escondida)==palabra:
                print("GANASTE !!")
                print("La palabra era: ", palabra)
                break 
            
            print("".join(palabra_escondida))
            print("Las opciones ya usadas fueron:  ", conjunto_de_letras)
            

        juego_activo=reiniciar_juego()
        

jugar()



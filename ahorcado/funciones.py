
def reiniciar_juego():

        while True: 
                print("Escriba SI para jugar nuevamente o NO para salir del juego ")
                jugar= input().upper()
                
                if jugar=="SI":
                            
                            return True
                            break
                
                elif jugar=="NO":
                        
                            print("NOS VIMOS! :)")
                            
                            
                            return False
                            break
                else:
                    print("Escribiste: " + jugar + ", ingresá Si o No")

def ocultador_palabra(parametro):

            palabra_escondida=list(parametro)
            
            palabra_escondida=["-" for var in palabra_escondida] 
            
            print("".join(palabra_escondida))
            
            return palabra_escondida

def ingresa_letra ():

        global letra
        
        while True:
        
                letra=input("ingresa una letra:  ").upper()
                
                if letra.isalpha() and len(letra)==1:
                
                        return letra
                        break
                else:
                        print("Eso no es UNA LETRA, vamos de nuevo ")
                        





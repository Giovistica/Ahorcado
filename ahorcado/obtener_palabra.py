from depurar_lista import palabras
from random import randint


def selecionador_palabra():
    
    indice=randint(0,len(palabras))
    palabra=palabras[indice]
    return palabra



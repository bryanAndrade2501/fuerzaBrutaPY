#Fuerza Bruta
#Bryan Andrade
from operator import length_hint
from tkinter import N
from tokenize import String


clave = "hola"
texto = "hola como estas"

def fuerzaBruta(texto, clave): 
    N = len(texto)
    M = len(clave) 
    for i in range(N-M):
        j = 0
        while j < M and clave[j] == texto[i+j]:
            j = j+1
        if j == M:            return i
    return -1
   
print(fuerzaBruta("hola como estas","a"))
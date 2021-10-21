# Import a library of functions called 'pygame'
import pygame
from main_functions import *

# Initialize the game engine
pygame.init()

#call main routine
ancho = int(input("Ancho de la ventana: "))
alto = int(input("Alto de la ventana: "))
size = (ancho, alto)
rojo = (255, 0, 0)
titulo = input("titulo simulador: ")
main2(size, titulo, rojo)

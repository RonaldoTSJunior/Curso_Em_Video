import pygame
pygame.init()
pygame.mixer.music.load('C:\\Users\\ronal\\Documents\\CURSO_EM_VIDEO\\Utilizando_Modulos_Do_Python\\10822.mp3')
pygame.mixer.music.play()
pygame.event.wait()
exit=input('Aperte Enter para finalizar')
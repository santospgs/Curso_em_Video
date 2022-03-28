#faça um programa queabra e reproduza o audio de um arquivo em mp3

import pygame

pygame.init()
pygame.mixer.music.load ('NewMail.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input()
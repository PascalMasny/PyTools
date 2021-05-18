#Imports
import pygame
import time

#Pygam init
pygame.init()

#Const
width  = 800
height = 600
dvdLogoSpeed = [1, 1]
backgroundColor = 0, 0, 0

#Screen
screen = pygame.display.set_mode((width, height))

#DVD 
dvdLogo = pygame.image.load("dvd-logo-white.png")
dvdLogoRect = dvdLogo.get_rect()

#Loop
while True:
    #Fill Color
    screen.fill(backgroundColor)
    #load DVD
    screen.blit(dvdLogo, dvdLogoRect)
    dvdLogoRect = dvdLogoRect.move(dvdLogoSpeed)

    #Move
    if dvdLogoRect.left < 0 or dvdLogoRect.right > width:
        dvdLogoSpeed[0] = -dvdLogoSpeed[0]
    if dvdLogoRect.top < 0 or dvdLogoRect.bottom > height:
        dvdLogoSpeed[1] = -dvdLogoSpeed[1]
    
    pygame.display.flip()
    time.sleep(10 / 1000)

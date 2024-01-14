import pygame
pygame.init()

screen = pygame.display.set_mode()
SCREEN_WIDTH = screen.get_width()
SCREEN_HEIGHT = screen.get_height()

player_image = pygame.image.load("assets/martin.png")
#load eggs images
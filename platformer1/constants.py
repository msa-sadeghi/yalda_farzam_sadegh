import pygame
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 640

ROWS = SCREEN_HEIGHT//32
COLS = SCREEN_WIDTH//32

print(ROWS, COLS)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FPS = 60
clock = pygame.time.Clock()

dirt_img = pygame.image.load("assets/dirt.png")
grass_img = pygame.image.load("assets/grass.png")
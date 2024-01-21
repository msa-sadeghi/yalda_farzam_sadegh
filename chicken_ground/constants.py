import pygame

pygame.init()

screen = pygame.display.set_mode()
SCREEN_WIDTH = screen.get_width()
SCREEN_HEIGHT = screen.get_height()
clock = pygame.time.Clock()
FPS = 60
player_image = pygame.image.load("assets/martin.png")
egg1_image = pygame.image.load("assets/egg1.png")
egg2_image = pygame.image.load("assets/egg2.png")
egg3_image = pygame.image.load("assets/egg3.png")
egg4_image = pygame.image.load("assets/egg4.png")

all_egg_images = [egg1_image, egg2_image, egg3_image, egg4_image]


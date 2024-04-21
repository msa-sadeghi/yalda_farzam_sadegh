import pygame
from soldier import Soldier


player = Soldier('player',200,200,3, 5)
enemy = Soldier('enemy',400,200,3, 5)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
CLOCK = pygame.time.Clock()
FPS = 60
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
moving_left = False
moving_right = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
    screen.fill((0,0,0))
    player.draw(screen) 
    player.move(moving_left, moving_right)       
    enemy.draw(screen) 
        
         
    pygame.display.update()
    CLOCK.tick(FPS)
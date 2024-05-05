import pygame
from soldier import Soldier


player = Soldier('player',200,200,3, 5, 20)
enemy = Soldier('enemy',400,200,3, 5, 10)

bullet_group = pygame.sprite.Group()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
CLOCK = pygame.time.Clock()
FPS = 60
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
moving_left = False
moving_right = False
shoot = False
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
            if event.key == pygame.K_SPACE:
                shoot = True
            if event.key == pygame.K_UP and player.alive:
                player.jump = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_SPACE:
                shoot = False
    screen.fill((0,0,0))
    pygame.draw.line(screen,(255,0,0) ,(0,300), (SCREEN_WIDTH,300), 4)
    player.draw(screen) 
    if player.alive:
        if shoot:
            player.shoot(bullet_group)
        if player.in_air:
            player.update_action(2)
        elif moving_left or moving_right:
            player.update_action(1)
        else:
            player.update_action(0)
    player.move(moving_left, moving_right) 
    player.update()      
    enemy.draw(screen)
    bullet_group.update(bullet_group, player, enemy) 
    bullet_group.draw(screen)
    enemy.update()
        
         
    pygame.display.update()
    CLOCK.tick(FPS)
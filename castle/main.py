from constants import *
from world import World
from castle import Castle
from enemy import Enemy
import random
from crosshair import MousePointer

Max_difficulty = 1000
level_difficulty = 0
last_spawn_time = pygame.time.get_ticks()
level = 1

enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

world = World()
castle = Castle(screen_width - 400, screen_height - 450)
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

mouse = MousePointer()
enemies_alive = 0
next_level = False
running = True
i = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if level_difficulty < Max_difficulty:
        if pygame.time.get_ticks() - last_spawn_time > 2000:
            last_spawn_time = pygame.time.get_ticks()
            random_index = random.randint(0,3)
            Enemy(-50, screen_height-(300 - i * 20), enemy_group, all_animation_images[random_index],2, all_enemy_healths[random_index])
            level_difficulty += all_enemy_healths[random_index]
            i += 1
    if level_difficulty >= Max_difficulty:
        enemies_alive = 0
        for enemy in enemy_group:
            if enemy.alive:
                enemies_alive += 1
        if enemies_alive == 0:
            next_level = True
    
    print(enemies_alive)
    if next_level:
        next_level = False
        level += 1
        i = 0
        last_spawn_time = pygame.time.get_ticks()
        Max_difficulty *=1.1
        level_difficulty = 0
        enemy_group.empty()
        
        
    
    world.draw(screen)  
    mouse.draw(screen)
    castle.draw(screen) 
    castle.fire(bullet_group) 
    enemy_group.update(castle, bullet_group)    
    enemy_group.draw(screen)
    bullet_group.update()    
    bullet_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
    
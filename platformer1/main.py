from constants import *
from world import World

from player import Player
import os
import pickle

if os.path.exists("levels/level1"):
    f = open("levels/level1", "rb")
    world_data = pickle.load(f)
level = 1
def change_level()   :
    player.__init__()
    enemy_group.empty()
    door_group.empty()
    global level
    level += 1
    
    if os.path.exists(f"levels/level{level}"):
        f = open(f"levels/level{level}", "rb")
        world_data = pickle.load(f)
        
        game_world = World(world_data, enemy_group, door_group)
    return game_world
    
    

enemy_group = pygame.sprite.Group()
door_group = pygame.sprite.Group()
game_world = World(world_data, enemy_group, door_group)

player = Player()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((23,123,98))
    player.update(game_world.tile_map, enemy_group, door_group)
    
    game_world.draw()
    if player.alive:
        enemy_group.update()
    enemy_group.draw(screen)
    door_group.draw(screen)
    door_group.update()
    if player.next_level:
        game_world = change_level() 
    pygame.display.update()
    clock.tick(FPS)
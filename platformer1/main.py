from constants import *
from world import World
from levels.level1 import world_data
from player import Player
game_world = World(world_data)

player = Player()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((23,123,98))
    player.update(game_world.tile_map)
    game_world.draw()
    pygame.display.update()
    clock.tick(FPS)
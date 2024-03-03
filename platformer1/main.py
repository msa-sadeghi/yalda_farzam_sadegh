from constants import *
from world import World
from levels.level1 import world_data
from player import Player

enemy_group = pygame.sprite.Group()
game_world = World(world_data, enemy_group)

player = Player()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((23,123,98))
    player.update(game_world.tile_map, enemy_group)
    game_world.draw()
    if player.alive:
        enemy_group.update()
    enemy_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
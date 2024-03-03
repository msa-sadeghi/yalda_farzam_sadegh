from constants import *
from enemy import Enemy
class World:
    def __init__(self, world_data, enemy_group):
        self.tile_map = []
        self.enemy_group = enemy_group
        for i in range(ROWS):
            for j in range(COLS):
                if world_data[i][j] == 1:
                    img = pygame.transform.scale(dirt_img,(32,32))
                    rect = img.get_rect(topleft=(j * 32, i * 32))
                    self.tile_map.append((img, rect))
                if world_data[i][j] == 2:
                    img = pygame.transform.scale(grass_img,(32,32))
                    rect = img.get_rect(topleft=(j * 32, i * 32))
                    self.tile_map.append((img, rect))
                if world_data[i][j] == 3:
                    Enemy(j * 32, i * 32, self.enemy_group)
                    
                    
    def draw(self):
        for item in self.tile_map:
            screen.blit(item[0], item[1])
                
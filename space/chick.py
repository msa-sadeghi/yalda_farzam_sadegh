from constants import *
from pygame.sprite import Sprite

class Chick(Sprite):
    def __init__(self,x,y,chick_group, egg_group):
        super().__init__()
        self.image = pygame.image.load("assets/chick.png")
        self.rect = self.image.get_rect(topleft=(x,y))
        chick_group.add(self)
        self.direction = 1
        self.speed = 3
        
    def update(self):
        self.rect.x += self.direction * self.speed
        
        
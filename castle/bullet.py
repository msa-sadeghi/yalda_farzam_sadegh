from pygame.sprite import Sprite
from constants import *
import math
class Bullet(Sprite):
    def __init__(self, x,y,deg):
        super().__init__()
        self.image = bullet_image
        self.rect = self.image.get_rect(topleft=(x,y))
        self.deg = deg
    def update(self):
        
        self.rect.x += math.cos(self.deg) * 10
        self.rect.y += -math.sin(self.deg) * 10
        
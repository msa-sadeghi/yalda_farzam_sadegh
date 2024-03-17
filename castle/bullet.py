from pygame.sprite import Sprite
from constants import *
class Bullet(Sprite):
    def __init__(self, x,y,deg):
        self.image = bullet_image
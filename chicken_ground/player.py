from constants import *
from pygame.sprite import Sprite

class Player(Sprite):
    def __init__(self, image, x,y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y


    def draw(self):
        screen.blit(self.image, self.rect)
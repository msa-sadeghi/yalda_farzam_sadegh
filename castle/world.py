from constants import *
class World:
    def __init__(self):
        self.image = bg_image
        self.rect = self.image.get_rect(topleft=(0,0))
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
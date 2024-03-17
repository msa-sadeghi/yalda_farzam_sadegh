from constants import *
class Castle:
    def __init__(self,x,y):
        w = castle_100_image.get_width()
        h = castle_100_image.get_height()
        self.image = pygame.transform.scale(castle_100_image,\
        (w * 0.3, h * 0.3))
        self.rect = self.image.get_rect(topleft = (x,y))
        self.health = 1000
        self.max_health = 1000
        
    def draw(self,screen):
        screen.blit(self.image, self.rect)
        
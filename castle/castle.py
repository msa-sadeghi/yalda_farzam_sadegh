from constants import *
from bullet import Bullet
import math
class Castle:
    def __init__(self,x,y):
        w = castle_100_image.get_width()
        h = castle_100_image.get_height()
        self.image_100 = pygame.transform.scale(castle_100_image,\
        (w * 0.3, h * 0.3))
        self.image_50 = pygame.transform.scale(castle_50_image,\
        (w * 0.3, h * 0.3))
        self.image_25 = pygame.transform.scale(castle_25_image,\
        (w * 0.3, h * 0.3))
        self.image = self.image_100
        self.rect = self.image.get_rect(topleft = (x,y))
        self.health = 1000
        self.max_health = 1000
        
    def draw(self,screen):
        if self.health <= 250:
            self.image = self.image_25
        elif self.health <= 500:
            self.image = self.image_50
        else:
            self.image = self.image_100
        screen.blit(self.image, self.rect)
        
    def fire(self, bullet_group):
        mouse_pos = pygame.mouse.get_pos()
        y_d = -(mouse_pos[1] - self.rect.midleft[1])
        x_d = mouse_pos[0] - self.rect.midleft[0]
        angle = math.atan2(y_d, x_d)
        if pygame.mouse.get_pressed()[0]:
            b =Bullet(self.rect.midleft[0], self.rect.midleft[1], angle)
            bullet_group.add(b)
        
        
from constants import *
from pygame.sprite import Sprite

class Player(Sprite):
    def __init__(self, image, x,y):
        self.image = pygame.transform.scale(image, (image.get_width() * 0.6, image.get_height() * 0.6))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = 5
        self.lives = 3


    def draw(self):
        screen.blit(self.image, self.rect)
        
    def reset(self):
        self.rect.bottom = SCREEN_HEIGHT
        self.rect.centerx = SCREEN_WIDTH/2
        
    def move(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP] and self.rect.top > 100:
            self.rect.y -= self.speed
            
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT - 100:
            self.rect.y += self.speed
            
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
            
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
            
            
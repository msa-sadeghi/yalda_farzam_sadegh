from constants import *
from pygame.sprite import Sprite
from bullet import Bullet
class Player(Sprite):
    def __init__(self, bullet_group):
        super().__init__()
        self.image = pygame.image.load("assets/space.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH/2
        self.rect.bottom = SCREEN_HEIGHT
        self.bullet_group = bullet_group
        self.shoot = False
        
    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] and not self.shoot:
                self.fire()
                self.shoot = True
        if not pygame.mouse.get_pressed()[0]:
            self.shoot = False
                
        screen.blit(self.image, self.rect)
        print(len(self.bullet_group))
        
        
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += 5
            
    def fire(self):
        Bullet(self.rect.centerx, self.rect.top, self.bullet_group)
        
from pygame.sprite import Sprite
from constants import *
class Player(Sprite):
    def __init__(self):
        super().__init__()
        self.right_images = []
        self.left_images = []
        for i in range(1,5):
            img = pygame.image.load(f"assets/guy{i}.png")
            self.right_images.append(img)
            left_img = pygame.transform.flip(img, True, False)
            self.left_images.append(left_img)
            
        self.frame_index = 0
        self.image = self.right_images[self.frame_index]
        self.rect = self.image.get_rect(topleft=(100,100))
        self.update_animation_time = pygame.time.get_ticks()
        self.moving_status = False
        self.speed = 5
        
    def update(self):
        self.move()
        self.animation()
        screen.blit(self.image, self.rect)
        
    def move(self):
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.moving_status = True
            dx += self.speed
        if keys[pygame.K_LEFT]:
            self.moving_status = True
            dx -= self.speed
        if not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            self.moving_status = False
            
    def animation(self):
        if pygame.time.get_ticks() - self.update_animation_time > 200:
            self.frame_index += 1
            if self.frame_index >= len(self.right_images):
                self.frame_index = 0
            self.update_animation_time = pygame.time.get_ticks()
        if not self.moving_status:
            self.image = self.right_images[0]
        else:
            self.image = self.right_images[self.frame_index]
            
        
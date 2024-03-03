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
        self.direction = 1
        self.yspeed = 0
        self.alive = True
        self.ghost_image = pygame.image.load("assets/ghost.png")
        
    def update(self, tile_map, enemy_group):
        if self.alive:
            self.move(tile_map, enemy_group)
            self.animation()
        else:
            self.image = self.ghost_image          
            
        screen.blit(self.image, self.rect)
        
    def move(self, tile_map, enemy_group):
        dx = 0
        dy = 0        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction = 1
            self.moving_status = True
            dx += self.speed
        if keys[pygame.K_LEFT]:
            self.direction = -1
            self.moving_status = True
            dx -= self.speed
        if not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            self.moving_status = False
        if keys[pygame.K_SPACE]:
            self.yspeed = -15
            
        dy += self.yspeed    
        self.yspeed += 1  
        
        for tile in tile_map:
            if tile[1].colliderect(self.rect.x + dx , self.rect.y, self.image.get_width(), self.image.get_height()):
                dx = 0                
            if tile[1].colliderect(self.rect.x , self.rect.y + dy, self.image.get_width(), self.image.get_height()):
                if self.yspeed >0:
                    self.yspeed = 0
                    dy = tile[1].top - self.rect.bottom
                elif self.yspeed <0:
                    dy = tile[1].bottom - self.rect.top
                    self.yspeed = 0
        if pygame.sprite.spritecollide(self, enemy_group, True):
            self.alive = False
            
         
        self.rect.x += dx
        self.rect.y += dy
            
    def animation(self):
        if pygame.time.get_ticks() - self.update_animation_time > 200:
            self.frame_index += 1
            if self.frame_index >= len(self.right_images):
                self.frame_index = 0
            self.update_animation_time = pygame.time.get_ticks()
        if not self.moving_status:
            self.frame_index = 0
        if self.direction == 1:
            self.image = self.right_images[self.frame_index]
        elif self.direction == -1:
            self.image = self.left_images[self.frame_index]
            
            
        
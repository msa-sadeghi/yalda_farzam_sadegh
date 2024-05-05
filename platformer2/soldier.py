from pygame.sprite import Sprite
import pygame
import os
from bullet import Bullet
class Soldier(Sprite):
    def __init__(self,char_type, x,y, scale, speed, ammo):
        super().__init__()
        self.speed = speed 
        self.direction = 1
        self.flip = False
        self.ammo = ammo
        self.health = 100
        self.alive = True
        self.vel_y = 0
        self.jump = False
        self.in_air = False
        self.animation_list =[]
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        self.shoot_cooldown = 20
        animation_types = ("Idle", "Run", "Jump","Death")
        for animation in animation_types:
            list1 = []
            num_of_images = len(os.listdir(f"assets/images/{char_type}/{animation}"))
            for i in range(num_of_images):
                img = pygame.image.load(f"assets/images/{char_type}/{animation}/{i}.png")
                img = pygame.transform.scale(img, (img.get_width() * scale, img.get_height() * scale))
                list1.append(img)
            self.animation_list.append(list1)
            
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect(center = (x,y))
        
    def draw(self, screen):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
        
    def move(self, moving_left, moving_right):
        dx = 0
        dy = 0
        if moving_left:
            dx -= self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx += self.speed
            self.flip = False
            self.direction = 1
        if self.jump and not self.in_air:
            self.vel_y = -15
            self.jump = False
            self.in_air = True
            
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
            
        dy += self.vel_y
        
        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom
            self.in_air = False
        
        self.rect.x += dx
        self.rect.y += dy
        
    def update(self):
        self.animation()
        self.shoot_cooldown -= 1
        if self.shoot_cooldown < 0:
            self.shoot_cooldown = 0
    
    def animation(self):
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > 100:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.animation_list[self.action]):
                self.frame_index = 0
        
    def update_action(self, new_action)    :
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
            
    def shoot(self, bullet_group):
        if self.ammo > 0 and self.shoot_cooldown == 0:
            self.shoot_cooldown = 20
            bullet = Bullet(self.rect.centerx + \
                (0.6 * self.rect.size[0] * self.direction), self.rect.centery, self.direction)
            bullet_group.add(bullet)
            self.ammo -= 1
            
        
        
            
        
        
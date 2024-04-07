from pygame.sprite import Sprite
import pygame
class Enemy(Sprite):
    def __init__(self, x,y, group, all_images, speed, health):
        super().__init__()
        self.all_images = all_images
        self.speed = speed
        self.health = health
        self.frame_index = 0
        self.action = 0
        self.image = self.all_images[self.action][self.frame_index]
        self.rect = self.image.get_rect(topleft=(x,y))
        group.add(self)
        self.last_update_time = pygame.time.get_ticks()
        self.last_attack_time = pygame.time.get_ticks()
        
        
    def update(self, castle):
        if self.action == 1:
            if pygame.time.get_ticks() - self.last_attack_time > 2000:
                castle.health -= 50
                self.last_attack_time = pygame.time.get_ticks()
            
        if self.action == 0:
            self.rect.x += self.speed
        if self.rect.right >= castle.rect.left:
            self.change_action(1)
        self.animation()
        
    def animation(self):
        self.image = self.all_images[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.last_update_time > 50:
            self.last_update_time = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.all_images[self.action]):
                self.frame_index = 0
                
    def change_action(self, new_action):
        if self.action != new_action:
            self.action = new_action
            
            
        
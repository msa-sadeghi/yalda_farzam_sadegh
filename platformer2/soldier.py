from pygame.sprite import Sprite
import pygame
import os

class Soldier(Sprite):
    def __init__(self,char_type, x,y, scale, speed):
        super().__init__()
        self.speed = speed 
        self.direction = 1
        self.flip = False
        
       
        self.alive = True
        self.vel_y = 0
        self.jump = False
        self.in_air = False
        self.animation_list =[]
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
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
        screen.blit(self.image, self.rect)
        
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
        self.rect.x += dx
        self.rect.y += dy
        
        
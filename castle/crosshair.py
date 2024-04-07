import pygame
class MousePointer:
    def __init__(self):
        self.image = pygame.image.load("assets/crosshair.png")
        w = self.image.get_width()
        h = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (w * 0.03, h * 0.03))
        pygame.mouse.set_visible(False)
        
    def draw(self, screen):
        screen.blit(self.image, pygame.mouse.get_pos())
        
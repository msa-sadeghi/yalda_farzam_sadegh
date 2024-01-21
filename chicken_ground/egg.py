from constants import *
from pygame.sprite import Sprite
import random
class Egg(Sprite):
    def __init__(self, image, x, y, type):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 1])
        self.velocity = random.randint(1, 5)
        self.type = type

    def update(self):
        self.rect.x += self.dx * self.velocity
        self.rect.y += self.dy * self.velocity
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.dx *= -1
        if self.rect.top <= 100 or self.rect.bottom >= SCREEN_HEIGHT - 100:
            self.dy *= -1

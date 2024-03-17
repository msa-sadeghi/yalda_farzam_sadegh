from constants import *
from world import World
from castle import Castle
world = World()
castle = Castle(screen_width - 400, screen_height - 450)
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    world.draw(screen)  
    castle.draw(screen)      
    pygame.display.update()
    clock.tick(FPS)
    
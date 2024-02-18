from constants import *

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((0,0,0))
    pygame.display.update()
    clock.tick(FPS)
from constants import *
from player import Player

my_player = Player(player_image, SCREEN_WIDTH/2,\
                    SCREEN_HEIGHT)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    my_player.draw()
    pygame.display.update()
from constants import *
from player import Player
from chick import Chick
chick_group = pygame.sprite.Group()
egg_group = pygame.sprite.Group()
player_bullet_group = pygame.sprite.Group()
my_player = Player(player_bullet_group)

level = 1

def spawn_chick():
    for i in range(4):
        for j in range(8):
            Chick(j * 96, i * 96  + 100,chick_group,egg_group)
            
spawn_chick()


def check_edge_collisions():
    on_edge = False
    for chick in chick_group:
        if chick.rect.left < 0 or chick.rect.right > SCREEN_WIDTH:
            on_edge = True
            break
    if on_edge:
        for chick in chick_group:
            chick.direction *= -1
            chick.rect.y += level * 10
        


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                my_player.fire()
    screen.fill((0,0,0))
    check_edge_collisions()
    chick_group.update()
    chick_group.draw(screen)
    player_bullet_group.update()
    player_bullet_group.draw(screen)
    my_player.move()
    my_player.draw()
    pygame.display.update()
    clock.tick(FPS)
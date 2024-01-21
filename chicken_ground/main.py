import random
from constants import *
from player import Player
from egg import Egg

level = 0
my_player = Player(player_image, SCREEN_WIDTH / 2, SCREEN_HEIGHT)
egg_group = pygame.sprite.Group()
target_egg_type = random.randint(0,3)
target_egg_image = all_egg_images[target_egg_type]
target_egg_rect = target_egg_image.get_rect()
target_egg_rect.bottom = 100
target_egg_rect.centerx = SCREEN_WIDTH/2

def start_new_level():
    global level
    level += 1
    for i in range(level):
        egg1 = Egg(egg1_image, random.randint(0, SCREEN_WIDTH), random.randint(100, SCREEN_HEIGHT - 100), 0)
        egg2 = Egg(egg2_image, random.randint(0, SCREEN_WIDTH), random.randint(100, SCREEN_HEIGHT - 100), 1)
        egg3 = Egg(egg3_image, random.randint(0, SCREEN_WIDTH), random.randint(100, SCREEN_HEIGHT - 100), 2)
        egg4 = Egg(egg4_image, random.randint(0, SCREEN_WIDTH), random.randint(100, SCREEN_HEIGHT - 100), 3)
        egg_group.add(egg1)
        egg_group.add(egg2)
        egg_group.add(egg3)
        egg_group.add(egg4)


start_new_level()


def draw():
    # TODO  نمایش دادن تصویر تخم مرغ تارگت
    # TODO  نمایش دادن امتیاز

def choose_new_target():
    pass







running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    screen.fill((0, 0, 0))
    my_player.draw()
    egg_group.update()
    egg_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)

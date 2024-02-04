import random
from constants import *
from player import Player
from egg import Egg

level = 0
score = 0
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
    screen.blit(target_egg_image, target_egg_rect)
    pygame.draw.rect(screen, (190, 10, 210), (0, 100, SCREEN_WIDTH, SCREEN_HEIGHT-200), 5)
    

def choose_new_target():
    global target_egg_image, target_egg_type
    new_target = random.choice(egg_group.sprites())
    target_egg_image = new_target.image
    target_egg_type = new_target.type


def check_colision():
    global score
    collided_egg = pygame.sprite.spritecollideany(my_player, egg_group)
    if collided_egg:
        if collided_egg.type == target_egg_type:
            collided_egg.remove(egg_group)
            score += 1
            if len(egg_group) != 0:
                choose_new_target()
            else:
                start_new_level()
        else:
            my_player.reset()
            

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    screen.fill((0, 0, 0))
    draw()
    check_colision()
    my_player.move()
    my_player.draw()
    egg_group.update()
    egg_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)

import pygame
screen_width = 1065
screen_height = 600
FPS = 60

castle_25_image = pygame.image.load("assets/castle/castle_25.png")
castle_50_image = pygame.image.load("assets/castle/castle_50.png")
castle_100_image = pygame.image.load("assets/castle/castle_100.png")

tower_25_image = pygame.image.load("assets/tower/tower_25.png")
tower_50_image = pygame.image.load("assets/tower/tower_50.png")
tower_100_image = pygame.image.load("assets/tower/tower_100.png")

armour_image = pygame.image.load("assets/armour.png")
bg_image = pygame.image.load("assets/bg.png")
bullet_image = pygame.image.load("assets/bullet.png")
crosshair_image = pygame.image.load("assets/crosshair.png")
repair_image = pygame.image.load("assets/repair.png")

all_animation_images = []
all_enemy_types = ("knight", "goblin", "purple_goblin", "red_goblin")
all_enemy_healths = (50, 75, 100, 125)
all_animations = ("walk", "attack", "death")

for enemy in all_enemy_types:
    enemy_list = []
    for anime in all_animations:
        anime_list = []
        for i in range(20):
            im = pygame.image.load(f"assets/enemies/{enemy}/{anime}/{i}.png")
            im_w = im.get_width()
            im_h = im.get_height()
            im = pygame.transform.scale(im, (im_w * 0.2, im_h * 0.2))
            anime_list.append(im)
        enemy_list.append(anime_list)
    all_animation_images.append(enemy_list)
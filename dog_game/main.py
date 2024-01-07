import pygame
pygame.init()
SCREEN = pygame.display.set_mode()
SCREEN_WIDTH = SCREEN.get_width()
SCREEN_HEIGHT = SCREEN.get_height()
score = 0
lives = 3
my_font = pygame.font.Font("assets/myfont.otf", 32)

score_text = my_font.render(f"Score: {score}", True, (100,20,150))
score_rect = score_text.get_rect()
score_rect.topleft = (0,0)

dog_image = pygame.image.load("assets/dog.png")
dog_rect = dog_image.get_rect()
dog_rect.bottom = SCREEN_HEIGHT
dog_rect.centerx = SCREEN_WIDTH/2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    SCREEN.blit(dog_image, dog_rect)
    SCREEN.blit(score_text, score_rect)
    pygame.display.update()
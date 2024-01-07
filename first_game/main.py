import random
import pygame

pygame.init()

def pause_game():
    global score, cow_lives, running,score_text,cow_lives_text
    game_over_text = font72.render("Game Over", True, (255,40,50))
    game_over_rect = game_over_text.get_rect()
    game_over_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    continue_text = font32.render("Press Enter to play again", True, (170,30,190))
    continue_rect = continue_text.get_rect()
    continue_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 50)

    score_text = font32.render(f"Score: {score}", True, (10, 240,100))
    cow_lives_text = font32.render(f"lives: {cow_lives}", True, (10,100,245))  
    screen.fill((0,0,0))
    screen.blit(title_text, title_rect)
    screen.blit(score_text, score_rect)
    screen.blit(cow_lives_text, cow_lives_rect)
    screen.blit(game_over_text, game_over_rect)
    screen.blit(continue_text, continue_rect)
    pygame.display.update()

    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    score = 0
                    cow_lives = 3
                    paused = False
            if event.type == pygame.QUIT:
                paused = False
                running  = False



SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 720
FPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

cow_image = pygame.image.load("cow.png")
cow_rect = cow_image.get_rect(bottomright=(SCREEN_WIDTH,SCREEN_HEIGHT))

#load milk image
milk_image = pygame.image.load("milk.png")
milk_rect = milk_image.get_rect()
milk_rect.topleft = (-100, random.randint(20, SCREEN_HEIGHT- 96))

font72 = pygame.font.Font("myfont.otf",72)
font32 = pygame.font.Font("myfont.otf",32)

title_text = font32.render("Cow Game", True, (240,30,197))
title_rect = title_text.get_rect(centerx = SCREEN_WIDTH/2 , top = 0)

score = 0
cow_lives = 3
milk_speed = 5

score_text = font32.render(f"Score: {score}", True, (10, 240,100))
score_rect = score_text.get_rect(top = 0, right=SCREEN_WIDTH)

cow_lives_text = font32.render(f"lives: {cow_lives}", True, (10,100,245))
cow_lives_rect = cow_lives_text.get_rect(left = 0, top = 0)


eat_sound = pygame.mixer.Sound("eat.wav")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # cow movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and cow_rect.top > 20:
        cow_rect.y -= 5
    if keys[pygame.K_DOWN] and cow_rect.bottom < SCREEN_HEIGHT:
        cow_rect.y += 5

    milk_rect.x += milk_speed

    if cow_rect.colliderect(milk_rect):
        milk_rect.topleft = (-100, random.randint(20, SCREEN_HEIGHT- 96))
        score += 1
        eat_sound.play()


    if milk_rect.left > SCREEN_WIDTH:
        milk_rect.topleft = (-100, random.randint(20, SCREEN_HEIGHT- 96))
        cow_lives -= 1

    if cow_lives <=0 :
        pause_game()


    score_text = font32.render(f"Score: {score}", True, (10, 240,100))
    cow_lives_text = font32.render(f"lives: {cow_lives}", True, (10,100,245))   
    screen.fill((0,0,0))
    screen.blit(cow_image, cow_rect)
    screen.blit(milk_image, milk_rect)
    screen.blit(title_text, title_rect)
    screen.blit(score_text, score_rect)
    screen.blit(cow_lives_text, cow_lives_rect)
    pygame.display.update()
    clock.tick(FPS)




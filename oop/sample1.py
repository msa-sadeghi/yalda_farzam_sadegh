import pygame
pygame.init()
class Dog:
    def __init__(self, name, age, gender, sound):
        self.name = name
        self.age = age
        self.gender = gender
        self.sound = sound
    def bark(self):
        print(f'{self.name} is barking')
        self.sound.play()  
    def eat(self):
        print(f"{self.name} is eating")
dog1 = Dog("jessi", 8, "girl",pygame.mixer.Sound("d.mp3"))
dog2 = Dog("peter",7, "boy", pygame.mixer.Sound("d.mp3"))
SCREEN = pygame.display.set_mode((200,200))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dog1.eat()
                dog1.bark()
            if event.key == pygame.K_RETURN:
                dog2.eat()
                dog2.bark()
    pygame.display.update()
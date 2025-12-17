import pygame #импорт библиотеки

pygame.init() #иниция библиотеки
screen = pygame.display.set_mode((600,300)) # flags=pygame.NOFRAME) #установка дисплея
pygame.display.set_caption("LuxOs")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

running = True
while running:
    ##screen.fill((174, 91, 91))
    pygame.display.update() #цикл на то, что бы дислей не закрывался
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #если 
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                screen.fill("white")
                

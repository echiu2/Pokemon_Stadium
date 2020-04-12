import pygame 

pygame.init()

background_color = (255,255,255)
red = (255,0,0)
blue = (0,0,128)

size = (720,480)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Pokemon Stadium')

font = pygame.font.Font('freesansbold.ttf', 32) 
text = font.render('Pokemon Stadium', True, red, blue)
text_border = text.get_rect()
text_border.center = (720//2, 480//2)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:         
            running = False
    
    screen.fill(background_color)
    screen.blit(text, text_border) 
    
    pygame.display.update()

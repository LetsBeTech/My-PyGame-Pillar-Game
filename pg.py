import pygame
from pygame.locals import *



#Colors
red = (255,0,0)
green = (0,255,0)
blue = (0,255,255)

#resolution of screen
res = (900,600)

#GameWindow
screen = pygame.display.set_mode(res)

#Title
pygame.display.set_caption("World's Hardest Game")
pygame.display.update()

font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, [x,y])


#Variables
init_velocity = 0.25

velocity_x = 0
rect_x = 300

velocity_x2 = 0
rect_x2 = 300

velocity_x3 = 0
rect_x3 = 300

velocity_x4 = 0
rect_x4 = 300

rect_y1 = 100
rect_y2 = 200
rect_y3 = 300
rect_y4 = 400

#velocity_y = 0



#GameLoop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            velocity_x = init_velocity
            velocity_x2 = -init_velocity
            velocity_x3 = init_velocity
            velocity_x4 = -init_velocity

    rect_x = rect_x + velocity_x
    rect_x2 = rect_x2 + velocity_x2
    rect_x3 = rect_x3 + velocity_x3
    rect_x4 = rect_x4 + velocity_x4

    if rect_x > 700 :
        velocity_x = -init_velocity

    if rect_x2 > 700:
        velocity_x2 = -init_velocity

    if rect_x3 > 700:
        velocity_x3 = -init_velocity

    if rect_x4 > 700:
        velocity_x4 = -init_velocity

    
    rect_x = rect_x + velocity_x
    rect_x2 = rect_x2 + velocity_x2
    rect_x3 = rect_x3 + velocity_x3
    rect_x4 = rect_x4 + velocity_x4

    if rect_x < 0:
        velocity_x = init_velocity

    if rect_x2 < 0:
        velocity_x2 = init_velocity

    if rect_x3 < 0:
        velocity_x3 = init_velocity

    if rect_x4 < 0:
        velocity_x4 = init_velocity

    rect_x = rect_x + velocity_x
    rect_x2 = rect_x2 + velocity_x2
    rect_x3 = rect_x3 + velocity_x3
    rect_x4 = rect_x4 + velocity_x4

    screen.fill((0,0,0))
    pygame.draw.rect(screen,red,[rect_x,rect_y1,200,25])
    pygame.draw.rect(screen,green,[rect_x2,rect_y2,200,25])
    pygame.draw.rect(screen,blue,[rect_x3,rect_y3,200,25])
    pygame.draw.rect(screen,(255,255,0),[rect_x4,rect_y4,200,25])
    
  
    pygame.display.update()

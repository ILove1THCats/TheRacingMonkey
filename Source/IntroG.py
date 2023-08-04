import pygame
import Menu

x = 1280
y = 720
x_title = x // 24
y_title = y // 14

#Create init
pygame.init()

screen = pygame.display.set_mode((x,y))
#Title for game
pygame.display.set_caption("The Racing Monkey")

#Backgroud game
white = (255,255,255)
screen.fill(white)

pygame.draw.rect(screen, (0,0,0), pygame.Rect(x_title-10,y_title,200,30), 1)
#Font and size
font = pygame.font.SysFont("Arial", 24)
titleGame = "The Racing Monkey"
label = font.render(titleGame, True, (0,100,0))
screen.blit(label, (x_title,y_title))

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
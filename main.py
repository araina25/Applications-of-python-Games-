import pygame

#initializing the pygame module
pygame.init()

#creating a screen with values 800 to 600 as the resolution

screen = pygame.display.set_mode((800,600))

#Setting the title
pygame.display.set_caption("Space Invaders")

#Adding an image on the screen 
image = pygame.image.load("image.jpg")
#X and Y coordinates for player 1 
x_1 = 400 
y_1 = 550

#showing player one on the screen
def player():
    pygame.blit(image,(x_1,y_1))


#The game loop and used for closing the window
program_run = True
while program_run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program_run = False
    #RGB -- Red, Green ,BLue
    screen.fill((255,0,0))
    player()
    pygame.display.update()



import pygame

#Initalize Pygame
pygame.init()

#Set up display dimensions
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

#Load player character image
player_image = pygame.image.load("player.png")
#determine initial position of the player character on screen
player_x = width // 2 - player_image.get_width() // 2
player_y = height - player_image.get_height()

#Game loop
running = True 
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    #Display player character
    screen.blit(player_image, (player_x, player_y))

    #Update display
    pygame.display.update()


pygame.quit()



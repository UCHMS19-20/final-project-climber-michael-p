import pygame
import sys
import random 

#initializing pygame
pygame.init()

#definitions
    #create screen 
screen = pygame.display.set_mode((400,800))    

    #create player
player_rect = pygame.Rect(200,200,50,100)

x_move = 0
#player_x = 50
#player_y = 50

#obstacles
boulders = [pygame.Rect(random.randint(0,600), 0, random.randint(10,20), random.randint(10,20))]

#difficulty
nice_mode = True

#main loop
while True:
    #clear screen by redrawing background
    screen.fill(pygame.Color("black"))
    #processing event queue
    for event in pygame.event.get():
       #ends game if x button is clicked
        if event.type == pygame.QUIT:
            sys.exit()
        # if event is KEYDOWN, then modify movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_move = -1
            if event.key == pygame.K_RIGHT:
                x_move = 1
        if event.type == pygame.KEYUP and nice_mode:
            x_move = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
           #this will change
            boulder.append(pygame.Rect()
        
        #updates x-position of player.rect
    player_rect.x += x_move

        #display character
    pygame.draw.rect(screen, pygame.Color("red"), player_rect)

    #update boulder position
    for boulder in boulder:
     boulders.y += 1
    #check for collisions
    if boulders.colliderect(player_rect):
                print("HAHA You Lose!")
    


#draw boulder
    pygame.draw.rect(screen, pygame.Color("white"), boulders[0])
    
#updates display so we can see
    pygame.display.flip()



# in event:
#     if event.type is key = pressed:
#         if key is left:
#             player_x -=1
#         elif key is right:
#             player_x += 1


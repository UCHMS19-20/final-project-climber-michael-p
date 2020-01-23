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

font = pygame.font.SysFont("Arial",50)
text = font.render("YOU LOSE!", True, (255,0,0))

x_move = 0
#player_x = 50
#player_y = 50

lost = False

#obstacles


def generate_boulders():
    sz = random.randint(5,20)
    rect = pygame.Rect(random.randint(0,400 - sz), 0, sz, sz)
    return rect

boulders = [generate_boulders()]

#difficulty
nice_mode = True

#main loop
while True:
    #clear screen by redrawing background
    screen.fill(pygame.Color("black"))
    if lost:
        screen.blit(text,(75
        ,10))

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
            boulders.append(generate_boulders())
        
        #updates x-position of player.rect
    if not lost:
        player_rect.x += x_move
        if player_rect.x < 0:
            player_rect.x = 0
        if player_rect.x > 400 - player_rect.w:
            player_rect.x = 400 - player_rect.w
    

        #display character
    pygame.draw.rect(screen, pygame.Color("red"), player_rect)

    #update boulder position
    # print(f"Player: {player_rect.x}, {player_rect.y}")
    for boulder in boulders:
        if not lost:
            boulder.y += 1
        # print(f"Boulder: {boulder.x}, {boulder.y}")
    #check for collisions
        if boulder.colliderect(player_rect):
            print("HAHA You Lose!")
            lost = True



#draw boulder
        pygame.draw.rect(screen, pygame.Color("white"), boulder)
    
#updates display so we can see
    pygame.display.flip()



# in event:
#     if event.type is key = pressed:
#         if key is left:
#             player_x -=1
#         elif key is right:
#             player_x += 1


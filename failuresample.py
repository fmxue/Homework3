import pygame
import time
import random
 
pygame.init()

empty=0
white = (255,255,255)
black = (0,0,0)
gray = (128,128,128)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
blue = (0,0,255)
display_width = 480
display_height = 480
 
gameDisplay = pygame.display.set_mode( (display_width,display_height) )
pygame.display.set_caption('Tic Tac Toe')
clock = pygame.time.Clock()
 
background = pygame.image.load('a.png')
def is_won():
    for val in range(3):
        if state[0][val] == state[1][val] == state[2][val] != empty:
            return state[0][val]              
        if state[val][0] == state[val][1] == state[val][2] != empty:                                 
            return state[val][0]                
        if state[0][0] == state[1][1] == state[2][2] != empty:            
            return state[1][1]
        if state[0][2] == state[1][1] == state[2][0] != empty:              
            return state[1][1]

def board(x, y):
    gameDisplay.blit(background, (x,y))
    
 
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
 
def message_diaplay(text):
    largeText = pygame.font.SysFont('comicsansms',48)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2) 
 
def button (msg, x, y, w, h, ic, ac, action=None):
        mouse =pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        print(click)
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
            if click[0] == 1 and action != None:
                action()
##                if action == "play":
##                    action()
##                if action == "quit":
##                    pygame.quit()
##                    quit()
        else:
            pygame.draw.rect(gameDisplay, ic, (x,y,w,h))
        smallText = pygame.font.SysFont('comicsansms', 20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)))
        gameDisplay.blit(textSurf, textRect)
 
def quitgame():
    pygame.quit()
    quit()
 
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        board(0,0)
        largeText = pygame.font.SysFont('comicsansms',72)
        TextSurf, TextRect = text_objects('Tic Tac Toe', largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.draw.line(gameDisplay,black,(0,160),(480,160),5)
        pygame.draw.line(gameDisplay,black,(0,320),(480,320),5)
        pygame.draw.line(gameDisplay,black,(160,0),(160,480),5)
        pygame.draw.line(gameDisplay,black,(320,0),(320,480),5)
        for row,line in enumerate(state):
            for col,val in enumerate(line):
                if val == -1:
                    upper_left=(col * 160 + 5 , row * 160 + 5)
                    lower_right=(col * 160 + 155 , row * 160 + 5)
                    pygame.draw.line(gameDisplay, red, upper_left, lower_right, 5)
                    upper_right = (col * 160 + 155, row * 160 + 5)
                    lower_left = (col * 160 + 5, row * 160 + 155)
                    pygame.draw.line(gameDisplay, red, upper_right, lower_left, 5)
                elif val == 1:
                #创建一个矩形.在矩形里画圆

                    rect = (col * 160 + 5, row * 160 + 5, 150, 150)
                    pygame.draw.ellipse(gameDisplay, blue, rect, 5)
                else:
                    assert val == empty
                    continue
        button("PLAYER FIRST", 80, 320, 160, 50, green, bright_green,PlayerGoesFirst)
        button("COMPUTER FIRST",240, 320, 160, 50, red, bright_red,ComputerGoesFirst)
        pygame.display.update()
        clock.tick(15)
'''def draw_O():
    while True:
          row = randint(0,2)
          col = randint(0,2)
          if state[row][col] == 0:
             state[row][col] = 1
             break
    game_intro()
    pygame.display.flip()'''
def PlayerGoesFirst():
    return 0
def ComputerGoesFirst():
    return 0
def begin():
    global state
    state = [[empty] * 3,[empty] * 3,[empty] * 3]
    game_intro()

begin()
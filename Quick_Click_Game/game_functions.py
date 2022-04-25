import pygame, sys
from pygame.locals import *
from block import *
import time



def CheckBlockDeletion(block, mouseX, mouseY):
    if (mouseX > block.x and mouseX < block.x + BLOCK_SIZE) and (mouseY > block.y and mouseY < block.y + BLOCK_SIZE):  # check if click was done to the block 
        return True
    return False

def ClickGame():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
    pygame.display.set_caption('Click Game')

    points = 0

    block = Block()

    block.CalculateCoords()
    block.PaintPosition(DISPLAYSURF)
    
    t_end = time.time() + 20      # Set the ending of the game to 20 seconds to the future for 20 seconds
    
    while True: # main game loop
        
        for event in pygame.event.get():
            if event.type == QUIT or time.time() >= t_end:      # Execute the game for 20 seconds
                pygame.quit()
                return points
                

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:      # Checks for mousedown event and specifically left click of mouse (button 1 --> left click)
                (mouseX, mouseY) = pygame.mouse.get_pos()
                if CheckBlockDeletion(block, mouseX, mouseY):
                    points += 1
                    block.CleanPosition(DISPLAYSURF)
                    block.CalculateCoords()
                    block.PaintPosition(DISPLAYSURF)
        
        pygame.display.set_caption(f'Points: {points}               Time Remaining: {round(t_end-time.time(),2)}')
        pygame.display.update()


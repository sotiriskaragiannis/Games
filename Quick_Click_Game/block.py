import pygame
from pygame.locals import *
import random

BLOCK_SIZE = 50

# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE = (  0,   0, 255)

WINDOW_X = 1300
WINDOW_Y = 1300


class Block():
    def __init__(self):
        pass

    def CalculateCoords(self):
        self.x = random.randint(0, (WINDOW_X-BLOCK_SIZE)/BLOCK_SIZE) * BLOCK_SIZE     # Calculate a random coordinate that is a multiple of BLOCK_SIZE
        self.y = random.randint(0, (WINDOW_Y-BLOCK_SIZE)/BLOCK_SIZE) * BLOCK_SIZE
            
    def PaintPosition(self, screen):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))

    def CleanPosition(self, screen):
        pygame.draw.rect(screen, BLACK, (self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))
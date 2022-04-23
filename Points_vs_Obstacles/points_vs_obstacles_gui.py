import pygame, sys
from pygame.locals import *
import random

PLAYER_SIZE = 25

# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE = (  0,   0, 255)

WINDOW_X = 250
WINDOW_Y = 250


def DetermineMotion(event, player):
    if event.type == pygame.KEYDOWN:      # Check if a key has been pressed
        player.move(event.key)


def PrintRandomObstacles(point, player):
    obstacles = []
    for y in range(0, WINDOW_Y, PLAYER_SIZE):
        for x in range(0, WINDOW_X, PLAYER_SIZE):
            chance = random.randint(0, 15)
            if chance == 1:
                if not (point.x == x and point.y == y) and not (player.x == x and player.y == y):           # Check for point or player overlapping with object.
                    pygame.draw.rect(DISPLAYSURF, RED, (x, y, PLAYER_SIZE, PLAYER_SIZE))
                    obstacles.append((x, y))
    return obstacles

def ClearObstacles():
    for obstacle_coords in obstacles:
        pygame.draw.rect(DISPLAYSURF, BLACK, (obstacle_coords[0], obstacle_coords[1], PLAYER_SIZE, PLAYER_SIZE))

def CheckForLoss(obstacles, player):
    if (player.x, player.y) in obstacles:
        sys.exit()



class Player():
    def __init__(self):
        self.x = 200
        self.y = 200
        pass

    def PaintPosition(self):
        pygame.draw.rect(DISPLAYSURF, GREEN, (self.x, self.y, PLAYER_SIZE, PLAYER_SIZE))

    def CleanPosition(self):
        pygame.draw.rect(DISPLAYSURF, BLACK, (self.x, self.y, PLAYER_SIZE, PLAYER_SIZE))

    def move(self, key):
        self.CleanPosition()

        if key == K_UP and self.y != 0:
            self.y -= PLAYER_SIZE
        if key == K_DOWN and self.y != WINDOW_Y-PLAYER_SIZE:
            self.y += PLAYER_SIZE
        if key == K_LEFT and self.x != 0:
            self.x -= PLAYER_SIZE
        if key == K_RIGHT and self.x != WINDOW_X-PLAYER_SIZE:
            self.x += PLAYER_SIZE

        self.PaintPosition()


class Point():
    def __init__(self):
        self.x = random.randint(0, WINDOW_X/PLAYER_SIZE) * PLAYER_SIZE
        self.y = random.randint(0, WINDOW_Y/PLAYER_SIZE) * PLAYER_SIZE
        pass

    def CalculateCoords(self, obstacles):
        # Emulating a do while with while True and break statement. Set point coords that are not in obstacles coords
        while True:
            self.x = random.randint(0, (WINDOW_X-PLAYER_SIZE)/PLAYER_SIZE) * PLAYER_SIZE     # Calculate a random coordinate that is a multiple of PLAYER_SIZE
            self.y = random.randint(0, (WINDOW_Y-PLAYER_SIZE)/PLAYER_SIZE) * PLAYER_SIZE
            if (self.x, self.y) not in obstacles:
                break

    def PaintPosition(self):
        pygame.draw.rect(DISPLAYSURF, BLUE, (self.x, self.y, PLAYER_SIZE, PLAYER_SIZE))

    def CleanPosition(self):
        pygame.draw.rect(DISPLAYSURF, BLACK, (self.x, self.y, PLAYER_SIZE, PLAYER_SIZE))




pygame.init()
#pygame.key.set_repeat(100,75)    # when a key is pressed down it sends multiple keydown signals after 100 miliseconds

DISPLAYSURF = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
pygame.display.set_caption('Points: 0')

player = Player()
point = Point()

total_points = 0

pygame.draw.rect(DISPLAYSURF, GREEN, (player.x, player.y, PLAYER_SIZE, PLAYER_SIZE))



obstacles = PrintRandomObstacles(point, player)
player.PaintPosition()
point.CleanPosition()
point.CalculateCoords(obstacles)
point.PaintPosition()


while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        DetermineMotion(event, player)
        CheckForLoss(obstacles, player)

        if player.x == point.x and player.y == point.y:
            total_points += 1
            ClearObstacles()
            obstacles = PrintRandomObstacles(point, player)
            point.CleanPosition()
            point.CalculateCoords(obstacles)
            point.PaintPosition()
            player.PaintPosition()

    pygame.display.set_caption(f'Points: {total_points}')
    pygame.display.update()


import os
import msvcrt
import random
import colorama
from colorama import Fore, Style

colorama.init()
SIZE = 50


def clearConsole():     # A function that clears the console.
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def output(array, points):          # Prints the array. 
    for i in range(SIZE+1):
        temp_str = ''
        for j in range(SIZE+1):
            temp_str += array[i][j] + ' '
        
        print(temp_str)
    print(f"Points: {points}")
         
def random_coordinates():                 #Sets random coordinates for the point.
    coordinate_i = random.randint(1, SIZE-1)
    coordinate_j = random.randint(1, SIZE-1)
    return coordinate_i, coordinate_j

def fill_array_with_starting_values(array):
    for i in range(SIZE+1):             # Fills the array with empty spaces and lines in the perimeter of the array to set the boundaries. 
        temp_list = []
        for j in range(SIZE+1):
            if (i == 0 and j == 0) or (i == SIZE and j == SIZE) or (i == 0 and j == SIZE) or (i == SIZE and j == 0):
                temp_list.append('+') 
            elif j == 0 or j == SIZE:
                temp_list.append('|')
            elif i == 0 or i == SIZE:
                temp_list.append('-')
            else:
                temp_list.append(' ')
        main_list.append(temp_list)
    

PLAYER_CHAR = Fore.MAGENTA + '0' + Style.RESET_ALL         # Use the Fore.'COLOR' to color the next character and then use the Style.RESET_ALL 
POINT_CHAR = Fore.GREEN + '$' + Style.RESET_ALL        # to reset the color of the printed text for all the next characters.
OBSTACLE_CHAR = Fore.RED + '*' + Style.RESET_ALL

points = 0
main_list = [] # Array of all the plane.

obstacles = [] # List with tuples of each obstacle's coordinates.

fill_array_with_starting_values(main_list)

point_i, point_j = random_coordinates()

main_list[point_i][point_j] = POINT_CHAR # Set the position of the POINT CHARacter in a random place in the array.
main_list[int(SIZE/2)][int(SIZE/2)] = PLAYER_CHAR    # Set the position of the PLAYER CHARacter in the middle of the array.

i = int(SIZE/2) # These variables are used to save the position of the
j = int(SIZE/2) #  player CHARacter every time, so it can be changed easily.


output(main_list, points)

inp = msvcrt.getch().decode("utf-8").lower()   # Get the only one letter input and the user doesn't need to press enter.

while (inp != 'q'):
    
    if (inp.lower() == 'w'):
        main_list[i][j] = ' '       # Clears the previous position of the character.
        if i == 1:                      
            i = SIZE-1              # Make a change for when the character is far up.
        else:   
            i -= 1                  # Change the character's position in the array based on the input of the user.
        main_list[i][j] = PLAYER_CHAR
    
    if (inp.lower() == 's'):
        main_list[i][j] = ' '       # Clears the previous position of the character.
        if i == (SIZE-1):
            i = 1                   # Make a change for when the character is far down.
        else:
            i += 1                  # Change the character's position in the array based on the input of the user.
        main_list[i][j] = PLAYER_CHAR
    
    if (inp.lower() == 'd'):
        main_list[i][j] = ' '       # Clears the previous position of the character.
        if j == (SIZE-1):
            j = 1                   # Make a change for when the character is far right.
        else:
            j += 1                  # Change the character's position in the array based on the input of the user.
        main_list[i][j] = PLAYER_CHAR
    
    if (inp.lower() == 'a'):
        main_list[i][j] = ' '       # Clears the previous position of the character
        if j == 1:
            j = SIZE-1                  # Make a change for when the character is far left.
        else:    
            j -= 1                  # Change the character's position in the array based on the input of the user.
        main_list[i][j] = PLAYER_CHAR
    
    point_scored = False            # The default value is false. It changes inside the if statement below if a point is scored.

    coord_tupl = (i, j)                 #create a tuple of the coordinates of your character.
    if coord_tupl in obstacles:         # Check if coordinates of player match these of an obstacle. Basically check if a player hit an obstacle.
        clearConsole()
        print(Fore.RED + "YOU LOST." + Style.RESET_ALL)
        print(f"Your score was {points} points.")       
        print("Press any key to close...")
        inp = msvcrt.getch().decode("utf-8").lower()   # Get the only one letter input and the user doesn't need to press enter.  
        break

    if (i == point_i) and (point_j == j): # Checks if the coordinates of the player character and the point's match.
        points = points + 1               # Increase the points by one.
        point_i, point_j = random_coordinates()
        main_list[point_i][point_j] = POINT_CHAR # Set the position for the new POINT CHARacter in a random place in the array.
        point_scored = True

    

    if point_scored:                            # We use the boolean variable to only increase the amount of obstacles when a point was scored.
        for k in range(points, 2**(points)+1):             # We use this range so the obstacles increase exponesialy.
            obstacle_i, obstacle_j = random_coordinates()
            while ((obstacle_i == i) and (obstacle_j == j)) or ((point_i == obstacle_i) and (point_j == obstacle_j)):
                obstacle_i, obstacle_j = random_coordinates()
            main_list[obstacle_i][obstacle_j] = OBSTACLE_CHAR
            obstacles.append((obstacle_i, obstacle_j))
            
    

    clearConsole()              # This function is used to clear the console and refresh the screen based on the input of the user.
    output(main_list, points)           # Re-prints the array based on the changes made by the user, for the movement of the char.
    inp = msvcrt.getch().decode("utf-8").lower()  # Get the only one letter input and the user doesn't need to press enter.
    
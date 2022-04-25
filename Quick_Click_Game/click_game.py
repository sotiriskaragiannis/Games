from game_functions import ClickGame
from gui_app_functions import *

     
latest_score = None


highscore = LoadHighScore()
window = OpenWindow(latest_score, highscore)

# Create an event loop
while True:

    event, values = window.read()

    # End program if user closes window 
    if event == sg.WIN_CLOSED:
        break

    if event == "Play":
        window.close()          # close the window to open the game and then refresh the latest score 
        latest_score = ClickGame()

        if highscore != None:
            if latest_score > highscore:
                SaveHighScore(latest_score)
        else:
            SaveHighScore(latest_score)
            
        highscore = LoadHighScore()
        window = OpenWindow(latest_score, highscore)   # recreate the window to refresh the latest score
        
window.close()
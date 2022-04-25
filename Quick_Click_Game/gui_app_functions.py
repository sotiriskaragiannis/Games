import PySimpleGUI as sg
import os.path
from os import path

def LoadHighScore():
    if path.exists("highscore.txt"):
        f = open("highscore.txt", "r")
        highscore = int(f.read())
        f.close()
        return highscore
    else:
        return None

def SaveHighScore(highscore):
    f = open("highscore.txt", "w")
    f.write(str(highscore))
    f.close()

def OpenWindow(latest_score, highscore):
    # Set the window's layout
    layout = [[sg.Text("Welcome to Click Game!")], [sg.Text(f"Latest Score: {latest_score}")], [sg.Text(f"High Score: {highscore}")], [sg.Button("Play")]]  
    # Create the window
    window = sg.Window("Click Game", layout, size=(300, 150))
    return window
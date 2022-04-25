# Click Game

In this game you must click some white blocks for 20 seconds. You can see your highscore and try to beat it.

## Beginning
![gui_app](https://user-images.githubusercontent.com/87957685/165132269-2b13683f-af9a-4165-8f42-77d63b944c10.png)

This is the first gui app that the user interacts with. It shows the latest score (None if you just opened the app) and the highscore which is stored in a file localy.
You can start playing by clicking "Play".

## Game
![game](https://user-images.githubusercontent.com/87957685/165133487-b836cf39-0261-42d3-bd12-d7128b2fa899.png)
When you click the white block, a new one is generated and a point is earned. In the top left of the window you can see the points you have and the time remaining in seconds.

## Game Parameters
In the block.py file you can change some game parameters such as the window size (WINDOW_X, WINDOW_Y), the color of the blocks and their size (BLOCK_SIZE). 
Also in the game_functions.py you can change the time of the game (t_end = time.time() + 20) which is 20 seconds.

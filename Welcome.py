def welcomeInstructions ():
    my_string = '''Welcome to Minesweeper! Here are the instructions:
    The game begins on a grid of unmarked squares - type the coordinates of a box to start the game. 
    You will see that some squares will disappear, others will now contain numbers, and some just remain blank.
    The numbers signify how many mines are touching the numbered square (including touching corners!)
    When the game prompts you to choose a row/column, enter the coordinates of the box that you want to reveal. Do the same for a box you want to flag, but type an F after the coordinates.
    Flag the squares that you think contain mines but look at the flag count to ensure that you don't flag more than 10 mines.
    To win a round, your goal is to click on every square of a grid that doesn't have a mine under it. If you lose around you'll be able to reset and try again!
    Happy playing!'''
    print(my_string)

welcomeInstructions()



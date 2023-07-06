import numpy as np
#from Welcome import welcomeInstructions
import termtables as tt
import random
lose = False
win = False

#welcomeInstructions()
def fill(x, y):
    if x < 0 or y < 0 or x >= r or y >= c:
        return puzzle
    if puzzle_mines[x][y] != "0" or puzzle[x][y] == "-":
        return puzzle
    else:
        puzzle[x][y] = "-"
        fill(x - 1, y)
        fill(x + 1, y)
        fill(x, y - 1)
        fill(x, y + 1)
        fill(x - 1, y - 1)
        fill(x - 1, y + 1)
        fill(x + 1, y - 1)
        fill(x + 1, y + 1)
    return puzzle
    

def generator():
    global list
    global flag_list
    list=[]
    flag_list = []
    for i in range(10):
        num=random.randint(1,8)
        num2=random.randint(1,8) 
        while (num,num2) in list:
            num=random.randint(1,8)
            num2=random.randint(1,8)
        num=num-1
        num2=num2-1
        list.append((num,num2))
    return(list)
def askUser():
    global guessColumn
    global guessRow
    global flagged
    while True:
        guessRow = input("What Row do you pick between 1-8? ")
        if guessRow.isnumeric(): 
            if int(guessRow) >= 1 and int(guessRow) <= 8:
                break
        print('Incorrect input, please enter an integer inbetween 1 and 8')
        
    while True:
        guessColumn = input("What Column do you pick between 1-8? ")
        if guessColumn.isnumeric():
            if int(guessColumn) >= 1 and int(guessColumn) <= 8:
                break
        print('Incorrect input, please enter an integer inbetween 1 and 8') 
    while True:
        flagged = input("Do you want to flag this square? Type Y or N ")
        if flagged.isalpha():
            if flagged == "n" or flagged == "N":
                flagged = False
                break
            if flagged  == "y" or  flagged == "Y":
                guessRow=(int(guessRow)-1)
                guessColumn=(int(guessColumn)-1)
                if puzzle[guessRow][guessColumn] == "X":
                    puzzle[guessRow][guessColumn] = "?"
                    flag_list.remove((guessRow,guessColumn))
                    break
                puzzle[guessRow][guessColumn] = "X"
                flag_list.append((guessRow,guessColumn))
                print(flag_list)
                flagged = True
                break
        print('Incorrect input, please enter Y or N') 
            
            
def userCheck():
    global guess
    global guessX
    global guessY
    global lose
    if not flagged:
        guess = ((int(guessRow)-1),  (int(guessColumn)-1))
        guessX = (int(guessRow)-1)
        guessY = (int(guessColumn)-1)
        for b in list:
            if guess == b:
                print('You Lose!')
                lose = True
                break

def checkForBombs():
    global count
    global r
    global c
    global row
    global col 
    count = 0
    r = len(puzzle)
    c = len(puzzle[0])
    for row in range (r):
        for col in range (c):
            # Check if space is a mine
            if puzzle_mines[row][col] == "M":
                continue
            # Check up  
            if row > 0 and puzzle_mines[row-1][col] == "M":
                count = count + 1
            # Check down    
            if row < r-1  and puzzle_mines[row+1][col] == "M":
                count = count + 1
            # Check left
            if col > 0 and puzzle_mines[row][col-1] == "M":
                count = count + 1
            # Check right
            if col < c-1 and puzzle_mines[row][col+1] == "M":
                count = count + 1
            # Check top-left    
            if row > 0 and col > 0 and puzzle_mines[row-1][col-1] == "M":
                count = count + 1
            # Check top-right
            if row > 0 and col < c-1 and puzzle_mines[row-1][col+1] == "M":
                count = count + 1
            # Check below-left  
            if row < r-1 and col > 0 and puzzle_mines[row+1][col-1] == "M":
                count = count + 1
            # Check below-right
            if row < r-1 and col < c-1 and puzzle_mines[row+1][col+1] == "M":
                count = count + 1
            puzzle_mines[row][col] = count
            count = 0
generator()
puzzle = np.array([[" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "]])
puzzle_mines = np.array([[" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "]])
for i in list:
    puzzle_mines[i[0]][i[1]] = "M" 
checkForBombs()
while lose == False and win == False:
    askUser()
    userCheck()
    if not flagged:
        if not (guessX,guessY) in flag_list:
            puzzle[guessX][guessY] = puzzle_mines[guessX][guessY]
        else:
            print('This space has been flagged')
        fill(guessX, guessY)
    puzzle_arrr = np.array(puzzle_mines).reshape(-1, 8)
    puzzle_arrr
    grid_mines = tt.to_string(
        puzzle_arrr,
        style=tt.styles.ascii_thin,
        # alignment="ll",
        # padding=(0, 1),
    )
    puzzle_arr = np.array(puzzle).reshape(-1, 8)
    puzzle_arr
    grid = tt.to_string(
        puzzle_arr,
        style=tt.styles.ascii_thin,
        # alignment="ll",
        # padding=(0, 1),
    )
    print(grid) 
    print("                 ")
    print(grid_mines)
    print(untilWin)
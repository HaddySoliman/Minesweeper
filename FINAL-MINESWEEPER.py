import numpy as np
#from Welcome import welcomeInstructions
import termtables as tt
import random
import time 
lose = False
win = False
win_count=0
mines_count = 0
restart = 'y'
global start_grid
puzzle = np.array([[" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "]])
puzzle_temp_start = np.array([[" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "]])

puzzle_arrrr = np.array(puzzle_temp_start ).reshape(-1, 8)
puzzle_arrrr
start_grid = tt.to_string(
    puzzle_arrrr,
    style=tt.styles.ascii_thin,
    # alignment="ll",
    # padding=(0, 1),
        )

print(start_grid)
start=input ("Press enter to start playing!")
print("The timer has started")
start_time = time.time()

def fill(x, y):
    if x < 0 or y < 0 or x >= r or y >= c:
        return puzzle
   
    if puzzle[x][y] != "-":
        puzzle[x][y] = puzzle_mines[x][y]
        zero_list.add((x,y))

    if puzzle[x][y] == "0":
        puzzle[x][y] = "-"
        zero_list.add((x,y))
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
    global zero_list
    global mines_count
    zero_list=set([])
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
                    mines_count-=1
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
    global win_count
    global win
    global restart
    global puzzle_mines
    global mines_count
    if flagged:
        mines_count += 1
        print("You have flagged", mines_count, "mines")
    if not flagged:
        guess = ((int(guessRow)-1),(int(guessColumn)-1))
        guessX = (int(guessRow)-1)
        guessY = (int(guessColumn)-1)
        for b in list:
            if guess == b:
                print('You Lose!')
                lose = True
                quit()
        if win_count >= 54:
            print("You Win!!!")
            win = True 
            quit()

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

while restart == 'y' or restart == 'Y':
    generator()
    #puzzle = np.array([[" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "]])
    puzzle_mines = np.array([[" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "]])
    for i in list:
        puzzle_mines[i[0]][i[1]] = "M" 
    checkForBombs()
    while lose == False and win == False:
        askUser()
        userCheck()
        if not flagged:
            if not guess in flag_list:
                puzzle[guessX][guessY] = puzzle_mines[guessX][guessY]
                fill(guessX,guessY)
                for i in zero_list:
                    win_count = win_count+1
            else:
                print('This space has been flagged')
                
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
        if win or lose:
            end_time = time.time()
            elapsed= end_time - start_time
            print ("You took ... ", elapsed, "seconds")
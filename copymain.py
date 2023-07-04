import numpy as np
import termtables as tt
import random
lose=False
def generator():
    global list
    list=[]
    for i in range(10):
        num=random.randint(1,8)
        num2=random.randint(1,8) 
        while (num,num2) in list:
            num=random.randint(1,8)
            num2=random.randint(1,8)
        num=num-1
        num2=num2-1
        list.append((num,num2))
    print(list)
    return(list)
def askUser():
    global guessColumn
    global guessRow
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
def userCheck():
    global guess
    guess = ((int(guessRow)-1),(int(guessColumn)-1))
    print(guess)
    for b in list:
        if guess == b:
            print('You Lose!')
            lose = True
            quit
def checkForBombs():
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
            print(puzzle_mines)
generator()
puzzle = np.array([[" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "]])
puzzle_mines = np.array([[" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "]])


for i in list:
    puzzle_mines[i[0]][i[1]] = "M" 
checkForBombs()

puzzle_arr = np.array(puzzle).reshape(-1, 8)

puzzle_arr
grid = tt.to_string(
    puzzle_arr,
    style=tt.styles.ascii_thin,
    # alignment="ll",
    # padding=(0, 1),
)

puzzle_arrr = np.array(puzzle_mines).reshape(-1, 8)

puzzle_arrr
grid_mines = tt.to_string(
    puzzle_arrr,
    style=tt.styles.ascii_thin,
    # alignment="ll",
    # padding=(0, 1),
)

askUser()
userCheck()

puzzle[guess[0]][guess[1]] = puzzle_mines[guess[0]][guess[1]]


print(grid) 
print("                 ")
print(grid_mines)


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
    guess = [int(guessRow),int(guessColumn)]
    print(guess)
    for b in list:
        if guess == b:
            print('You Lose!')
            lose=True
            quit
    
generator()


puzzle = np.array([[" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "]])
puzzle_mines = np.array([[" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "], [" "," "," "," "," "," "," "," "]])
listx=[]
listy=[]
for i in list:
    listx = [x[0] for x in list]
    listy = [x[1] for x in list]
    puzzle[[x[0] for x in list]][[x[1] for x in list]] = "mine" 

print(listx)
print(listy)


puzzle_arr = np.array(puzzle).reshape(-1, 8)

puzzle_arr
grid = tt.to_string(
    puzzle_arr,
    style=tt.styles.ascii_thin,
    # alignment="ll",
    # padding=(0, 1),
)
print(grid) 

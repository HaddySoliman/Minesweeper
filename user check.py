import random
lose=False
def generator():
    global list
    list=[]
    for i in range(10):
        num=random.randint(1,8)
        num2=random.randint(1,8)
        while [num,num2] in list:
            num=random.randint(1,8)
            num2=random.randint(1,8)
        list.append([num,num2])
    print(list)
    return(list)
def askUser():
    global guessColumn
    global guessRow
    guessRow = input("What row do you pick between 1-8? ")
    guessColumn = input("What column do you pick between 1-8? ")

    

def userCheck():
    guess = [int(guessRow),int(guessColumn)]
    print(guess)
    for b in list:
        if guess == b:
            print('You Lose!')
            lose=True
            quit
    
generator()
askUser()
userCheck()



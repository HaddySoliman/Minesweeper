import random
lose=False
guessRow=0
guessColumn=0
global y1
y1 = 0
x1 = 0
y2 = 0
x2 = 0
y3 = 0
x3 = 0
y4 = 0
x4 = 0
y5 = 0
x5 = 0
y6 = 0
x6 = 0
y7 = 0
x7 = 0
y8 = 0
x8 = 0
y9 = 0
x9 = 0
y10 = 0
x10 = 0
mine1 = 0
mine2 = 0
mine3 = 0
mine4 = 0
mine5 = 0
mine6 = 0
mine7 = 0
mine8 = 0
mine9 = 0
mine10 = 0
guess = 0    
def checkmines():
    global y1
    y1 = random.randint(1,8)
    global x1
    x1 = random.randint(1,8)
    global y2 
    y2 = random.randint(1,8)
    global x2
    x2 = random.randint(1,8)
    global y3
    y3 = random.randint(1,8)
    global x3
    x3 = random.randint(1,8)
    global y4
    y4 = random.randint(1,8)
    global x4
    x4 = random.randint(1,8)
    global y5
    y5 = random.randint(1,8)
    global x5
    x5 = random.randint(1,8)
    global y6
    y6 = random.randint(1,8)
    global x6
    x6 = random.randint(1,8)
    global y7
    y7 = random.randint(1,8)
    global x7
    x7 = random.randint(1,8)
    global y8
    y8 = random.randint(1,8)
    global x8
    x8 = random.randint(1,8)
    global y9
    y9 = random.randint(1,8)
    global x9
    x9 = random.randint(1,8)
    global y10 
    y10 = random.randint(1,8)
    global x10
    x10 = random.randint(1,8)
    global mine1
    mine1 = (x1,y1)
    global mine2
    mine2 = (x2,y2)
    global mine3
    mine3 = (x3,y3)
    global mine4
    mine4 = (x4,y4)
    global mine5
    mine5 = (x5,y5)
    global mine6
    mine6 = (x6,y6)
    global mine7
    mine7 = (x7,y7)
    global mine8
    mine8 = (x8,y8)
    global mine9
    mine9 = (x9,y9)
    global mine10
    mine10 = (x10,y10)
    print(str(mine1) + 'mine 1')
    print(str(mine2) + 'mine 2')
    print(str(mine3) + 'mine 3')
    print(str(mine4) + 'mine 4')
    print(str(mine5) + 'mine 5')
    print(str(mine6) + 'mine 6')
    print(str(mine7) + 'mine 7')
    print(str(mine8) + 'mine 8')
    print(str(mine9) + 'mine 9')
    print(str(mine10) + 'mine 10')
    while mine1 == mine2 or mine1 == mine3 or mine1 == mine4 or mine1 == mine5 or mine1 == mine6 or mine1 == mine7 or mine1 == mine8 or mine1 == mine9 or mine1 == mine10 or mine2 == mine3 or mine2 == mine4 or mine2 == mine5 or mine2 == mine6 or mine2 == mine7 or mine2 == mine8 or mine2 == mine9 or mine2 == mine10 or mine3 ==  mine4 or mine3 == mine5 or mine3 == mine6 or mine3 == mine7 or mine3 == mine8 or mine3 == mine9 or mine3 == mine10 or mine4 == mine5 or mine4 == mine6 or mine4 == mine7 or mine4 == mine8 or mine4 == mine9 or mine4 == mine10 or mine5 == mine6 or mine5 == mine7 or mine5 == mine8 or mine5 == mine9 or mine5 == mine10 or mine6 == mine7 or mine6 == mine8 or mine6 == mine9 or mine6 == mine10 or mine7 == mine8 or mine7 == mine9 or mine7 == mine10 or mine8 == mine9 or mine8 == mine10 or mine9 == mine10:
        if mine1 == mine2 or mine1 == mine3 or mine1 == mine4 or mine1 == mine5 or mine1 == mine6 or mine1 == mine7 or mine1 == mine8 or mine1 == mine9 or mine1 == mine10:
            global y1
            y1=random.randint(1,8)
            global x1
            x1=random.randint(1,8)
            global mine1
            mine1=(x1,y1)
            print(str(mine1) + 'mine 1')
        elif mine2 == mine3 or mine2 == mine4 or mine2 == mine5 or mine2 == mine6 or mine2 == mine7 or mine2 == mine8 or mine2 == mine9 or mine2 == mine10:
            global y2
            y2=random.randint(1,8)
            global x2
            x2=random.randint(1,8)
            global mine2
            mine2=(x2,y2) 
            print(str(mine2) + 'mine 2')
        elif mine3 ==  mine4 or mine3 == mine5 or mine3 == mine6 or mine3 == mine7 or mine3 == mine8 or mine3 == mine9 or mine3 == mine10:
            global y3
            y3=random.randint(1,8)
            global x3
            x3=random.randint(1,8)
            global mine3
            mine3=(x3,y3)
            print(str(mine3) + 'mine 3')
        elif  mine4 == mine5 or mine4 == mine6 or mine4 == mine7 or mine4 == mine8 or mine4 == mine9 or mine4 == mine10:
            global y4
            y4=random.randint(1,8)
            global x4
            x4=random.randint(1,8)
            global mine4
            mine4=(x4,y4)
            print(str(mine4) + 'mine 4')
        elif mine5 == mine6 or mine5 == mine7 or mine5 == mine8 or mine5 == mine9 or mine5 == mine10:
            global y5
            y5=random.randint(1,8)
            global x5
            x5=random.randint(1,8)
            global mine5
            mine5=(x5,y5)
            print(str(mine5) + 'mine 5')
        elif mine6 == mine7 or mine6 == mine8 or mine6 == mine9 or mine6 == mine10:
            global y6
            y6=random.randint(1,8)
            global x6
            x6=random.randint(1,8)
            global mine6
            mine6=(x6,y6)
            print(str(mine6) + 'mine 6')
        elif mine7 == mine8 or mine7 == mine9 or mine7 == mine10:
            global y7
            y7=random.randint(1,8)
            global x7
            x7=random.randint(1,8)
            global mine7
            mine7=(x7,y7)
            print(str(mine7) + 'mine 7')
        elif mine8 == mine9 or mine8 == mine10:
            global y8
            y8=random.randint(1,8)
            global x8
            x8=random.randint(1,8)
            global mine8
            mine8=(x8,y8)
            print(str(mine8) + 'mine 8')
        elif mine9 == mine10:
            global y9
            y9=random.randint(1,8)
            global x9
            x9=random.randint(1,8)
            global mine9
            mine9=(x9,y9)
            global mine10
            mine10=(x10,y10)
            print(str(mine9)  + 'mine 9')
            print(str(mine10) + 'mine 10')
            pass
def askUser():
    global guessRow
    guessRow = input("What row do you pick between 1-8? ")
    global guessColumn
    guessColumn = input("What column do you pick between 1-8? ")
    print(guessRow)
    print(guessColumn)
    pass
def userCheck():
    global guessRow
    global guessColumn
    global mine1
    global mine2
    global mine3
    global mine4
    global mine5
    global mine6
    global mine7
    global mine8
    global mine9
    global mine10
    global lose
    global guess
    guess= (guessRow,guessColumn)
    print(guess)
    if guess == mine1 or guess == mine2 or guess == mine3 or guess == mine4 or guess == mine5 or guess == mine6 or guess == mine7 or guess == mine8 or guess == mine9 or guess == mine10:
        print('You Lose!')
        lose=True
        quit
    pass 


checkmines()
askUser()
userCheck()


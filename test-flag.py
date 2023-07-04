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
    
    while True:
        flagged = input("Do you want to flag this square? Type Y(yes) or N(no)")
        if flagged.isalpha():
            if flagged != "y" or "n" or "Y" or "N":
                print('Incorrect input, please enter Y(yes) or N(no)') 
            if flagged == "Y" or "y":
                puzzle[row][col] = "X"
            elif flagged == "N" or "n":
                puzzle[row][col] = "X"
            

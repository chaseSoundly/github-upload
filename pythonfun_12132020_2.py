# Sudoku

game = [" ","6"," ","8"," "," ","5"," ","9",
        " ","2"," ","6"," "," "," "," "," ",
        " "," ","4","5"," "," "," "," "," ",
        " ","5","1","3","7"," ","9"," ","8",
        " ","4","9"," ","8"," ","7","6","3",
        "7"," "," "," "," ","2","4","1"," ",
        "9"," ","6"," ","5","3","2","8"," ",
        "4"," ","5"," ","1"," "," ","9"," ",
        "3"," "," ","4"," ","6"," "," ","7"]

def crossbeam(length):
    print("-",end="")
    for i in range(0,length):
        print("-",end="")
    print("-")

def nav():
    while True:
        answer = input()
        crossbeam(57)
        for i in range(0,9):
            print("|",end="")
            for j in range(i*9,(i*9)+9):
                if (j % 3 == 0):
                    print("|",end="")
                temp_text = game[j]
                print(temp_text.center(5),end="|")
            print("|")
            if (i == 2 or i == 5 or i == 8):
                crossbeam(57)
        break
nav()
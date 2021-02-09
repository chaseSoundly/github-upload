# For finding shortest route

def make_grid(x,y,x1,y1):
    for i in range(0,y):
        for j in range(0,x):
            if (j == x1 - 1 and i == y1 - 1):
                print(" | ",end="")
            else:
                print(" • ",end="")
        print()

make_grid(9,9,5,5)

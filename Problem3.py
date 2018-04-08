import math

def checkColFill(col, lst, centerRow=1):
    if lst[centerRow-1][col] == 1 and lst[centerRow][col] == 1\
        and lst[centerRow+1][col] == 1:
        return True
    return False

noOfCols = lambda x: math.ceil(x/3) if math.ceil(x/3) >= 3 else 3

def do(lst):
    for col in range(1, len(lst[0])-1):
        if col != len(lst[0])-2:
            while checkColFill(col-1, lst) == False:
                print('{} {}'.format(2, col+1), flush=True)
                rowFilled, colFilled = list(map(int, input().split(' ')))
                if rowFilled == 0 and colFilled == 0:
                    break
                else:
                    lst[rowFilled-1][colFilled-1] = 1
        else:
            a, b = None, None
            while True:
                print('{} {}'.format(2, col+1), flush=True)
                a, b = list(map(int, input().split(' ')))
                if a == 0 and b == 0:
                    break
                else:
                    lst[a-1][b-1]

for i in range(0, int(input())):
    minArea = int(input())
    columns = noOfCols(minArea)
    lst = [[0]*columns]+[[0]*columns]+[[0]*columns]
    do(lst)
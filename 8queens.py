board=[-1]*8

def isSafe(row,col):
    for i in range(col):
        if board[i]==row:
            return False
        if abs(board[i]-row)==abs(i-col):
            return False

    return True

def solve(col):
    if col==8:
        return True

    for row in range(8):
        if isSafe(row,col):
            board[col]=row

            if solve(col+1):
                return True
            board[col]=-1
    return False

if solve(0):
    for cols in range(8):
        for rows in range(8):
            if board[cols]==rows:
                print("Q",end=" ")
            else:
                print("#",end=" ")
        print(end="\n")
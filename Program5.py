def safe(b,r,c):
    for i in range(r):
        if b[i]==c or abs(b[i]-c)==abs(i-r):
            return False
    return True

def solve(b,r,n):
    if r==n:
        for i in range(n):
            for j in range(n):
                print("Q" if b[i]==j else ".",end=" ")
            print()
        return True
    for c in range(n):
        if safe(b,r,c):
            b[r]=c
            if solve(b,r+1,n):
                return True
    return False

n=8
board=[-1]*n
solve(board,0,n)
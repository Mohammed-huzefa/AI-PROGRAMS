def print_board(b):
    for r in b:
        print("|".join(r))
        print("-"*5)

def win(b,p):
    return any(all(c==p for c in r) for r in b) or \
           any(all(b[i][j]==p for i in range(3)) for j in range(3)) or \
           all(b[i][i]==p for i in range(3)) or \
           all(b[i][2-i]==p for i in range(3))

b=[[' ']*3 for _ in range(3)]
p='X'

while True:
    print_board(b)
    r=int(input("Row: "))-1
    c=int(input("Col: "))-1

    if b[r][c]==' ':
        b[r][c]=p
    else:
        print("Invalid move")
        continue

    if win(b,p):
        print_board(b)
        print(p,"wins")
        break

    if all(b[i][j]!=' ' for i in range(3) for j in range(3)):
        print("Tie")
        break

    p='O' if p=='X' else 'X'
def show(b):
    for r in b:
        print(" | ".join(r))
        print("-"*9)

def win(b,p):
    if any(all(c==p for c in r) for r in b):
        return True
    if any(all(b[r][c]==p for r in range(3)) for c in range(3)):
        return True
    if all(b[i][i]==p for i in range(3)):
        return True
    if all(b[i][2-i]==p for i in range(3)):
        return True
    return False

b=[[' ']*3 for _ in range(3)]
p='X'

while 1:
    show(b)
    r=int(input("Row: "))-1
    c=int(input("Col: "))-1

    if b[r][c]!=' ':
        print("Invalid")
        continue

    b[r][c]=p

    if win(b,p):
        show(b)
        print("Player",p,"wins!")
        break

    if all(x!=' ' for row in b for x in row):
        show(b)
        print("Tie!")
        break

    p='O' if p=='X' else 'X'

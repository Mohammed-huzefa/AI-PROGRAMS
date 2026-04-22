def queens(n=8):
    sols = []
    
    def bt(cols, diag1, diag2, placed):
        r = len(placed)
        
        if r == n:
            sols.append(placed[:])
            return
        
        for c in range(n):
            if c not in cols and (r - c) not in diag1 and (r + c) not in diag2:
                bt(cols | {c}, diag1 | {r - c}, diag2 | {r + c}, placed + [c])
    
    bt(set(), set(), set(), [])
    return sols


sols = queens()
print(f"Total: {len(sols)}\n")

for i, s in enumerate(sols[:2], 1):
    print(f"Solution {i}: {s}")
    
    for r in range(8):
        print("".join('Q' if c == s[r] else '.' for c in range(8)))
    
    print()
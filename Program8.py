def negate(x):
    return x[1:] if x.startswith('~') else '~'+x

def resolve(c1, c2):
    for l in c1:
        if negate(l) in c2:
            return [x for x in c1 if x!=l] + [x for x in c2 if x!=negate(l)]
    return None

def resolution(kb, query):
    kb = kb + [[negate(query)]]
    while True:
        new = []
        for i in range(len(kb)):
            for j in range(i+1,len(kb)):
                r = resolve(kb[i], kb[j])
                if r == []:
                    return True
                if r and r not in new:
                    new.append(r)
        if all(c in kb for c in new):
            return False
        kb += new


kb = [['~P','Q'],['P','~Q','R'],['~R','S']]
query = 'S'

if resolution(kb,query):
    print("Query proved")
else:
    print("Query not proved")
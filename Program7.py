def fc(r,f,g):
    i=set(f)
    while 1:
        n=0
        for c,r in rules:
            if all(x in i for x in c) and r not in i:
                i.add(r)
                n=1
                if r==g:return 1
        if not n:return 0

def bc(r,f,g):
    if g in f:return 1
    for c,res in r:
        if res==g and all(bc(r,f,x) for x in c):
            return 1
    return 0

rules=[
(['hair','live young'],'mammal'),
(['feathers','fly'],'bird')
]

print("The cat is classified as a mammal." if fc(rules,['hair','live young'],'mammal') else "Not mammal")

print("The pigeon is classified as a bird." if bc(rules,['feathers','fly'],'bird') else "Not bird")

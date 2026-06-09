def neg(x):
    return x[1:] if x[0]=='~' else '~'+x

def res(c1,c2):
    r=[]
    f=0
    for x in c1:
        if neg(x) in c2:f=1
        else:r.append(x)
    for x in c2:
        if neg(x) not in c1:r.append(x)
    return r if f else None

def resolution(kb,q):
    kb=kb+[[neg(q)]]
    while 1:
        new=[]
        for i in range(len(kb)):
            for j in range(i+1,len(kb)):
                r=res(kb[i],kb[j])
                if r==[]: return 1
                if r and r not in kb and r not in new: new.append(r)
        if not new: return 0
        kb+=new

kb=[['P'],['~P','Q']]
q='Q'

if resolution(kb,q):
    print(f"The query '{q}' is PROVED.")
else:
    print(f"The query '{q}' is DISPROVED.")

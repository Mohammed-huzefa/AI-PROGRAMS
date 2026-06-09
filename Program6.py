def tsp(d):
    n=len(d)
    v=[0]
    c=0
    dist=0
    while len(v)<n:
        nxt=min([i for i in range(n) if i not in v],key=lambda i:d[c][i])
        dist+=d[c][nxt]
        v.append(nxt)
        c=nxt
    dist+=d[c][0]
    v.append(0)
    return v,dist

d=[[0,4,8,9,12],[4,0,6,8,9],[8,6,0,10,11],[9,8,10,0,7],[12,9,11,7,0]]

t,dist=tsp(d)

print("Tour:",t)

print("Distance:",dist)

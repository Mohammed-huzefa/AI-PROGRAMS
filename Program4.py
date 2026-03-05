import heapq

def h(n):
    H={'A':5,'B':3,'C':2,'D':1,'E':2,'G':0}
    return H.get(n,0)

def ao(start,goal,g):
    q=[(h(start),start,[start])]
    v=set()

    while q:
        f,n,path=heapq.heappop(q)

        if n==goal:
            return path

        v.add(n)

        for nb,c in g.get(n,[]):
            if nb not in v:
                heapq.heappush(q,(c+h(nb),nb,path+[nb]))

    return None


g={'A':[('B',1),('C',4)],
   'B':[('D',2)],
   'C':[('G',3)],
   'D':[('G',1)]}

p=ao('A','G',g)

if p:
    print("Path:",p)
else:
    print("No path")
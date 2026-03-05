import heapq

def h(n,g):
    return abs(ord(n)-ord(g))

def astar(start,goal,graph):
    q=[(h(start,goal),0,start,[start])]
    v=set()

    while q:
        f,c,n,path=heapq.heappop(q)

        if n==goal:
            return path

        v.add(n)

        for nb,w in graph.get(n,[]):
            if nb not in v:
                heapq.heappush(q,(c+w+h(nb,goal),c+w,nb,path+[nb]))

g={'A':[('B',1),('C',3)],
   'B':[('D',2)],
   'C':[('D',4)]}

p=astar('A','D',g)

print("Path:",p)
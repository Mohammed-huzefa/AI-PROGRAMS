def tsp(d):
    n=len(d)
    tour=[0]
    visited={0}
    cost=0

    while len(visited)<n:
        m=10**9
        for j in range(n):
            if j not in visited and d[tour[-1]][j]<m:
                m=d[tour[-1]][j]
                x=j
        tour.append(x)
        visited.add(x)
        cost+=m

    cost+=d[tour[-1]][0]
    tour.append(0)

    return tour,cost


n=int(input("Enter number of cities: "))
d=[]

print("Enter distance matrix:")
for i in range(n):
    row=list(map(int,input().split()))
    d.append(row)

tour,cost=tsp(d)

print("TSP Tour:",tour)
print("Total Cost:",cost)
class Rebro:
    def __init__(self, a, b, dist):
        self.a = a
        self.b = b
        self.dist = dist

    def __str__(self):
        return f"{self.a}->{self.b} : {self.dist}"


graph = [Rebro(1, 2, 18), Rebro(1, 4, 4), Rebro(1, 7, 9), Rebro(1, 8, 22), Rebro(2, 3, 1), Rebro(2, 5, 3),
         Rebro(2, 8, 1), Rebro(3, 5, 13), Rebro(4, 6, 5),
         Rebro(4, 7, 7), Rebro(5, 8, 9), Rebro(5, 7, 2), Rebro(6, 7, 5), Rebro(7, 8, 10)]

v=set(range(1,9))
visited=set()
ostov=[]
min_rebro=min((reb for reb in graph if reb.a==1), key=lambda reb: reb.dist)
ostov.append(graph.pop(graph.index(min_rebro)))
visited.add(1)
visited.add(min_rebro.b)
while v!=visited:
    min_rebro=min((reb for reb in graph if reb.a in visited and reb.b not in visited or reb.a not in visited and reb.b in visited ),key=lambda reb:reb.dist)
    ostov.append(graph.pop(graph.index(min_rebro)))
    visited.add(min_rebro.a)
    visited.add(min_rebro.b)
for rebro in ostov:
    print(rebro)
print(f"sum={sum(r.dist for r in ostov)}")
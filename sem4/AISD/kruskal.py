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

graph = sorted(graph, key=lambda x: x.dist)
connected = set()
isolated = {}
ostov = []

for r in graph:
    if r.a not in connected or r.b not in connected:
        if r.a not in connected and r.b not in connected:
            isolated[r.a] = [r.a, r.b]
            isolated[r.b] = isolated[r.a]
        else:
            if not isolated.get(r.a):
                isolated[r.b].append(r.a)
                isolated[r.a] = isolated[r.b]
            else:
                isolated[r.a].append(r.b)
                isolated[r.b] = isolated[r.a]

        ostov.append(r)
        connected.add(r.a)
        connected.add(r.b)

for r in graph:
    if r.b not in isolated[r.a]:
        ostov.append(r)
        gr1 = isolated[r.a]
        isolated[r.a] += isolated[r.b]
        isolated[r.b] += gr1

for r in ostov:
    print(r)
print(f'sum={sum(r.dist for r in ostov)}')
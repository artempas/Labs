from dataclasses import dataclass, field


@dataclass()
class Edge:
    source: int
    destination: int
    distance: int
    def __post_init__(self):
        self.source-=1
        self.destination-=1


@dataclass()
class Node:
    name:int
    path: list = field(default_factory=list)
    distance: int = None


nodes = list(Node(i) for i in range(7))


edges = [
    Edge(1, 2, 9),
    Edge(1, 3, 2),
    Edge(2, 4, 4),
    Edge(2, 5, 12),
    Edge(3, 2, 6),
    Edge(3, 5, 28),
    Edge(3, 6, 10),
    Edge(4, 5, 16),
    Edge(4, 7, 19),
    Edge(5, 7, 3),
    Edge(6, 5, 15),
    Edge(6, 7, 25)
]

nodes[0].path=[]
nodes[0].distance=0
found_nodes={nodes[1]}

while len(found_nodes)!=len(nodes):




import queue

class Graph:
    # n: number of nodes
    # arcs: [a, b] a -> b
    def __init__(self, n, arcs):
        self.n = n
        self.arcs = arcs
        self.arc_dict = [[] for i in range(n)]
        self.ind = [0] * n
        self.ond = [0] * n
        for arc in arcs:
            a, b = arc[0], arc[1]
            self.arc_dict[a].append(b)
            self.ind[a] += 1
            self.ond[b] += 1

    def TopoOrder(self):
        res = []
        q = queue.Queue()
        visited = [False] * self.n
        while len(res) < self.n:
            for i in range(self.n):
                if visited[i] == False and self.ond[i] == 0:
                    q.put(i)
                    visited[i] = True
            if q.empty():
                return None
            curr = q.get()
            res.append(curr)
            for node in self.arc_dict[curr]:
                self.ond[node] -= 1
        return res
    
if __name__ == "__main__":
    g = Graph(5, [[0, 1], [0, 3], [1, 3], [3, 2], [1, 2], [3, 4], [2, 4]])
    res = g.TopoOrder()
    print(res)
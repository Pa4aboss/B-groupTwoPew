import graphviz


class Node:
    def __init__(self, num, obj=None):
        self.data = obj
        self.num = num


class Graph:
    def __init__(self, directed=False):
        self.graph = dict()
        self.vertices = dict()
        self.undirected = not directed

    def add_node(self, e1):
        self.vertices[e1.num] = e1

    def add_edge(self, e1, e2):
        if e1 not in self.vertices:
            self.vertices[e1.num] = e1

        if e2 not in self.vertices:
            self.vertices[e2.num] = e2

        if e1.num not in self.graph:
            self.graph[e1.num] = []

        self.graph[e1.num].append(e2.num)
        if self.undirected:
            if e2.num not in self.graph:
                self.graph[e2.num] = []
            self.graph[e2.num].append(e1.num)

    def dfs(self, start, visited=None, sort=None):
        if visited is None:
            visited = []
        if sort is None:
            sort = []

        visited.append(start)

        if start not in self.graph:
            sort.append(start)
            return visited

        for u in self.graph[start]:
            if u not in visited:
                self.dfs(u, visited, sort)
        sort.append(start)
        return visited

    def dfs1(self, cl, p, v, st_end):
        # Поиск в глубину для поиска цикла
        cl[v] = 1
        if v not in self.graph:
            cl[v] = 2
            return False

        for i in self.graph[v]:
            if cl[i] == 0:
                p[i] = v
                if self.dfs1(cl, p, i, st_end):
                    return True
            elif cl[i] == 1:
                st_end[0] = i
                st_end[1] = v
                return True
        cl[v] = 2
        return False

    def find_cycle(self):
        p = dict()
        cl = dict()
        for u in list(self.vertices.keys()):
            p[u] = -1
            cl[u] = 0
        st_end = [-1] * 2
        for i in self.graph:
            if self.dfs1(cl, p, i, st_end):
                break
        if st_end[0] == -1:
            return False
        else:
            cycle = []
            v = st_end[1]
            while v != st_end[0]:
                cycle.append(v)
                v = p[v]
            cycle.append(st_end[0])
            cycle.reverse()
            return cycle

    def topological_sort(self):
        print(self.graph.keys())
        visited = []
        res = []

        for i in self.vertices.keys():
            if i not in visited:
                self.dfs(i, visited, res)
        res.reverse()
        return res

    def transpose(self):
        gt = Graph()
        for u in self.graph:
            for v in self.graph[u]:
                gt.add_edge(self.vertices[v], self.vertices[u])
        return gt

    def strong_connected_comps(self):
        visited1 = []
        for u in self.graph:
            if u not in visited1:
                self.dfs(u, visited1)

        gt = self.transpose()
        visited1 = list(reversed(visited1))
        visited2 = []
        num_comps = 0
        for i in range(0, len(visited1)):
            v = visited1[len(visited1) - 1 - i]
            if v not in visited2:
                gt.dfs(v, visited2)
                num_comps += 1

        return num_comps

    def draw_graph(self, graph_name, extension):
        drew = []
        if self.undirected:
            dot = graphviz.Graph(comment=graph_name, format=extension, engine='dot')
        else:
            dot = graphviz.Digraph(comment=graph_name, format=extension, engine='dot')
        for i in self.vertices:
            dot.node(str(i))
        for u in self.graph:
            for v in self.graph[u]:
                if self.undirected and [v, u] in drew:
                    continue
                drew.append([u, v])
                dot.edge(str(u), str(v))
        dot.render(graph_name, view=True)

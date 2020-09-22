class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for pair in ancestors:
        parent = pair[0]
        child = pair[1]
        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(child, parent)


    queue = []
    # to find the farthest node we look for the longest path
    queue.append([starting_node])

    path_length = 1
    earliest_ancestor = -1

    while len(queue) > 0:
        path = queue.pop(0)
        current_node = path[-1]

        if (len(path) >= path_length and current_node < earliest_ancestor) or len(path) > path_length:
            path_length = len(path)
            earliest_ancestor = current_node
         

        neighbors = graph.vertices[current_node]

        for neighbor in neighbors:
            path_copy = list(path)
            path_copy.append(neighbor)
            queue.append(path_copy)
    
    return earliest_ancestor
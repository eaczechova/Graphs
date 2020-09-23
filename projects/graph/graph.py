
"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # Create the new key with vertex id and set the value to the empty set (no edges yet)
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # Find vertex v1 in vertices, add v2 to the set of edges
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return set()

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        # Creates empty queue and pushes the Id of starting_vertex
        queue = Queue()
        queue.enqueue(starting_vertex)

        # Create Set to store visited vertices to prevent a loop
        visited_vertex = set()

        while queue.size() > 0:
            # get starting node/vertex
            vertex = queue.dequeue()
            if vertex not in visited_vertex:
                print(vertex)
                # if not visited add to the queue
                visited_vertex.add(vertex)
                # add each of its children to the back of the queue
                for neighbor in self.get_neighbors(vertex):
                    queue.enqueue(neighbor)

        
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # creates empty stack and pushes the Id of starting_vertex
        stack = Stack()
        stack.push(starting_vertex)

        # creates Set to store visited vertices
        visited_vertex = set()

        # loops while the stack is not empty
        while stack.size() > 0:
            # stores whatever is on the top of the stack, first vertex
            vertex = stack.pop()
            if vertex not in visited_vertex:
                # if not visited add to the stack
                print(vertex)
                visited_vertex.add(vertex)
                # add each of its children to the top of the stack
                for neighbor in self.get_neighbors(vertex):
                    stack.push(neighbor)
                

    def dft_recursive(self, starting_vertex, visited_vertex = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        print(starting_vertex)
        if visited_vertex is None:
            visited_vertex = set()
    
        visited_vertex.add(starting_vertex)
        
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited_vertex:
                self.dft_recursive(neighbor, visited_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()
        queue.enqueue([starting_vertex])
        visited_vertex = set()

        while queue.size() > 0:
            # dequeue the first path 
            path = queue.dequeue()
            # gets the last vertex from the path
            vertex = path[-1]

            if vertex not in visited_vertex:
                # if not yet visited, check if it's the target
                if vertex == destination_vertex:
                    return path
                visited_vertex.add(vertex)

                for neighbor in self.get_neighbors(vertex):
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    queue.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex, visited_vertex = None, path = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """

        stack = Stack()
        stack.push([starting_vertex])
        visited_vertex = set()

        while stack.size() > 0:
            path = stack.pop()
            vertex = path[-1]

            if vertex not in visited_vertex:
                if vertex == destination_vertex:
                    return path
                visited_vertex.add(vertex)

                for neighbor in self.get_neighbors(vertex):
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    stack.push(path_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited_vertex = None, path = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited_vertex is None:
            visited_vertex = set()

        if path is None:
        # use path to have values in order
            path = []
        visited_vertex.add(starting_vertex)
        # add vertex to the path
        path = path + [starting_vertex]

        # checks if starting_vertex is the destination_vertex and returns the path
        if starting_vertex == destination_vertex:
            return path
        # if not call the function on each unvisited neighbor
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited_vertex:
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited_vertex, path)
                if new_path is not None:
                    return new_path
        
        return None



if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))

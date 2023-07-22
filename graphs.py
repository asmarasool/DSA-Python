# vertices: interconnected objects
# edges : links that connect the vertices
# Dictionary: Key(vertices) and value(edges)
# V = {a, b, c, d, e}
# E = {ab, ac, bd, cd, de}



class graph:
    def __init__(self, gdict = None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    def getVertices(self):
        # vertices are the keys so we use .keys() to find vertices
        return list(self.gdict.keys())

    def add_vertex(self, vertex):
        # Adding vertex is like adding key to a dictionary
        if vertex not in self.gdict:
            self.gdict[vertex] = []

    def add_Edge(self, edge): # the edge will be a dict with two values
        edge = set(edge)  # converting to set to avoid duplicates
        start_point, end_point = tuple(edge)  # using tuple to unpack it to two vertexes
        if start_point in self.gdict:
            # if the start point is already in dict it will look like this
            # gdict{start_point: [end_point]}
            self.gdict[start_point].append(end_point)
        else:
            self.gdict[start_point] = [end_point] # assign start_point as key with value list of end_point

    def get_Edges(self):
        edge_list = []
        for vertex in self.gdict:
            for edge in self.gdict[vertex]:
                if {vertex, edge} not in edge_list:
                    edge_list.append({vertex, edge})
        return edge_list


graph_V_E = {
    "a": ["b", "c"],
    "b": ["a", "d"],
    "C": ["a", "d"],
    "d": ["e"],
    "e": ["d"],
}
my_graph = graph(graph_V_E)
print(my_graph.getVertices())
# my_graph.add_vertex("g")
print(my_graph.getVertices())
# my_graph.add_Edge({"h", "p"})
print(my_graph.get_Edges())


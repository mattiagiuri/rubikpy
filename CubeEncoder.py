# input must contain faces in this order: white, red, green, orange, blue, yellow
from Edge import Edge
from Vertex import Vertex
from Center import Center


class CubeEncoder:

    def __init__(self, cube):
        self.cube = cube
        self.edges = {}
        self.vertexes = {}
        self.centers = {}
        self.get_centers()
        self.get_edges()
        self.get_vertexes()
        self.edge_positions = None
        self.vertex_positions = None

    def get_edges(self):

        def add_edge(name, coordinates):
            edge = Edge(name, coordinates)
            if self.edges.get(edge.name, 0) == 0:
                self.edges[edge.name] = edge
                # print(edge.name)
            else:
                print(edge.name)
                raise RuntimeError('Invalid Disposition')

        add_edge(self.cube[0][0][1] + self.cube[1][2][1], (0, -1, -1))
        add_edge(self.cube[0][1][2] + self.cube[2][2][1], (1, -1, 0))
        add_edge(self.cube[0][2][1] + self.cube[3][2][1], (0, -1, 1))
        add_edge(self.cube[0][1][0] + self.cube[4][2][1], (-1, -1, 0))
        add_edge(self.cube[1][1][0] + self.cube[4][1][2], (-1, 0, -1))
        add_edge(self.cube[1][1][2] + self.cube[2][1][0], (1, 0, -1))
        add_edge(self.cube[3][1][0] + self.cube[2][1][2], (1, 0, 1))
        add_edge(self.cube[3][1][2] + self.cube[4][1][0], (-1, 0, 1))
        add_edge(self.cube[5][2][1] + self.cube[1][0][1], (0, 1, -1))
        add_edge(self.cube[5][1][2] + self.cube[2][0][1], (1, 1, 0))
        add_edge(self.cube[5][0][1] + self.cube[3][0][1], (0, 1, 1))
        add_edge(self.cube[5][1][0] + self.cube[4][0][1], (-1, 1, 0))

        c = self.cube

        # currently not used
        self.edge_positions = [c[0][0][1], c[0][1][0], c[0][1][2], c[0][2][1], c[1][0][1], c[1][1][0], c[1][1][2], c[1][2][1], c[2][0][1], c[2][1][0], c[2][1][2], c[2][2][1], c[3][0][1], c[3][1][0], c[3][1][2], c[3][2][1], c[4][0][1], c[4][1][0], c[4][1][2], c[4][2][1], c[5][0][1], c[5][1][0], c[5][1][2], c[5][2][1]]

    def get_vertexes(self):

        def add_vertex(name, coordinates):
            vertex = Vertex(name, coordinates)
            if self.vertexes.get(vertex.name, 0) == 0:
                self.vertexes[vertex.name] = vertex
                # print(vertex.name)
            else:
                print(vertex.name)
                raise RuntimeError('Invalid Disposition')

        add_vertex(self.cube[0][0][0] + self.cube[1][2][0] + self.cube[4][2][2], (-1, -1, -1))
        add_vertex(self.cube[0][0][2] + self.cube[1][2][2] + self.cube[2][2][0], (1, -1, -1))
        add_vertex(self.cube[0][2][2] + self.cube[2][2][2] + self.cube[3][2][0], (1, -1, 1))
        add_vertex(self.cube[0][2][0] + self.cube[3][2][2] + self.cube[4][2][0], (-1, -1, 1))
        add_vertex(self.cube[5][2][0] + self.cube[1][0][0] + self.cube[4][0][2], (-1, 1, -1))
        add_vertex(self.cube[5][2][2] + self.cube[1][0][2] + self.cube[2][0][0], (1, 1, -1))
        add_vertex(self.cube[5][0][2] + self.cube[2][0][2] + self.cube[3][0][0], (1, 1, 1))
        add_vertex(self.cube[5][0][0] + self.cube[3][0][2] + self.cube[4][0][0], (-1, 1, 1))
        c = self.cube

        # currently not used
        self.vertex_positions = [c[0][0][0], c[0][0][2], c[0][2][0], c[0][2][2], c[1][0][0], c[1][0][2], c[1][2][0], c[1][2][2], c[2][0][0], c[2][0][2], c[2][2][0], c[2][2][2], c[3][0][0], c[3][0][2], c[3][2][0], c[3][2][2], c[4][0][0], c[4][0][2], c[4][2][0], c[4][2][2], c[5][0][0], c[5][0][2], c[5][2][0], c[5][2][2]]

    def get_centers(self):

        def add_center(name):
            center = Center(name)
            if self.centers.get(center.name, 0) == 0:
                self.centers[center.name] = center
            else:
                print(center.name)
                raise RuntimeError('Invalid Disposition')

        add_center('W')
        add_center('R')
        add_center('G')
        add_center('O')
        add_center('U')
        add_center('Y')

    def check_unicity(self):
        coords = []

        for a, b in self.vertexes.items():
            if b.coordinates in coords:
                print(b.coordinates)
                for x, y in self.vertexes.items():
                    print(x, y.coordinates)
                raise RuntimeError('Mistaken Rotation')

            if b.coordinates not in coords:
                coords.append(b.coordinates)

        for a, b in self.edges.items():
            if b.coordinates in coords:
                print(b.coordinates)
                for x, y in self.edges.items():
                    print(x, y.coordinates)
                raise RuntimeError('Mistaken Rotation')

            if b.coordinates not in coords:
                coords.append(b.coordinates)

        return True

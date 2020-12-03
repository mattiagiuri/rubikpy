# input must contain faces in this order: white, red, green, orange, blue, yellow

from CubeEncoder import CubeEncoder
import numpy as np


class CubeMover:

    def __init__(self, cube):
        self.cube = cube
        self.initial_cube = cube.copy()
        self.cube_encoder = CubeEncoder(cube)
        self.moves = ''

    def F(self):
        self.cube[1] = np.rot90(self.cube[1], 3)

        w = np.rot90(self.cube[0], 2)
        u = np.rot90(self.cube[4], 3)
        y = self.cube[5]
        g = np.rot90(self.cube[2], 1)

        rw = w[2].copy()
        ru = u[2].copy()
        ry = y[2].copy()
        rg = g[2].copy()

        w[2] = rg
        u[2] = rw
        y[2] = ru
        g[2] = ry

        self.cube[0] = np.rot90(w, 2)
        self.cube[4] = np.rot90(u, 1)
        self.cube[5] = y
        self.cube[2] = np.rot90(g, 3)

        for a, b in self.cube_encoder.edges.items():
            if b.coordinates == (-1, 0, -1):
                b.coordinates = (0, 1, -1)
            elif b.coordinates == (0, 1, -1):
                b.coordinates = (1, 0, -1)
            elif b.coordinates == (1, 0, -1):
                b.coordinates = (0, -1, -1)
            elif b.coordinates == (0, -1, -1):
                b.coordinates = (-1, 0, -1)

        for a, b in self.cube_encoder.vertexes.items():
            if b.coordinates == (-1, -1, -1):
                b.coordinates = (-1, 1, -1)
            elif b.coordinates == (-1, 1, -1):
                b.coordinates = (1, 1, -1)
            elif b.coordinates == (1, 1, -1):
                b.coordinates = (1, -1, -1)
            elif b.coordinates == (1, -1, -1):
                b.coordinates = (-1, -1, -1)

        self.cube_encoder.check_unicity()
        self.moves = self.moves + 'F'

    def inv_F(self):
        self.cube[1] = np.rot90(self.cube[1], 1)

        w = np.rot90(self.cube[0], 2)
        u = np.rot90(self.cube[4], 3)
        y = self.cube[5]
        g = np.rot90(self.cube[2], 1)

        rw = w[2].copy()
        ru = u[2].copy()
        ry = y[2].copy()
        rg = g[2].copy()

        w[2] = ru
        u[2] = ry
        y[2] = rg
        g[2] = rw

        self.cube[0] = np.rot90(w, 2)
        self.cube[4] = np.rot90(u, 1)
        self.cube[5] = y
        self.cube[2] = np.rot90(g, 3)

        for a, b in self.cube_encoder.edges.items():
            if b.coordinates == (0, 1, -1):
                b.coordinates = (-1, 0, -1)
            elif b.coordinates == (1, 0, -1):
                b.coordinates = (0, 1, -1)
            elif b.coordinates == (0, -1, -1):
                b.coordinates = (1, 0, -1)
            elif b.coordinates == (-1, 0, -1):
                b.coordinates = (0, -1, -1)

        for a, b in self.cube_encoder.vertexes.items():
            if b.coordinates == (-1, 1, -1):
                b.coordinates = (-1, -1, -1)
            elif b.coordinates == (1, 1, -1):
                b.coordinates = (-1, 1, -1)
            elif b.coordinates == (1, -1, -1):
                b.coordinates = (1, 1, -1)
            elif b.coordinates == (-1, -1, -1):
                b.coordinates = (1, -1, -1)

        self.cube_encoder.check_unicity()
        self.moves = self.moves + 'F1'

    def R(self):
        self.cube[2] = np.rot90(self.cube[2], 3)

        w = np.rot90(self.cube[0], 3)
        r = np.rot90(self.cube[1], 3)
        y = np.rot90(self.cube[5], 3)
        o = np.rot90(self.cube[3], 1)

        rw = w[2].copy()
        rr = r[2].copy()
        ry = y[2].copy()
        ro = o[2].copy()

        w[2] = ro
        r[2] = rw
        y[2] = rr
        o[2] = ry

        self.cube[0] = np.rot90(w, 1)
        self.cube[1] = np.rot90(r, 1)
        self.cube[5] = np.rot90(y, 1)
        self.cube[3] = np.rot90(o, 3)

        for a, b in self.cube_encoder.edges.items():
            if b.coordinates == (1, 0, -1):
                b.coordinates = (1, 1, 0)
            elif b.coordinates == (1, 1, 0):
                b.coordinates = (1, 0, 1)
            elif b.coordinates == (1, 0, 1):
                b.coordinates = (1, -1, 0)
            elif b.coordinates == (1, -1, 0):
                b.coordinates = (1, 0, -1)

        for a, b in self.cube_encoder.vertexes.items():
            if b.coordinates == (1, 1, -1):
                b.coordinates = (1, 1, 1)
            elif b.coordinates == (1, 1, 1):
                b.coordinates = (1, -1, 1)
            elif b.coordinates == (1, -1, 1):
                b.coordinates = (1, -1, -1)
            elif b.coordinates == (1, -1, -1):
                b.coordinates = (1, 1, -1)

        self.cube_encoder.check_unicity()
        self.moves = self.moves+'R'

    def inv_R(self):
        self.cube[2] = np.rot90(self.cube[2], 1)

        w = np.rot90(self.cube[0], 3)
        r = np.rot90(self.cube[1], 3)
        y = np.rot90(self.cube[5], 3)
        o = np.rot90(self.cube[3], 1)

        rw = w[2].copy()
        rr = r[2].copy()
        ry = y[2].copy()
        ro = o[2].copy()

        w[2] = rr
        r[2] = ry
        y[2] = ro
        o[2] = rw

        self.cube[0] = np.rot90(w, 1)
        self.cube[1] = np.rot90(r, 1)
        self.cube[5] = np.rot90(y, 1)
        self.cube[3] = np.rot90(o, 3)

        for a, b in self.cube_encoder.edges.items():
            if b.coordinates == (1, 1, 0):
                b.coordinates = (1, 0, -1)
            elif b.coordinates == (1, 0, 1):
                b.coordinates = (1, 1, 0)
            elif b.coordinates == (1, -1, 0):
                b.coordinates = (1, 0, 1)
            elif b.coordinates == (1, 0, -1):
                b.coordinates = (1, -1, 0)

        for a, b in self.cube_encoder.vertexes.items():
            if b.coordinates == (1, 1, 1):
                b.coordinates = (1, 1, -1)
            elif b.coordinates == (1, -1, 1):
                b.coordinates = (1, 1, 1)
            elif b.coordinates == (1, -1, -1):
                b.coordinates = (1, -1, 1)
            elif b.coordinates == (1, 1, -1):
                b.coordinates = (1, -1, -1)

        self.cube_encoder.check_unicity()
        self.moves = self.moves + 'R1'

    def B(self):
        self.cube[3] = np.rot90(self.cube[3], 3)

        w = self.cube[0]
        g = np.rot90(self.cube[2], 3)
        y = np.rot90(self.cube[5], 2)
        b = np.rot90(self.cube[4], 1)

        rw = w[2].copy()
        rg = g[2].copy()
        ry = y[2].copy()
        rb = b[2].copy()

        w[2] = rb
        g[2] = rw
        y[2] = rg
        b[2] = ry

        self.cube[0] = w
        self.cube[2] = np.rot90(g, 1)
        self.cube[5] = np.rot90(y, 2)
        self.cube[4] = np.rot90(b, 3)

        for a, b in self.cube_encoder.edges.items():
            if b.coordinates == (1, 0, 1):
                b.coordinates = (0, 1, 1)
            elif b.coordinates == (0, 1, 1):
                b.coordinates = (-1, 0, 1)
            elif b.coordinates == (-1, 0, 1):
                b.coordinates = (0, -1, 1)
            elif b.coordinates == (0, -1, 1):
                b.coordinates = (1, 0, 1)

        for a, b in self.cube_encoder.vertexes.items():
            if b.coordinates == (1, -1, 1):
                b.coordinates = (1, 1, 1)
            elif b.coordinates == (1, 1, 1):
                b.coordinates = (-1, 1, 1)
            elif b.coordinates == (-1, 1, 1):
                b.coordinates = (-1, -1, 1)
            elif b.coordinates == (-1, -1, 1):
                b.coordinates = (1, -1, 1)

        self.cube_encoder.check_unicity()
        self.moves = self.moves+'B'

    def inv_B(self):
        self.cube[3] = np.rot90(self.cube[3], 1)

        w = self.cube[0]
        g = np.rot90(self.cube[2], 3)
        y = np.rot90(self.cube[5], 2)
        b = np.rot90(self.cube[4], 1)

        rw = w[2].copy()
        rg = g[2].copy()
        ry = y[2].copy()
        rb = b[2].copy()

        w[2] = rg
        g[2] = ry
        y[2] = rb
        b[2] = rw

        self.cube[0] = w
        self.cube[2] = np.rot90(g, 1)
        self.cube[5] = np.rot90(y, 2)
        self.cube[4] = np.rot90(b, 3)

        for a, b in self.cube_encoder.edges.items():
            if b.coordinates == (0, 1, 1):
                b.coordinates = (1, 0, 1)
            elif b.coordinates == (-1, 0, 1):
                b.coordinates = (0, 1, 1)
            elif b.coordinates == (0, -1, 1):
                b.coordinates = (-1, 0, 1)
            elif b.coordinates == (1, 0, 1):
                b.coordinates = (0, -1, 1)

        for a, b in self.cube_encoder.vertexes.items():
            if b.coordinates == (1, 1, 1):
                b.coordinates = (1, -1, 1)
            elif b.coordinates == (-1, 1, 1):
                b.coordinates = (1, 1, 1)
            elif b.coordinates == (-1, -1, 1):
                b.coordinates = (-1, 1, 1)
            elif b.coordinates == (1, -1, 1):
                b.coordinates = (-1, -1, 1)

        self.cube_encoder.check_unicity()
        self.moves = self.moves+'B1'

    def L(self):
        self.cube[4] = np.rot90(self.cube[4], 3)

        w = np.rot90(self.cube[0], 1)
        o = np.rot90(self.cube[3], 3)
        y = np.rot90(self.cube[5], 1)
        r = np.rot90(self.cube[1], 1)

        rw = w[2].copy()
        ro = o[2].copy()
        ry = y[2].copy()
        rr = r[2].copy()

        w[2] = rr
        o[2] = rw
        y[2] = ro
        r[2] = ry

        self.cube[0] = np.rot90(w, 3)
        self.cube[3] = np.rot90(o, 1)
        self.cube[5] = np.rot90(y, 3)
        self.cube[1] = np.rot90(r, 3)

        for a, b in self.cube_encoder.edges.items():
            if b.coordinates == (-1, 0, 1):
                b.coordinates = (-1, 1, 0)
            elif b.coordinates == (-1, 1, 0):
                b.coordinates = (-1, 0, -1)
            elif b.coordinates == (-1, 0, -1):
                b.coordinates = (-1, -1, 0)
            elif b.coordinates == (-1, -1, 0):
                b.coordinates = (-1, 0, 1)

        for a, b in self.cube_encoder.vertexes.items():
            if b.coordinates == (-1, -1, 1):
                b.coordinates = (-1, 1, 1)
            elif b.coordinates == (-1, 1, 1):
                b.coordinates = (-1, 1, -1)
            elif b.coordinates == (-1, 1, -1):
                b.coordinates = (-1, -1, -1)
            elif b.coordinates == (-1, -1, -1):
                b.coordinates = (-1, -1, 1)

        self.cube_encoder.check_unicity()
        self.moves = self.moves+'L'

    def inv_L(self):
        self.cube[4] = np.rot90(self.cube[4], 1)

        w = np.rot90(self.cube[0], 1)
        o = np.rot90(self.cube[3], 3)
        y = np.rot90(self.cube[5], 1)
        r = np.rot90(self.cube[1], 1)

        rw = w[2].copy()
        ro = o[2].copy()
        ry = y[2].copy()
        rr = r[2].copy()

        w[2] = ro
        o[2] = ry
        y[2] = rr
        r[2] = rw

        self.cube[0] = np.rot90(w, 3)
        self.cube[3] = np.rot90(o, 1)
        self.cube[5] = np.rot90(y, 3)
        self.cube[1] = np.rot90(r, 3)

        for a, b in self.cube_encoder.edges.items():
            if b.coordinates == (-1, 1, 0):
                b.coordinates = (-1, 0, 1)
            elif b.coordinates == (-1, 0, -1):
                b.coordinates = (-1, 1, 0)
            elif b.coordinates == (-1, -1, 0):
                b.coordinates = (-1, 0, -1)
            elif b.coordinates == (-1, 0, 1):
                b.coordinates = (-1, -1, 0)

        for a, b in self.cube_encoder.vertexes.items():
            if b.coordinates == (-1, 1, 1):
                b.coordinates = (-1, -1, 1)
            elif b.coordinates == (-1, 1, -1):
                b.coordinates = (-1, 1, 1)
            elif b.coordinates == (-1, -1, -1):
                b.coordinates = (-1, 1, -1)
            elif b.coordinates == (-1, -1, 1):
                b.coordinates = (-1, -1, -1)

        self.cube_encoder.check_unicity()
        self.moves = self.moves+'L1'

    def D(self):
        self.cube[0] = np.rot90(self.cube[0], 3)

        r = self.cube[1]
        g = self.cube[2]
        o = self.cube[3]
        b = self.cube[4]

        rr = r[2].copy()
        rg = g[2].copy()
        ro = o[2].copy()
        rb = b[2].copy()

        r[2] = rb
        g[2] = rr
        o[2] = rg
        b[2] = ro

        self.cube[1] = r
        self.cube[2] = g
        self.cube[3] = o
        self.cube[4] = b

        for a, b in self.cube_encoder.edges.items():
            if b.coordinates == (0, -1, -1):
                b.coordinates = (1, -1, 0)
            elif b.coordinates == (1, -1, 0):
                b.coordinates = (0, -1, 1)
            elif b.coordinates == (0, -1, 1):
                b.coordinates = (-1, -1, 0)
            elif b.coordinates == (-1, -1, 0):
                b.coordinates = (0, -1, -1)

        for a, b in self.cube_encoder.vertexes.items():
            if b.coordinates == (-1, -1, -1):
                b.coordinates = (1, -1, -1)
            elif b.coordinates == (1, -1, -1):
                b.coordinates = (1, -1, 1)
            elif b.coordinates == (1, -1, 1):
                b.coordinates = (-1, -1, 1)
            elif b.coordinates == (-1, -1, 1):
                b.coordinates = (-1, -1, -1)

        self.cube_encoder.check_unicity()
        self.moves = self.moves+'D'

    def inv_D(self):
        self.cube[0] = np.rot90(self.cube[0], 1)

        r = self.cube[1]
        g = self.cube[2]
        o = self.cube[3]
        b = self.cube[4]

        rr = r[2].copy()
        rg = g[2].copy()
        ro = o[2].copy()
        rb = b[2].copy()

        r[2] = rg
        g[2] = ro
        o[2] = rb
        b[2] = rr

        self.cube[1] = r
        self.cube[2] = g
        self.cube[3] = o
        self.cube[4] = b

        for a, b in self.cube_encoder.edges.items():
            if b.coordinates == (1, -1, 0):
                b.coordinates = (0, -1, -1)
            elif b.coordinates == (0, -1, 1):
                b.coordinates = (1, -1, 0)
            elif b.coordinates == (-1, -1, 0):
                b.coordinates = (0, -1, 1)
            elif b.coordinates == (0, -1, -1):
                b.coordinates = (-1, -1, 0)

        for a, b in self.cube_encoder.vertexes.items():
            if b.coordinates == (1, -1, -1):
                b.coordinates = (-1, -1, -1)
            elif b.coordinates == (1, -1, 1):
                b.coordinates = (1, -1, -1)
            elif b.coordinates == (-1, -1, 1):
                b.coordinates = (1, -1, 1)
            elif b.coordinates == (-1, -1, -1):
                b.coordinates = (-1, -1, 1)

        self.cube_encoder.check_unicity()
        self.moves = self.moves+'D1'

    def inv_U(self):
        self.cube[5] = np.rot90(self.cube[5], 1)

        r = self.cube[1]
        g = self.cube[2]
        o = self.cube[3]
        b = self.cube[4]

        rr = r[0].copy()
        rg = g[0].copy()
        ro = o[0].copy()
        rb = b[0].copy()

        r[0] = rb
        g[0] = rr
        o[0] = rg
        b[0] = ro

        self.cube[1] = r
        self.cube[2] = g
        self.cube[3] = o
        self.cube[4] = b

        for a, b in self.cube_encoder.edges.items():
            if b.coordinates == (0, 1, -1):
                b.coordinates = (1, 1, 0)
            elif b.coordinates == (1, 1, 0):
                b.coordinates = (0, 1, 1)
            elif b.coordinates == (0, 1, 1):
                b.coordinates = (-1, 1, 0)
            elif b.coordinates == (-1, 1, 0):
                b.coordinates = (0, 1, -1)

        for a, b in self.cube_encoder.vertexes.items():
            if b.coordinates == (-1, 1, -1):
                b.coordinates = (1, 1, -1)
            elif b.coordinates == (1, 1, -1):
                b.coordinates = (1, 1, 1)
            elif b.coordinates == (1, 1, 1):
                b.coordinates = (-1, 1, 1)
            elif b.coordinates == (-1, 1, 1):
                b.coordinates = (-1, 1, -1)

        self.cube_encoder.check_unicity()
        self.moves = self.moves+'U1'

    def U(self):
        self.cube[5] = np.rot90(self.cube[5], 3)

        r = self.cube[1]
        g = self.cube[2]
        o = self.cube[3]
        b = self.cube[4]

        rr = r[0].copy()
        rg = g[0].copy()
        ro = o[0].copy()
        rb = b[0].copy()

        r[0] = rg
        g[0] = ro
        o[0] = rb
        b[0] = rr

        self.cube[1] = r
        self.cube[2] = g
        self.cube[3] = o
        self.cube[4] = b

        for a, b in self.cube_encoder.edges.items():
            if b.coordinates == (1, 1, 0):
                b.coordinates = (0, 1, -1)
            elif b.coordinates == (0, 1, 1):
                b.coordinates = (1, 1, 0)
            elif b.coordinates == (-1, 1, 0):
                b.coordinates = (0, 1, 1)
            elif b.coordinates == (0, 1, -1):
                b.coordinates = (-1, 1, 0)

        for a, b in self.cube_encoder.vertexes.items():
            if b.coordinates == (1, 1, -1):
                b.coordinates = (-1, 1, -1)
            elif b.coordinates == (1, 1, 1):
                b.coordinates = (1, 1, -1)
            elif b.coordinates == (-1, 1, 1):
                b.coordinates = (1, 1, 1)
            elif b.coordinates == (-1, 1, -1):
                b.coordinates = (-1, 1, 1)

        self.cube_encoder.check_unicity()
        self.moves = self.moves+'U'

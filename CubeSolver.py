# input must contain faces in this order: white, red, green, orange, blue, yellow

import numpy as np
from CubeMover import CubeMover


class CubeSolver:

    def __init__(self, cube):
        self.mover = CubeMover(cube)
        self.cube = cube
        self.yellow_crossed = False
        self.yellow_vertexes = False
        self.solve_cube()

    def sexy_moves(self):
        self.mover.R()
        self.mover.U()
        self.mover.inv_R()
        self.mover.inv_U()

    def anti_sexy_moves(self):
        self.mover.U()
        self.mover.R()
        self.mover.inv_U()
        self.mover.inv_R()

    def adjust_white_edge(self, name):
        c = self.mover.cube_encoder.edges[name].coordinates
        cube = self.mover.cube
        if c == (1, 0, -1):
            if cube[2][1][0] == 'W':
                self.mover.F()
            else:
                self.mover.D()
                self.mover.inv_R()
                self.mover.inv_D()
        elif c == (-1, 0, -1):
            if cube[4][1][2] == 'W':
                self.mover.inv_F()
            else:
                self.mover.inv_D()
                self.mover.L()
                self.mover.D()
        elif c == (0, 1, -1):
            if cube[1][0][1] == 'W':
                self.mover.F()
                self.mover.D()
                self.mover.inv_R()
                self.mover.inv_D()
            else:
                self.mover.F()
                self.mover.F()
        elif c == (1, 1, 0):
            self.mover.U()
            if cube[1][0][1] == 'W':
                self.mover.F()
                self.mover.D()
                self.mover.inv_R()
                self.mover.inv_D()
            else:
                self.mover.F()
                self.mover.F()
        elif c == (0, 1, 1):
            self.mover.U()
            self.mover.U()
            if cube[1][0][1] == 'W':
                self.mover.F()
                self.mover.D()
                self.mover.inv_R()
                self.mover.inv_D()
            else:
                self.mover.F()
                self.mover.F()
        elif c == (-1, 1, 0):
            self.mover.inv_U()
            if cube[1][0][1] == 'W':
                self.mover.F()
                self.mover.D()
                self.mover.inv_R()
                self.mover.inv_D()
            else:
                self.mover.F()
                self.mover.F()

        elif c == (1, 0, 1):
            self.mover.B()
            self.mover.U()
            self.mover.U()
            self.mover.inv_B()
            if cube[1][0][1] == 'W':
                self.mover.F()
                self.mover.D()
                self.mover.inv_R()
                self.mover.inv_D()
            else:
                self.mover.F()
                self.mover.F()

        elif c == (-1, 0, 1):
            self.mover.inv_B()
            self.mover.U()
            self.mover.U()
            self.mover.B()
            if cube[1][0][1] == 'W':
                self.mover.F()
                self.mover.D()
                self.mover.inv_R()
                self.mover.inv_D()
            else:
                self.mover.F()
                self.mover.F()

        elif c == (0, -1, -1):
            if cube[1][2][1] == 'W':
                self.mover.inv_F()
                self.mover.D()
                self.mover.inv_R()
                self.mover.inv_D()

        elif c == (-1, -1, 0):
            self.mover.inv_L()
            if cube[4][1][2] == 'W':
                self.mover.inv_F()
            else:
                self.mover.inv_D()
                self.mover.L()
                self.mover.D()

        elif c == (0, -1, 1):
            self.mover.B()
            self.mover.B()
            self.mover.U()
            self.mover.U()
            if cube[1][0][1] == 'W':
                self.mover.F()
                self.mover.D()
                self.mover.inv_R()
                self.mover.inv_D()
            else:
                self.mover.F()
                self.mover.F()

        elif c == (1, -1, 0):
            self.mover.R()
            if cube[2][1][0] == 'W':
                self.mover.F()
            else:
                self.mover.D()
                self.mover.inv_R()
                self.mover.inv_D()

    def solve_white_cross(self):
        self.adjust_white_edge('WR')
        self.mover.inv_D()
        self.adjust_white_edge('WG')
        self.mover.inv_D()
        self.adjust_white_edge('WO')
        self.mover.inv_D()
        self.adjust_white_edge('WU')
        self.mover.inv_D()
        self.mover.moves = self.mover.moves+'\n'

    def solve_vertex_base_case(self, cube):
        if cube[5][2][2] == 'W':
            self.sexy_moves()
            self.sexy_moves()
            self.sexy_moves()
        elif cube[2][0][0] == 'W':
            self.sexy_moves()
        else:
            self.anti_sexy_moves()

    def adjust_white_vertex(self, name):
        c = self.mover.cube_encoder.vertexes[name].coordinates
        cube = self.mover.cube

        if c == (1, 1, -1):
            self.solve_vertex_base_case(cube)

        elif c == (1, 1, 1):
            self.mover.U()
            self.solve_vertex_base_case(cube)

        elif c == (-1, 1, 1):
            self.mover.U()
            self.mover.U()
            self.solve_vertex_base_case(cube)

        elif c == (-1, 1, -1):
            self.mover.inv_U()
            self.solve_vertex_base_case(cube)

        elif c == (1, -1, -1):
            if not cube[0][0][2] == 'W':
                self.sexy_moves()
                self.solve_vertex_base_case(cube)

        elif c == (1, -1, 1):
            self.mover.B()
            self.mover.U()
            self.mover.inv_B()
            self.solve_vertex_base_case(cube)

        elif c == (-1, -1, 1):
            self.mover.L()
            self.mover.U()
            self.mover.U()
            self.mover.inv_L()
            self.solve_vertex_base_case(cube)

        elif c == (-1, -1, -1):
            self.mover.F()
            self.mover.inv_U()
            self.mover.inv_F()
            self.mover.inv_U()
            self.solve_vertex_base_case(cube)

    def finish_white_face(self):
        self.adjust_white_vertex('WRG')
        self.mover.inv_D()
        self.mover.moves = self.mover.moves + '\n'
        self.adjust_white_vertex('WGO')
        self.mover.inv_D()
        self.mover.moves = self.mover.moves + '\n'
        self.adjust_white_vertex('WOU')
        self.mover.inv_D()
        self.mover.moves = self.mover.moves + '\n'
        self.adjust_white_vertex('WRU')
        self.mover.inv_D()
        self.mover.moves = self.mover.moves + '\n'

    def R_to_G(self):
        self.anti_sexy_moves()
        self.mover.inv_U()
        self.mover.inv_F()
        self.mover.U()
        self.mover.F()

    def R_to_U(self):
        self.mover.inv_U()
        self.mover.inv_L()
        self.mover.U()
        self.mover.L()
        self.mover.U()
        self.mover.F()
        self.mover.inv_U()
        self.mover.inv_F()

    def G_to_R(self):
        self.mover.inv_U()
        self.mover.inv_F()
        self.mover.U()
        self.mover.F()
        self.mover.U()
        self.mover.R()
        self.mover.inv_U()
        self.mover.inv_R()

    def G_to_O(self):
        self.mover.U()
        self.mover.B()
        self.mover.inv_U()
        self.mover.inv_B()
        self.mover.inv_U()
        self.mover.inv_R()
        self.mover.U()
        self.mover.R()

    def O_to_G(self):
        self.mover.inv_U()
        self.mover.inv_R()
        self.mover.U()
        self.mover.R()
        self.mover.U()
        self.mover.B()
        self.mover.inv_U()
        self.mover.inv_B()

    def O_to_U(self):
        self.mover.U()
        self.mover.L()
        self.mover.inv_U()
        self.mover.inv_L()
        self.mover.inv_U()
        self.mover.inv_B()
        self.mover.U()
        self.mover.B()

    def U_to_O(self):
        self.mover.inv_U()
        self.mover.inv_B()
        self.mover.U()
        self.mover.B()
        self.mover.U()
        self.mover.L()
        self.mover.inv_U()
        self.mover.inv_L()

    def U_to_R(self):
        self.mover.U()
        self.mover.F()
        self.mover.inv_U()
        self.mover.inv_F()
        self.mover.inv_U()
        self.mover.inv_L()
        self.mover.U()
        self.mover.L()

    def adjust_RG(self):
        c = self.mover.cube_encoder.edges['RG'].coordinates
        cube = self.mover.cube

        if c == (1, 1, 0):
            if cube[2][0][1] == 'G':
                self.G_to_R()
            else:
                self.mover.U()
                self.R_to_G()

        elif c == (0, 1, -1):
            if cube[1][0][1] == 'R':
                self.R_to_G()
            else:
                self.mover.inv_U()
                self.G_to_R()

        elif c == (-1, 1, 0):
            if cube[4][0][1] == 'R':
                self.mover.inv_U()
                self.R_to_G()
            else:
                self.mover.U()
                self.mover.U()
                self.G_to_R()

        elif c == (0, 1, 1):
            if cube[3][0][1] == 'G':
                self.mover.U()
                self.G_to_R()
            else:
                self.mover.U()
                self.mover.U()
                self.R_to_G()

        elif c == (1, 0, -1):
            if cube[1][1][2] == 'G':
                self.R_to_G()
                self.mover.U()
                self.mover.U()
                self.R_to_G()

        elif c == (1, 0, 1):
            self.G_to_O()
            if cube[4][0][1] == 'R':
                self.mover.inv_U()
                self.R_to_G()
            else:
                self.mover.U()
                self.mover.U()
                self.G_to_R()

        elif c == (-1, 0, 1):
            self.O_to_U()
            if cube[1][0][1] == 'R':
                self.R_to_G()
            else:
                self.mover.inv_U()
                self.G_to_R()

        elif c == (-1, 0, -1):
            self.U_to_R()
            if cube[2][0][1] == 'G':
                self.G_to_R()
            else:
                self.mover.U()
                self.R_to_G()

    def adjust_GO(self):
        c = self.mover.cube_encoder.edges['GO'].coordinates
        cube = self.mover.cube

        if c == (1, 1, 0):
            if cube[2][0][1] == 'O':
                self.mover.inv_U()
                self.O_to_G()
            else:
                self.G_to_O()

        elif c == (0, 1, -1):
            if cube[1][0][1] == 'O':
                self.mover.U()
                self.mover.U()
                self.O_to_G()
            else:
                self.mover.inv_U()
                self.G_to_O()

        elif c == (-1, 1, 0):
            if cube[4][0][1] == 'O':
                self.mover.U()
                self.O_to_G()
            else:
                self.mover.U()
                self.mover.U()
                self.G_to_O()

        elif c == (0, 1, 1):
            if cube[3][0][1] == 'O':
                self.O_to_G()
            else:
                self.mover.U()
                self.G_to_O()

        elif c == (1, 0, -1):
            self.R_to_G()
            if cube[3][0][1] == 'O':
                self.O_to_G()
            else:
                self.mover.U()
                self.G_to_O()

        elif c == (1, 0, 1):
            if cube[2][1][2] == 'O':
                self.G_to_O()
                self.mover.U()
                self.mover.U()
                self.G_to_O()

        elif c == (-1, 0, 1):
            self.O_to_U()
            if cube[1][0][1] == 'O':
                self.mover.U()
                self.mover.U()
                self.O_to_G()
            else:
                self.mover.inv_U()
                self.G_to_O()

        elif c == (-1, 0, -1):
            self.U_to_R()
            if cube[2][0][1] == 'O':
                self.mover.inv_U()
                self.O_to_G()
            else:
                self.G_to_O()

    def adjust_OU(self):
        c = self.mover.cube_encoder.edges['OU'].coordinates
        cube = self.mover.cube

        if c == (1, 1, 0):
            if cube[2][0][1] == 'U':
                self.mover.U()
                self.mover.U()
                self.U_to_O()
            else:
                self.mover.inv_U()
                self.O_to_U()

        elif c == (0, 1, -1):
            if cube[1][0][1] == 'U':
                self.mover.U()
                self.U_to_O()
            else:
                self.mover.U()
                self.mover.U()
                self.O_to_U()

        elif c == (-1, 1, 0):
            if cube[4][0][1] == 'U':
                self.U_to_O()
            else:
                self.mover.U()
                self.O_to_U()

        elif c == (0, 1, 1):
            if cube[3][0][1] == 'U':
                self.mover.inv_U()
                self.U_to_O()
            else:
                self.O_to_U()

        elif c == (1, 0, -1):
            self.R_to_G()
            if cube[3][0][1] == 'U':
                self.mover.inv_U()
                self.U_to_O()
            else:
                self.O_to_U()

        elif c == (1, 0, 1):
            self.G_to_O()
            if cube[4][0][1] == 'U':
                self.U_to_O()
            else:
                self.mover.U()
                self.O_to_U()

        elif c == (-1, 0, 1):
            if cube[3][1][2] == 'U':
                self.O_to_U()
                self.mover.U()
                self.mover.U()
                self.O_to_U()

        elif c == (-1, 0, -1):
            self.U_to_R()
            if cube[2][0][1] == 'U':
                self.mover.U()
                self.mover.U()
                self.U_to_O()
            else:
                self.mover.inv_U()
                self.O_to_U()

    def adjust_RU(self):
        c = self.mover.cube_encoder.edges['RU'].coordinates
        cube = self.mover.cube

        if c == (1, 1, 0):
            if cube[2][0][1] == 'R':
                self.mover.U()
                self.R_to_U()
            else:
                self.mover.U()
                self.mover.U()
                self.U_to_R()

        elif c == (0, 1, -1):
            if cube[1][0][1] == 'R':
                self.R_to_U()
            else:
                self.mover.U()
                self.U_to_R()

        elif c == (-1, 1, 0):
            if cube[4][0][1] == 'R':
                self.mover.inv_U()
                self.R_to_U()
            else:
                self.U_to_R()

        elif c == (0, 1, 1):
            if cube[3][0][1] == 'R':
                self.mover.U()
                self.mover.U()
                self.R_to_U()
            else:
                self.mover.inv_U()
                self.U_to_R()

        elif c == (1, 0, -1):
            self.R_to_G()
            if cube[3][0][1] == 'R':
                self.mover.U()
                self.mover.U()
                self.R_to_U()
            else:
                self.mover.inv_U()
                self.U_to_R()

        elif c == (1, 0, 1):
            self.G_to_O()
            if cube[4][0][1] == 'R':
                self.mover.inv_U()
                self.R_to_U()
            else:
                self.U_to_R()

        elif c == (-1, 0, 1):
            self.O_to_U()
            if cube[1][0][1] == 'R':
                self.R_to_U()
            else:
                self.mover.U()
                self.U_to_R()

        elif c == (-1, 0, -1):
            if cube[4][1][2] == 'R':
                self.U_to_R()
                self.mover.U()
                self.mover.U()
                self.U_to_R()

    def solve_second_layer(self):
        self.adjust_RG()
        self.mover.moves = self.mover.moves + '\n'
        self.adjust_GO()
        self.mover.moves = self.mover.moves + '\n'
        self.adjust_OU()
        self.mover.moves = self.mover.moves + '\n'
        self.adjust_RU()
        self.mover.moves = self.mover.moves + '\n'

    def solve_L(self):
        self.mover.F()
        self.mover.U()
        self.mover.R()
        self.mover.inv_U()
        self.mover.inv_R()
        self.mover.inv_F()

    def solve_line(self):
        self.mover.F()
        self.mover.R()
        self.mover.U()
        self.mover.inv_R()
        self.mover.inv_U()
        self.mover.inv_F()

    def make_yellow_cross(self):
        cube = self.mover.cube
        if not (cube[5][0][1] == 'Y' and cube[5][1][0] == 'Y' and cube[5][1][2] == 'Y' and cube[5][2][1] == 'Y'):

            if not (cube[5][0][1] == 'Y' or cube[5][1][0] == 'Y' or cube[5][1][2] == 'Y' or cube[5][2][1] == 'Y'):
                self.solve_line()
                self.solve_L()

            elif cube[5][0][1] == 'Y' and cube[5][1][0] == 'Y':
                self.solve_L()

            elif cube[5][0][1] == 'Y' and cube[5][1][2] == 'Y':
                self.mover.inv_U()
                self.solve_L()

            elif cube[5][2][1] == 'Y' and cube[5][1][2] == 'Y':
                self.mover.U()
                self.mover.U()
                self.solve_L()

            elif cube[5][2][1] == 'Y' and cube[5][1][2] == 'Y':
                self.mover.U()
                self.solve_L()

            elif cube[5][1][0] == 'Y' and cube[5][1][2] == 'Y':
                self.solve_line()

            elif cube[5][0][1] == 'Y' and cube[5][2][1] == 'Y':
                self.mover.U()
                self.solve_line()

            self.mover.moves = self.mover.moves + '\n'

    def sune_R(self):
        self.mover.R()
        self.mover.U()
        self.mover.inv_R()
        self.mover.U()
        self.mover.R()
        self.mover.U()
        self.mover.U()
        self.mover.inv_R()

    def sune_G(self):
        self.mover.B()
        self.mover.U()
        self.mover.inv_B()
        self.mover.U()
        self.mover.B()
        self.mover.U()
        self.mover.U()
        self.mover.inv_B()

    def sune_O(self):
        self.mover.L()
        self.mover.U()
        self.mover.inv_L()
        self.mover.U()
        self.mover.L()
        self.mover.U()
        self.mover.U()
        self.mover.inv_L()

    def sune_U(self):
        self.mover.F()
        self.mover.U()
        self.mover.inv_F()
        self.mover.U()
        self.mover.F()
        self.mover.U()
        self.mover.U()
        self.mover.inv_F()

    def check_yellow_cross_positions(self):
        cube = self.mover.cube

        if cube[1][0][1] == 'R' and cube[4][0][1] == 'U':
            self.sune_O()
            self.yellow_crossed = True

        elif cube[1][0][1] == 'R' and cube[2][0][1] == 'G':
            self.sune_U()
            self.yellow_crossed = True

        elif cube[2][0][1] == 'G' and cube[3][0][1] == 'O':
            self.sune_R()
            self.yellow_crossed = True

        elif cube[3][0][1] == 'O' and cube[4][0][1] == 'U':
            self.sune_G()
            self.yellow_crossed = True

        elif cube[1][0][1] == 'R' and cube[3][0][1] == 'O':
            self.sune_G()
            self.sune_R()
            self.yellow_crossed = True

        elif cube[4][0][1] == 'U' and cube[2][0][1] == 'G':
            self.sune_R()
            self.sune_U()
            self.yellow_crossed = True

        self.mover.U()
        self.mover.moves = self.mover.moves + '\n'

    def adjust_yellow_cross_edges(self):
        cube = self.mover.cube
        a = (cube[1][0][1] == 'R' and cube[2][0][1] == 'G' and cube[3][0][1] == 'O' and cube[4][0][1] == 'U')
        b = (cube[2][0][1] == 'R' and cube[3][0][1] == 'G' and cube[4][0][1] == 'O' and cube[1][0][1] == 'U')
        c = (cube[3][0][1] == 'R' and cube[4][0][1] == 'G' and cube[1][0][1] == 'O' and cube[2][0][1] == 'U')
        d = (cube[4][0][1] == 'R' and cube[1][0][1] == 'G' and cube[2][0][1] == 'O' and cube[3][0][1] == 'U')
        if a:
            self.yellow_crossed = True
            self.mover.moves = self.mover.moves + '\n'

        elif b:
            self.yellow_crossed = True
            self.mover.U()
            self.mover.moves = self.mover.moves + '\n'

        elif c:
            self.yellow_crossed = True
            self.mover.U()
            self.mover.U()
            self.mover.moves = self.mover.moves + '\n'

        elif d:
            self.yellow_crossed = True
            self.mover.inv_U()
            self.mover.moves = self.mover.moves + '\n'

        elif not (a or b or c or d):
            while not self.yellow_crossed:
                self.check_yellow_cross_positions()

    def check_yellow_vertexes(self):
        v = self.mover.cube_encoder.vertexes

        if v['RGY'].coordinates == v['RGY'].final_coordinates:
            self.mover.B()
            self.mover.inv_U()
            self.mover.inv_F()
            self.mover.U()
            self.mover.inv_B()
            self.mover.inv_U()
            self.mover.F()
            self.mover.U()

        elif v['GOY'].coordinates == v['GOY'].final_coordinates:
            self.mover.L()
            self.mover.inv_U()
            self.mover.inv_R()
            self.mover.U()
            self.mover.inv_L()
            self.mover.inv_U()
            self.mover.R()
            self.mover.U()

        elif v['OUY'].coordinates == v['OUY'].final_coordinates:
            self.mover.F()
            self.mover.inv_U()
            self.mover.inv_B()
            self.mover.U()
            self.mover.inv_F()
            self.mover.inv_U()
            self.mover.B()
            self.mover.U()

        elif v['RUY'].coordinates == v['RUY'].final_coordinates:
            self.mover.R()
            self.mover.inv_U()
            self.mover.inv_L()
            self.mover.U()
            self.mover.inv_R()
            self.mover.inv_U()
            self.mover.L()
            self.mover.U()

        else:
            self.mover.R()
            self.mover.inv_U()
            self.mover.inv_L()
            self.mover.U()
            self.mover.inv_R()
            self.mover.inv_U()
            self.mover.L()
            self.mover.U()

    def adjust_yellow_vertexes(self):
        v = self.mover.cube_encoder.vertexes

        while not self.yellow_vertexes:
            self.check_yellow_vertexes()
            if v['RGY'].coordinates == v['RGY'].final_coordinates and v['GOY'].coordinates == v['GOY'].final_coordinates and v['OUY'].coordinates == v['OUY'].final_coordinates and v['RUY'].coordinates == v['RUY'].final_coordinates:
                self.yellow_vertexes = True
            self.mover.moves = self.mover.moves+'\n'

    def final_sexy_moves(self):
        self.mover.L()
        self.mover.D()
        self.mover.inv_L()
        self.mover.inv_D()

    def finish_yellow_face(self):
        cube = self.mover.cube

        for i in range(4):

            if cube[1][0][0] == 'Y':
                self.final_sexy_moves()
                self.final_sexy_moves()
                self.final_sexy_moves()
                self.final_sexy_moves()

            elif cube[4][0][2] == 'Y':
                self.final_sexy_moves()
                self.final_sexy_moves()

            self.mover.U()
            self.mover.moves = self.mover.moves + '\n'

    def solve_cube(self):
        self.solve_white_cross()
        self.finish_white_face()
        self.solve_second_layer()
        self.make_yellow_cross()
        self.adjust_yellow_cross_edges()
        self.adjust_yellow_vertexes()
        self.finish_yellow_face()

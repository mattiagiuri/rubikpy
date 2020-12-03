from CubeSolver import CubeSolver
import numpy as np

# disposition = np.array([[['U', 'G', 'Y'],
#                          ['U', 'W', 'O'],
#                          ['R', 'Y', 'W']],
#                         [['G', 'G', 'U'],
#                          ['Y', 'R', 'G'],
#                          ['O', 'Y', 'U']],
#                         [['R', 'R', 'O'],
#                          ['W', 'G', 'O'],
#                          ['O', 'Y', 'R']],
#                         [['G', 'G', 'Y'],
#                          ['W', 'O', 'O'],
#                          ['G', 'U', 'W']],
#                         [['R', 'U', 'Y'],
#                          ['U', 'U', 'R'],
#                          ['U', 'R', 'W']],
#                         [['G', 'R', 'W'],
#                          ['W', 'Y', 'W'],
#                          ['O', 'O', 'Y']]
#                         ])

disposition = np.array([[['G', 'U', 'W'],
                         ['Y', 'W', 'Y'],
                         ['U', 'G', 'Y']],
                        [['R', 'R', 'O'],
                         ['O', 'R', 'U'],
                         ['O', 'O', 'O']],
                        [['G', 'G', 'Y'],
                         ['Y', 'G', 'W'],
                         ['U', 'O', 'R']],
                        [['R', 'O', 'U'],
                         ['U', 'O', 'R'],
                         ['U', 'R', 'R']],
                        [['Y', 'G', 'G'],
                         ['U', 'U', 'G'],
                         ['W', 'R', 'Y']],
                        [['O', 'W', 'G'],
                         ['Y', 'Y', 'W'],
                         ['W', 'W', 'W']]
                        ])

sample_input = np.array([[['G', 'U', 'W'],
                          ['Y', 'W', 'Y'],
                          ['U', 'G', 'Y']],
                         [['R', 'R', 'O'],
                          ['O', 'R', 'U'],
                          ['O', 'O', 'O']],
                         [['G', 'G', 'Y'],
                          ['Y', 'G', 'W'],
                          ['U', 'O', 'R']],
                         [['R', 'O', 'U'],
                          ['U', 'O', 'R'],
                          ['U', 'R', 'R']],
                         [['Y', 'G', 'G'],
                          ['U', 'U', 'G'],
                          ['W', 'R', 'Y']],
                         [['O', 'W', 'G'],
                          ['Y', 'Y', 'W'],
                          ['W', 'W', 'W']]
                         ])

print('input must be a numpy array and contain faces in this order: white, red, green, orange, blue, yellow')
print(sample_input)
print('white face input considered as if you had red face on top')
print('yellow face input considered as if you had orange face on top')
print('the other faces are considered as if you had yellow face on top')
print('while you solve the cube, you should look to the red face with yellow face on top')
print('F = move front (red) face clockwise, F1 = move front (red) face anticlockwise')
print('R = move right (green) face clockwise, R1 = move right (green) face anticlockwise')
print('B = move back (orange) face clockwise, B1 = move back (orange) face anticlockwise')
print('L = move left (blue) face clockwise, L1 = move left (blue) face anticlockwise')
print('U = move up (yellow) face clockwise, U1 = move up (yellow) face anticlockwise')
print('D = move down (white) face clockwise, D1 = move down (white) face anticlockwise')
print('\n\n')

solver = CubeSolver(disposition)

print(solver.mover.moves)
print(solver.mover.cube)
print(solver.mover.initial_cube)

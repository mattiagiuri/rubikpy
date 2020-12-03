import numpy as np
from CubeEncoder import CubeEncoder

disposition = np.array([[['W', 'W', 'W'],
                         ['W', 'W', 'W'],
                         ['W', 'W', 'W']],
                        [['R', 'R', 'R'],
                         ['R', 'R', 'R'],
                         ['R', 'R', 'R']],
                        [['G', 'G', 'G'],
                         ['G', 'G', 'G'],
                         ['G', 'G', 'G']],
                        [['O', 'O', 'O'],
                         ['O', 'O', 'O'],
                         ['O', 'O', 'O']],
                        [['U', 'U', 'U'],
                         ['U', 'U', 'U'],
                         ['U', 'U', 'U']],
                        [['Y', 'Y', 'Y'],
                         ['Y', 'Y', 'Y'],
                         ['Y', 'Y', 'Y']]
                        ])

cuber = CubeEncoder(disposition)

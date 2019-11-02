#
# Created by Brendan Berg on 01.11.2019
#

import numpy as np

from mesh import *


def init_velocity_field(mesh_geometry):
    return 0.0 * np.ones([mesh_geometry.mesh_cells_y, mesh_geometry.mesh_cells_x, 2])


def init_pressure_field(mesh_geometry):
    return 1.0 * np.ones([mesh_geometry.mesh_cells_y, mesh_geometry.mesh_cells_x])

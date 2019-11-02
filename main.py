#
# Created by Brendan Berg on 01.11.2019
#

import numpy as np
import matplotlib.pyplot as plt

from mesh import *
from lid_driven_cavity_flow import *
from simple_fvm import *


mesh_geometry = MeshGeometry(mesh_cells_x=10, mesh_cells_y=5, mesh_size_x=2.0, mesh_size_y=1.0, mesh_depth=0.1)
simple_fvm = SimpleFVM(3)


# fields and initial conditions

velocity_field = init_velocity_field(mesh_geometry)
pressure_field = init_pressure_field(mesh_geometry)


# SIMPLE algorithm

while simple_fvm.iterate():
    # solve for velocity field
    next_velocity_field = solve_for_velocity_field(velocity_field, pressure_field)

    # solve for pressure field
    next_pressure_field = pressure_field

    # correct velocity field

    # apply iteration
    velocity_field = next_velocity_field
    pressure_field = next_pressure_field

    velocity_field_x = velocity_field[:, :, 0]
    velocity_field_y = velocity_field[:, :, 1]

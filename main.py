#
# Created by Brendan Berg on 01.11.2019
#

import numpy as np
import matplotlib.pyplot as plt

from mesh import *
from lid_driven_cavity_flow import *


# input

mesh_cells_x = 10                   # [#]
mesh_cells_y = 20                   # [#]
mesh_size_x = 1.0                   # [m]
mesh_size_y = 1.0                   # [m]
mesh_depth = 0.1                    # [m]

simple_iterations = 3


# mesh

faces_x, faces_y = generate_cartesian_mesh_face_positions(0, mesh_size_x, mesh_cells_x, 0, mesh_size_y, mesh_cells_y)
centroids_x, centroids_y = centroids_from_face_positions(faces_x, faces_y)
cell_sizes_x, cell_sizes_y = cell_sizes_from_face_positions(faces_x, faces_y)
face_areas_x, face_areas_y = face_area_from_cell_sizes(cell_sizes_x, cell_sizes_y, mesh_depth)
cell_volumes = cell_volumes_from_cell_sizes(cell_sizes_x, cell_sizes_y, mesh_depth)


# fields and initial conditions

velocity_field = init_velocity_field(mesh_cells_x, mesh_cells_y)
pressure_field = init_pressure_field(mesh_cells_x, mesh_cells_y)


# SIMPLE algorithm

for iteration in range(simple_iterations):
    # apply boundary conditions
    next_velocity_field = apply_boundary_conditions_for_velocity_field(velocity_field)
    next_pressure_field = apply_boundary_conditions_for_pressure_field(pressure_field)

    # solve for velocity field

    # solve for pressure field

    # correct velocity field

    # apply iteration
    velocity_field = next_velocity_field
    pressure_field = next_pressure_field

    velocity_field_x = velocity_field[:, :, 0]
    velocity_field_y = velocity_field[:, :, 1]

#
# Created by Brendan Berg on 01.11.2019
#

import numpy as np


def init_velocity_field(mesh_cells_x, mesh_cells_y):
    return 0.0 * np.ones([mesh_cells_y, mesh_cells_x, 2])


def init_pressure_field(mesh_cells_x, mesh_cells_y):
    return 1.0 * np.ones([mesh_cells_y, mesh_cells_x])


def apply_boundary_conditions_for_velocity_field(velocity_field):
    next_velocity_field = velocity_field

    next_velocity_field[:, 0, 0] = 0.0 * np.ones(next_velocity_field[:, 0, 0].shape)
    next_velocity_field[:, -1, 0] = 0.0 * np.ones(next_velocity_field[:, -1, 0].shape)
    next_velocity_field[0, :, 0] = 0.0 * np.ones(next_velocity_field[0, :, 0].shape)
    next_velocity_field[-1, :, 0] = 1.0 * np.ones(next_velocity_field[-1, :, 0].shape)

    next_velocity_field[:, 0, 1] = 0.0 * np.ones(next_velocity_field[:, 0, 1].shape)
    next_velocity_field[:, -1, 1] = 0.0 * np.ones(next_velocity_field[:, -1, 1].shape)
    next_velocity_field[0, :, 1] = 0.0 * np.ones(next_velocity_field[0, :, 1].shape)
    next_velocity_field[-1, :, 1] = 0.0 * np.ones(next_velocity_field[-1, :, 1].shape)

    return next_velocity_field


def apply_boundary_conditions_for_pressure_field(pressure_field):
    next_pressure_field = pressure_field

    next_pressure_field[:, 0] = 1.0 * np.ones(next_pressure_field[:, 0].shape)
    next_pressure_field[:, -1] = 1.0 * np.ones(next_pressure_field[:, -1].shape)
    next_pressure_field[0, :] = 1.0 * np.ones(next_pressure_field[0, :].shape)
    next_pressure_field[-1, :] = 1.0 * np.ones(next_pressure_field[-1, :].shape)

    return next_pressure_field

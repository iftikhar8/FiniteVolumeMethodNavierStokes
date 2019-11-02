#
# Created by Brendan Berg on 01.11.2019
#

import numpy as np


def generate_cartesian_mesh_face_positions(x_min, x_max, x_count, y_min, y_max, y_count):
    faces_tmp_x = np.linspace(x_min, x_max, x_count + 1)
    faces_x = np.tile(faces_tmp_x, y_count).reshape(y_count, x_count + 1)

    faces_tmp_y = np.linspace(y_min, y_max, y_count + 1)
    faces_y = np.repeat(faces_tmp_y, x_count).reshape(y_count + 1, x_count)

    return faces_x, faces_y


def centroids_from_face_positions(faces_x, faces_y):
    centroids_x = 0.5 * (faces_x[:, 1:] + faces_x[:, 0:-1])
    centroids_y = 0.5 * (faces_y[1:, :] + faces_y[0:-1, :])
    return centroids_x, centroids_y


def cell_sizes_from_face_positions(faces_x, faces_y):
    cell_size_x = faces_x[:, 1:] - faces_x[:, 0:-1]
    cell_size_y = faces_y[1:, :] - faces_y[0:-1, :]
    return cell_size_x, cell_size_y


def face_area_from_cell_sizes(cell_sizes_x, cell_sizes_y, mesh_depth):
    face_areas_tmp_x = mesh_depth * cell_sizes_x
    face_areas_x = np.hstack([face_areas_tmp_x, face_areas_tmp_x[:, -1].reshape(face_areas_tmp_x.shape[0], 1)])

    face_areas_tmp_y = mesh_depth * cell_sizes_y
    face_areas_y = np.vstack([face_areas_tmp_y, face_areas_tmp_y[-1, :]])

    return face_areas_x, face_areas_y


def cell_volumes_from_cell_sizes(cell_sizes_x, cell_sizes_y, mesh_depth):
    return mesh_depth * np.multiply(cell_sizes_x, cell_sizes_y)

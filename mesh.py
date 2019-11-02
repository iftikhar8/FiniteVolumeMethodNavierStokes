#
# Created by Brendan Berg on 01.11.2019
#

import numpy as np


class MeshGeometry(object):
    def __init__(self, mesh_cells_x, mesh_cells_y, mesh_size_x, mesh_size_y, mesh_depth):
        self.mesh_cells_x = mesh_cells_x
        self.mesh_cells_y = mesh_cells_y
        self.mesh_size_x = mesh_size_x
        self.mesh_size_y = mesh_size_y
        self.mesh_depth = mesh_depth

        self.faces_x, self.faces_y = self.__generate_cartesian_mesh_face_positions()
        self.centroids_x, self.centroids_y = self.__centroids_from_face_positions()
        self.cell_sizes_x, self.cell_sizes_y = self.__cell_sizes_from_face_positions()
        self.face_areas_x, self.face_areas_y = self.__face_areas_from_cell_sizes()
        self.cell_volumes = self.__cell_volumes_from_cell_sizes()

    def cell_to_index(self, j, i):
        return self.mesh_cells_x * j + i

    def __generate_cartesian_mesh_face_positions(self):
        faces_tmp_x = np.linspace(0.0, self.mesh_size_x, self.mesh_cells_x + 1)
        faces_x = np.tile(faces_tmp_x, self.mesh_cells_y).reshape(self.mesh_cells_y, self.mesh_cells_x + 1)

        faces_tmp_y = np.linspace(0.0, self.mesh_size_y, self.mesh_cells_y + 1)
        faces_y = np.repeat(faces_tmp_y, self.mesh_cells_x).reshape(self.mesh_cells_y + 1, self.mesh_cells_x)

        return faces_x, faces_y

    def __centroids_from_face_positions(self):
        centroids_x = 0.5 * (self.faces_x[:, 1:] + self.faces_x[:, 0:-1])
        centroids_y = 0.5 * (self.faces_y[1:, :] + self.faces_y[0:-1, :])
        return centroids_x, centroids_y

    def __cell_sizes_from_face_positions(self):
        cell_sizes_x = self.faces_x[:, 1:] - self.faces_x[:, 0:-1]
        cell_sizes_y = self.faces_y[1:, :] - self.faces_y[0:-1, :]
        return cell_sizes_x, cell_sizes_y

    def __face_areas_from_cell_sizes(self):
        face_areas_tmp_x = self.mesh_depth * self.cell_sizes_x
        face_areas_x = np.hstack([face_areas_tmp_x, face_areas_tmp_x[:, -1].reshape(face_areas_tmp_x.shape[0], 1)])

        face_areas_tmp_y = self.mesh_depth * self.cell_sizes_y
        face_areas_y = np.vstack([face_areas_tmp_y, face_areas_tmp_y[-1, :]])

        return face_areas_x, face_areas_y

    def __cell_volumes_from_cell_sizes(self):
        return self.mesh_depth * np.multiply(self.cell_sizes_x, self.cell_sizes_y)

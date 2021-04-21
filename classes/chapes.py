import pyrr
from OpenGL.GL import *
import numpy as np
from utils.TextureLoader import load_texture

class Cube:
    def __init__(self, pModel_loc):
        cube_vertices = [-0.5, -0.5, 0.5, 0.0, 0.0,
                         0.5, -0.5, 0.5, 1.0, 0.0,
                         0.5, 0.5, 0.5, 1.0, 1.0,
                         -0.5, 0.5, 0.5, 0.0, 1.0,

                         -0.5, -0.5, -0.5, 0.0, 0.0,
                         0.5, -0.5, -0.5, 1.0, 0.0,
                         0.5, 0.5, -0.5, 1.0, 1.0,
                         -0.5, 0.5, -0.5, 0.0, 1.0,

                         0.5, -0.5, -0.5, 0.0, 0.0,
                         0.5, 0.5, -0.5, 1.0, 0.0,
                         0.5, 0.5, 0.5, 1.0, 1.0,
                         0.5, -0.5, 0.5, 0.0, 1.0,

                         -0.5, 0.5, -0.5, 0.0, 0.0,
                         -0.5, -0.5, -0.5, 1.0, 0.0,
                         -0.5, -0.5, 0.5, 1.0, 1.0,
                         -0.5, 0.5, 0.5, 0.0, 1.0,

                         -0.5, -0.5, -0.5, 0.0, 0.0,
                         0.5, -0.5, -0.5, 1.0, 0.0,
                         0.5, -0.5, 0.5, 1.0, 1.0,
                         -0.5, -0.5, 0.5, 0.0, 1.0,

                         0.5, 0.5, -0.5, 0.0, 0.0,
                         -0.5, 0.5, -0.5, 1.0, 0.0,
                         -0.5, 0.5, 0.5, 1.0, 1.0,
                         0.5, 0.5, 0.5, 0.0, 1.0]

        cube_indices = [ 0, 1, 2, 2, 3, 0,
                         4, 5, 6, 6, 7, 4,
                         8, 9, 10, 10, 11, 8,
                         12, 13, 14, 14, 15, 12,
                         16, 17, 18, 18, 19, 16,
                         20, 21, 22, 22, 23, 20]

        self.vertices = np.array(cube_vertices, dtype=np.float32)
        self.indices  = np.array(cube_indices, dtype=np.uint32)

        self.__VAO = glGenVertexArrays(1)
        self.__VBO = glGenBuffers(1)
        self.__EBO = glGenBuffers(1)

        # Cube VAO
        glBindVertexArray(self.__VAO)
        # Cube Vertex Buffer Object
        glBindBuffer(GL_ARRAY_BUFFER, self.__VBO)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)

        # Cube Element Buffer Object
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.__EBO)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.indices.nbytes, self.indices, GL_STATIC_DRAW)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, self.vertices.itemsize * 5, ctypes.c_void_p(0))

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, self.vertices.itemsize * 5, ctypes.c_void_p(12))

        self.__texture   = glGenTextures(1)
        load_texture("textures/crate.jpg", self.__texture)

        self.position    = pyrr.matrix44.create_from_translation(pyrr.Vector3([-1, 0, 0]))
        self.__model_loc = pModel_loc

    def draw(self):
        glBindVertexArray(self.__VAO)
        glBindTexture(GL_TEXTURE_2D, self.__texture)
        glUniformMatrix4fv(self.__model_loc, 1, GL_FALSE, self.position)
        glDrawElements(GL_TRIANGLES, len(self.indices), GL_UNSIGNED_INT, None)

class Quad:
    def __init__(self, pModel_loc):
        self.quad_vertices = [-0.5, -0.5, 0, 0.0, 0.0,
                               0.5, -0.5, 0, 1.0, 0.0,
                               0.5, 0.5, 0, 1.0, 1.0,
                              -0.5, 0.5, 0, 0.0, 1.0]

        self.quad_indices = [0, 1, 2, 2, 3, 0]
        self.vertices     = np.array(self.quad_vertices, dtype=np.float32)
        self.indices      = np.array(self.quad_indices, dtype=np.uint32)

        self.__VAO = glGenVertexArrays(1)
        self.__VBO = glGenBuffers(1)
        self.__EBO = glGenBuffers(1)

         # Quad VAO
        glBindVertexArray(self.__VAO)
        # Quad Vertex Buffer Object
        glBindBuffer(GL_ARRAY_BUFFER, self.__VBO)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)

        # Quad Element Buffer Object
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.__EBO)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.indices.nbytes, self.indices, GL_STATIC_DRAW)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, self.vertices.itemsize * 5, ctypes.c_void_p(0))

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, self.vertices.itemsize * 5, ctypes.c_void_p(12))

        self.__texture   = glGenTextures(1)
        load_texture("textures/window.webp", self.__texture)

        self.position    = pyrr.matrix44.create_from_translation(pyrr.Vector3([1, 0, 0]))
        self.__model_loc = pModel_loc

    def draw(self):
        glBindVertexArray(self.__VAO)
        glBindTexture(GL_TEXTURE_2D, self.__texture)
        glUniformMatrix4fv(self.__model_loc, 1, GL_FALSE, self.position)
        glDrawElements(GL_TRIANGLES, len(self.indices), GL_UNSIGNED_INT, None)

class Triangle:
    def __init__(self, pModel_loc, pSwitcher_loc):
        self.triangle_vertices = [-0.5, -0.5, 0, 1, 0, 0,
                                   0.5, -0.5, 0, 0, 1, 0,
                                   0.0, 0.5, 0, 0, 0, 1]

        self.vertices = np.array(self.triangle_vertices, dtype=np.float32)

        self.__VAO = glGenVertexArrays(1)
        self.__VBO = glGenBuffers(1)

        # Triangle VAO
        glBindVertexArray(self.__VAO)
        # Triangle Vertex Buffer Object
        glBindBuffer(GL_ARRAY_BUFFER, self.__VBO)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, self.vertices.itemsize * 6, ctypes.c_void_p(0))

        glEnableVertexAttribArray(2)
        glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, self.vertices.itemsize * 6, ctypes.c_void_p(12))

        self.position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, 1, 0]))
        self.__model_loc = pModel_loc
        self.__switcher_loc = pSwitcher_loc

    def draw(self):
        glUniform1i(self.__switcher_loc, 1)
        glBindVertexArray(self.__VAO)
        glUniformMatrix4fv(self.__model_loc, 1, GL_FALSE, self.position)
        glDrawArrays(GL_TRIANGLES, 0, 3)


import pyrr
from OpenGL.GL import *
import numpy as np
from utils.TextureLoader import load_texture

class ShapeBase:
    def __init__(self, pModel_loc):
        self.vertices = None
        self.indices = None

        self._VAO = glGenVertexArrays(1)
        self._VBO = glGenBuffers(1)
        self._EBO = glGenBuffers(1)

        self._model_loc = pModel_loc
        self._position  = None
        self._texture   = glGenTextures(1)

    def _handleObject(self, vertices, indices):
        self.vertices = np.array(vertices, dtype=np.float32)
        self.indices  = np.array(indices, dtype=np.uint32)

        # VAO
        glBindVertexArray(self._VAO)
        # Vertex Buffer Object
        glBindBuffer(GL_ARRAY_BUFFER, self._VBO)
        glBufferData(GL_ARRAY_BUFFER, self._getVertices().nbytes, self._getVertices(), GL_STATIC_DRAW)

        # Element Buffer Object
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self._getEBO())
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self._getIndices().nbytes, self._getIndices(), GL_STATIC_DRAW)

    def draw(self):
        glBindVertexArray(self._VAO)
        glBindTexture(GL_TEXTURE_2D, self._texture)
        glUniformMatrix4fv(self._model_loc, 1, GL_FALSE, self._position)
        glDrawElements(GL_TRIANGLES, len(self.indices), GL_UNSIGNED_INT, None)

    def _setPosition(self, position):
        self._position = position

    def _getPosition(self):
        return self._position

    def _getModel_loc(self):
        return self._model_loc

    def _getVAO(self):
        return self._VAO

    def _getVBO(self):
        return self._VBO

    def _getEBO(self):
        return self._EBO

    def _getVertices(self):
        return self.vertices

    def _getIndices(self):
        return self.indices

    def _getTexture(self):
        return self._texture

class Cube(ShapeBase):
    def __init__(self, pModel_loc):
        super().__init__(pModel_loc)
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

        super()._handleObject(cube_vertices, cube_indices)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, super()._getVertices().itemsize * 5, ctypes.c_void_p(0))

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, super()._getVertices().itemsize * 5, ctypes.c_void_p(12))

        load_texture("textures/crate.jpg", super()._getTexture())

        super()._setPosition(pyrr.matrix44.create_from_translation(pyrr.Vector3([-1, 0, 0])))

class Quad(ShapeBase):
    def __init__(self, pModel_loc):
        super().__init__(pModel_loc)
        quad_vertices = [-0.5, -0.5, 0, 0.0, 0.0,
                          0.5, -0.5, 0, 1.0, 0.0,
                          0.5, 0.5, 0, 1.0, 1.0,
                         -0.5, 0.5, 0, 0.0, 1.0]

        quad_indices = [0, 1, 2, 2, 3, 0]
        super()._handleObject(quad_vertices, quad_indices)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, self.vertices.itemsize * 5, ctypes.c_void_p(0))

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, self.vertices.itemsize * 5, ctypes.c_void_p(12))

        load_texture("textures/window.webp", super()._getTexture())

        super()._setPosition(pyrr.matrix44.create_from_translation(pyrr.Vector3([1, 0, 0])))

class Triangle(ShapeBase):
    def __init__(self, pModel_loc, pSwitcher_loc):
        super().__init__(pModel_loc)
        triangle_vertices = [-0.5, -0.5, 0, 1, 0, 0,
                              0.5, -0.5, 0, 0, 1, 0,
                              0.0, 0.5, 0, 0, 0, 1]

        super()._handleObject(triangle_vertices, [])

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, self.vertices.itemsize * 6, ctypes.c_void_p(0))

        glEnableVertexAttribArray(2)
        glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, self.vertices.itemsize * 6, ctypes.c_void_p(12))

        super()._setPosition(pyrr.matrix44.create_from_translation(pyrr.Vector3([0, 1, 0])))
        self.__switcher_loc = pSwitcher_loc

    # override
    def draw(self):
        glUniform1i(self.__switcher_loc, 1)
        glBindVertexArray(super()._getVAO())
        glUniformMatrix4fv(super()._getModel_loc(), 1, GL_FALSE, super()._getPosition())
        glDrawArrays(GL_TRIANGLES, 0, 3)


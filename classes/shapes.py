import pyrr
from OpenGL.GL import *
import numpy as np
from utils.TextureLoader import load_texture

class ShapeBase:
    def __init__(self, pModel_loc, pSwitcher_loc, pCordinates):
        self.vertices = None
        self.indices = None

        self._VAO = glGenVertexArrays(1)
        self._VBO = glGenBuffers(1)
        self._EBO = glGenBuffers(1)

        self._model_loc    = pModel_loc
        self._switcher_loc = pSwitcher_loc
        self._position     = None
        self._texture      = glGenTextures(1)

        self._setPosition(pCordinates)

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
        self._position = pyrr.matrix44.create_from_translation(pyrr.Vector3(position))

    def _getPosition(self):
        return self._position

    def _getModel_loc(self):
        return self._model_loc

    def _getSwitcher_loc(self):
        return self._switcher_loc

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
    def __init__(self, pModel_loc, pSwitcher_loc, pCordinates):
        super().__init__(pModel_loc, pSwitcher_loc, pCordinates)
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
    def __init__(self, pModel_loc, pSwitcher_loc, pCordinates):
        super().__init__(pModel_loc, pSwitcher_loc, pCordinates)
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
    def __init__(self, pModel_loc, pSwitcher_loc, pCordinates):
        super().__init__(pModel_loc, pSwitcher_loc, pCordinates)
        triangle_vertices = [-0.5, -0.5, 0, 1, 0, 0,
                              0.5, -0.5, 0, 0, 1, 0,
                              0.0, 0.5, 0, 0, 0, 1]

        super()._handleObject(triangle_vertices, [])

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, self.vertices.itemsize * 6, ctypes.c_void_p(0))

        glEnableVertexAttribArray(2)
        glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, self.vertices.itemsize * 6, ctypes.c_void_p(12))

        super()._setPosition(pyrr.matrix44.create_from_translation(pyrr.Vector3([0, 1, 0])))

    # override
    def draw(self):
        glUniform1i(super()._getSwitcher_loc(), 1)
        glBindVertexArray(super()._getVAO())
        glUniformMatrix4fv(super()._getModel_loc(), 1, GL_FALSE, super()._getPosition())
        glDrawArrays(GL_TRIANGLES, 0, 3)

class Roof1(ShapeBase):
    def __init__(self, pModel_loc, pSwitcher_loc, pCordinates):
        super().__init__(pModel_loc, pSwitcher_loc, pCordinates)
        vertices = [-0.8, -0.5, 0.0, 54/255, 119/255, 31/255,
                    0.5, -0.5, 0.0, 54/255, 119/255, 31/255,
                    -0.15,  0.1, 0.0, 54/255, 119/255, 31/255]

        super()._handleObject(vertices, [])

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, self.vertices.itemsize * 6, ctypes.c_void_p(0))

        glEnableVertexAttribArray(2)
        glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, self.vertices.itemsize * 6, ctypes.c_void_p(12))

    # override
    def draw(self):
        glUniform1i(super()._getSwitcher_loc(), 1)
        glBindVertexArray(super()._getVAO())
        glUniformMatrix4fv(super()._getModel_loc(), 1, GL_FALSE, super()._getPosition())
        glDrawArrays(GL_TRIANGLES, 0, 3)

class Roof2(ShapeBase):
    def __init__(self, pModel_loc, pSwitcher_loc, pCordinates):
        super().__init__(pModel_loc, pSwitcher_loc, pCordinates)
        vertices = [-0.5, -0.5, 0.0, 90/255, 138/255, 207/255,
                     2, -0.5, 0.0, 90/255, 138/255, 207/255,
                    -1.15,  0.1, 0.0, 90/255, 138/255, 207/255,
                     1.5,  0.1, 0.0, 90/255, 138/255, 207/255]

        super()._handleObject(vertices, [])

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, self.vertices.itemsize * 6, ctypes.c_void_p(0))

        glEnableVertexAttribArray(2)
        glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, self.vertices.itemsize * 6, ctypes.c_void_p(12))

    # override
    def draw(self):
        glUniform1i(super()._getSwitcher_loc(), 1)
        glBindVertexArray(super()._getVAO())
        glUniformMatrix4fv(super()._getModel_loc(), 1, GL_FALSE, super()._getPosition())
        glDrawArrays(GL_TRIANGLE_STRIP, 0, 4)

class Wall1(ShapeBase):
    def __init__(self, pModel_loc, pSwitcher_loc, pCordinates):
        super().__init__(pModel_loc, pSwitcher_loc, pCordinates)
        vertices = [-0.8, -0.5, 0.0, 182/255, 81/255, 87/255,
                     0.5, -0.5, 0.0, 182/255, 81/255, 87/255,
                    -0.8,  0.5, 0.0, 182/255, 81/255, 87/255,
                     0.5,  0.5, 0.0, 182/255, 81/255, 87/255]

        super()._handleObject(vertices, [])

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))

        glEnableVertexAttribArray(2)
        glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))

    # override
    def draw(self):
        glUniform1i(super()._getSwitcher_loc(), 1)
        glBindVertexArray(super()._getVAO())
        glUniformMatrix4fv(super()._getModel_loc(), 1, GL_FALSE, super()._getPosition())
        glDrawArrays(GL_TRIANGLE_STRIP, 0, 4)

class Wall2(ShapeBase):
    def __init__(self, pModel_loc, pSwitcher_loc, pCordinates):
        super().__init__(pModel_loc, pSwitcher_loc, pCordinates)
        vertices = [-0.5, -0.5, 0.0, 31/255, 58/255, 84/255,
                     2, -0.5, 0.0, 31/255, 58/255, 84/255,
                    -0.5,  0.5, 0.0, 31/255, 58/255, 84/255,
                     2,  0.5, 0.0, 31/255, 58/255, 84/255]

        super()._handleObject(vertices, [])

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))

        glEnableVertexAttribArray(2)
        glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))

    # override
    def draw(self):
        glUniform1i(super()._getSwitcher_loc(), 1)
        glBindVertexArray(super()._getVAO())
        glUniformMatrix4fv(super()._getModel_loc(), 1, GL_FALSE, super()._getPosition())
        glDrawArrays(GL_TRIANGLE_STRIP, 0, 4)

class Door(ShapeBase):
    def __init__(self, pModel_loc, pSwitcher_loc, pCordinates):
        super().__init__(pModel_loc, pSwitcher_loc, pCordinates)
        vertices = [-0.2, -0.5, 0.0, 168/255, 87/255, 215/255,
                     0.2, -0.5, 0.0, 168/255, 87/255, 215/255,
                    -0.2,  0.2, 0.0, 168/255, 87/255, 215/255,
                     0.2,  0.2, 0.0, 168/255, 87/255, 215/255]

        super()._handleObject(vertices, [])

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))

        glEnableVertexAttribArray(2)
        glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))

    def draw(self):
        glUniform1i(super()._getSwitcher_loc(), 1)
        glBindVertexArray(super()._getVAO())
        glUniformMatrix4fv(super()._getModel_loc(), 1, GL_FALSE, super()._getPosition())
        glDrawArrays(GL_TRIANGLE_STRIP, 0, 4)

class DoorHandle(ShapeBase):
    def __init__(self, pModel_loc, pSwitcher_loc, pCordinates):
        super().__init__(pModel_loc, pSwitcher_loc, pCordinates)
        vertices = [-0.03, -0.03, 0.0, 93/255, 162/255, 204/255,
                     0.03, -0.03, 0.0, 93/255, 162/255, 204/255,
                    -0.03,  0.03, 0.0, 93/255, 162/255, 204/255,
                     0.03,  0.03, 0.0, 93/255, 162/255, 204/255]

        super()._handleObject(vertices, [])

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))

        glEnableVertexAttribArray(2)
        glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))

    def draw(self):
        glUniform1i(super()._getSwitcher_loc(), 1)
        glBindVertexArray(super()._getVAO())
        glUniformMatrix4fv(super()._getModel_loc(), 1, GL_FALSE, super()._getPosition())
        glDrawArrays(GL_TRIANGLE_STRIP, 0, 4)

class Path(ShapeBase):
    def __init__(self, pModel_loc, pSwitcher_loc, pCordinates):
        super().__init__(pModel_loc, pSwitcher_loc, pCordinates)
        vertices = [-0.6, -0.6, 0.0, 71/255, 106/255, 143/255,
                     0, -0.6, 0.0, 71/255, 106/255, 143/255,
                    -0.2,  0.2, 0.0, 71/255, 106/255, 143/255,
                     0.2,  0.2, 0.0, 71/255, 106/255, 143/255]

        super()._handleObject(vertices, [])

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))

        glEnableVertexAttribArray(2)
        glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))

    def draw(self):
        glUniform1i(super()._getSwitcher_loc(), 1)
        glBindVertexArray(super()._getVAO())
        glUniformMatrix4fv(super()._getModel_loc(), 1, GL_FALSE, super()._getPosition())
        glDrawArrays(GL_TRIANGLE_STRIP, 0, 4)

class Window1(ShapeBase):
    def __init__(self, pModel_loc, pSwitcher_loc, pCordinates):
        super().__init__(pModel_loc, pSwitcher_loc, pCordinates)
        quad_vertices = [-0.2, -0.1, 0, 0.0, 0.0,
                          0.4, -0.1, 0, 1.0, 0.0,
                          0.4, 0.3, 0, 1.0, 1.0,
                         -0.2, 0.3, 0, 0.0, 1.0]

        quad_indices = [0, 1, 2, 2, 3, 0]
        super()._handleObject(quad_vertices, quad_indices)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, self.vertices.itemsize * 5, ctypes.c_void_p(0))

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, self.vertices.itemsize * 5, ctypes.c_void_p(12))

        load_texture("textures/window.webp", super()._getTexture())

class Window2(ShapeBase):
    def __init__(self, pModel_loc, pSwitcher_loc, pCordinates):
        super().__init__(pModel_loc, pSwitcher_loc, pCordinates)
        quad_vertices = [-0.2, -0.1, 0, 0.0, 0.0,
                          0.4, -0.1, 0, 1.0, 0.0,
                          0.4, 0.3, 0, 1.0, 1.0,
                         -0.2, 0.3, 0, 0.0, 1.0]

        quad_indices = [0, 1, 2, 2, 3, 0]
        super()._handleObject(quad_vertices, quad_indices)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, self.vertices.itemsize * 5, ctypes.c_void_p(0))

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, self.vertices.itemsize * 5, ctypes.c_void_p(12))

        load_texture("textures/window.webp", super()._getTexture())
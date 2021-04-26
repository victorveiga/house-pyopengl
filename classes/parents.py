import pyrr
from OpenGL.GL import *
import numpy as np
from utils.TextureLoader import load_texture

class DayNightTimeBase:
    pass

class DaytimeBase:
    pass

class NighttimeBase:
    pass

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
        self._defaultShape = GL_TRIANGLE_STRIP

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

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, self.vertices.itemsize * 6, ctypes.c_void_p(0))

        glEnableVertexAttribArray(2)
        glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, self.vertices.itemsize * 6, ctypes.c_void_p(12))

    def draw(self):
        glUniform1i(self._getSwitcher_loc(), 1)
        glBindVertexArray(self._getVAO())
        glUniformMatrix4fv(self._getModel_loc(), 1, GL_FALSE, self._getPosition())
        glDrawArrays(self._getDefaultShape(), 0, int(self._getVertices().size / 6))

    def _setPosition(self, position):
        self._position = pyrr.matrix44.create_from_translation(pyrr.Vector3(position))

    def _setModel_loc(self, model_loc):
        self._model_loc = model_loc

    def _setSwitcher_loc(self, switcher_loc):
        self._switcher_loc = switcher_loc

    def _getPosition(self):
        return self._position

    def _setDefaultShape(self, shape):
        self._defaultShape = shape

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

    def _getDefaultShape(self):
        return self._defaultShape

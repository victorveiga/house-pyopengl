import pyrr
from OpenGL.GL import *
import numpy as np
from utils.TextureLoader import load_texture

class DayNightTimeBase:
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

class Roof1(ShapeBase):
    def __init__(self, pModel_loc, pSwitcher_loc, pCordinates):
        super().__init__(pModel_loc, pSwitcher_loc, pCordinates)
        color    = [54/255, 119/255, 31/255]
        vertices = [-0.8, -0.5, 0.0, *color,
                    0.5, -0.5, 0.0, *color,
                    -0.15,  0.1, 0.0, *color]

        super()._handleObject(vertices, [])
        super()._setDefaultShape(GL_TRIANGLES)
        

class Roof2(ShapeBase):
    def __init__(self, pModel_loc, pSwitcher_loc, pCordinates):
        super().__init__(pModel_loc, pSwitcher_loc, pCordinates)
        color    = [90/255, 138/255, 207/255]
        vertices = [-0.5, -0.5, 0.0, *color,
                     2, -0.5, 0.0, *color,
                    -1.15,  0.1, 0.0, *color,
                     1.5,  0.1, 0.0, *color]

        super()._handleObject(vertices, [])

class Wall1(ShapeBase):
    def __init__(self, pModel_loc, pSwitcher_loc, pCordinates):
        super().__init__(pModel_loc, pSwitcher_loc, pCordinates)
        color    = [182/255, 81/255, 87/255]
        vertices = [-0.8, -0.5, 0.0, *color,
                     0.5, -0.5, 0.0, *color,
                    -0.8,  0.5, 0.0, *color,
                     0.5,  0.5, 0.0, *color]

        super()._handleObject(vertices, [])

class Wall2(ShapeBase):
    def __init__(self, pModel_loc, pSwitcher_loc, pCordinates):
        super().__init__(pModel_loc, pSwitcher_loc, pCordinates)
        color    = [31/255, 58/255, 84/255]
        vertices = [-0.5, -0.5, 0.0, *color,
                     2, -0.5, 0.0, *color,
                    -0.5,  0.5, 0.0, *color,
                     2,  0.5, 0.0, *color]

        super()._handleObject(vertices, [])

class Door(ShapeBase):
    def __init__(self, pModel_loc, pSwitcher_loc, pCordinates):
        super().__init__(pModel_loc, pSwitcher_loc, pCordinates)
        color    = [168/255, 87/255, 215/255]
        vertices = [-0.2, -0.5, 0.0, *color,
                     0.2, -0.5, 0.0, *color,
                    -0.2,  0.2, 0.0, *color,
                     0.2,  0.2, 0.0, *color]

        super()._handleObject(vertices, [])

class DoorHandle(ShapeBase):
    def __init__(self, pModel_loc, pSwitcher_loc, pCordinates):
        super().__init__(pModel_loc, pSwitcher_loc, pCordinates)
        color    = [93/255, 162/255, 204/255]
        vertices = [-0.03, -0.03, 0.0, *color,
                     0.03, -0.03, 0.0, *color,
                    -0.03,  0.03, 0.0, *color,
                     0.03,  0.03, 0.0, *color]

        super()._handleObject(vertices, [])

class Path(ShapeBase):
    def __init__(self, pModel_loc, pSwitcher_loc, pCordinates):
        super().__init__(pModel_loc, pSwitcher_loc, pCordinates)
        color    = [71/255, 106/255, 143/255]
        vertices = [-0.6, -0.6, 0.0, *color,
                     0, -0.6, 0.0, *color,
                    -0.2,  0.2, 0.0, *color,
                     0.2,  0.2, 0.0, *color]

        super()._handleObject(vertices, [])

class WindowObj(ShapeBase):
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

    def draw(self):
        glBindVertexArray(self._VAO)
        glBindTexture(GL_TEXTURE_2D, self._texture)
        glUniformMatrix4fv(self._model_loc, 1, GL_FALSE, self._position)
        glDrawElements(GL_TRIANGLES, len(self.indices), GL_UNSIGNED_INT, None)

class Garden(ShapeBase, DayNightTimeBase):
    def __init__(self, pModel_loc, pSwitcher_loc, pCordinates):
        self.__Daytime = True
        super().__init__(pModel_loc, pSwitcher_loc, pCordinates)
        super()._handleObject(self._getCustomVertices(), [])

    def _getCustomVertices(self):
        if self.__Daytime == True:
            color = [150/255, 213/255, 120/255] # green
        else:
            color = [61/255, 175/255, 44/255] # midnight green
        
        return [-2, -1, 0.0, *color,
                 5.0, -1, 0.0, *color,
                -2,  0.0, 0.0, *color,
                 5.0,  0.0, 0.0, *color]

    def setDaytime(self, Daytime: bool):
        self.__Daytime = Daytime
        super()._handleObject(self._getCustomVertices(), [])

class Sky(ShapeBase, DayNightTimeBase):
    def __init__(self, pModel_loc, pSwitcher_loc, pCordinates):
        self.__Daytime = True
        super().__init__(pModel_loc, pSwitcher_loc, pCordinates)
        super()._handleObject(self._getCustomVertices(), [])

    def _getCustomVertices(self):
        if self.__Daytime == True:
            color = [173/255, 203/255, 227/255] # blue
        else:
            color = [0/255, 3/255, 22/255] # midnight blue

        return [-2.0, -1, 0.0, *color,
                 5.0, -1, 0.0, *color,
                -2.0,  1, 0.0, *color,
                 5.0,  1, 0.0, *color]

    def setDaytime(self, Daytime: bool):
        self.__Daytime = Daytime
        super()._handleObject(self._getCustomVertices(), [])
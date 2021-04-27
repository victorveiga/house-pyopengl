from OpenGL.GL import *
from utils.TextureLoader import load_texture
from .parents import ShapeBase, DayNightTimeBase, DaytimeBase, NighttimeBase
import numpy as np

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

class Sun(DaytimeBase):
    pass

class Cloud(DaytimeBase):
    pass

class Star(ShapeBase, NighttimeBase):
    def __init__(self, pModel_loc, pSwitcher_loc, pCordinates):
        super().__init__(pModel_loc, pSwitcher_loc, pCordinates)
        color    = [1,1,1]
        vertices = [-0.60, 0.77, 0, *color,
                    -0.68, 0.77, 0, *color,
                    -0.70, 0.68, 0, *color,
                    -0.64, 0.63, 0, *color,
                    -0.58, 0.68, 0, *color ]

        super()._handleObject(vertices, [])
        super()._setDefaultShape(GL_POLYGON)

class Moon(ShapeBase, NighttimeBase):
    def __init__(self, pModel_loc, pSwitcher_loc, pCordinates):
        super().__init__(pModel_loc, pSwitcher_loc, pCordinates)
        quad_vertices = [-0.5, -0.5,  0.5, 0.0, 0.0,
                          0.5, -0.5,  0.5, 1.0, 0.0,
                          0.5,  0.5,  0.5, 1.0, 1.0,
                         -0.5,  0.5,  0.5, 0.0, 1.0,]

        quad_indices = [0, 1, 2, 2, 3, 0]
        super()._handleObject(quad_vertices, quad_indices)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, self.vertices.itemsize * 5, ctypes.c_void_p(0))

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, self.vertices.itemsize * 5, ctypes.c_void_p(12))

        load_texture("textures/moon.png", super()._getTexture())

    def draw(self):
        glBindVertexArray(self._VAO)
        glBindTexture(GL_TEXTURE_2D, self._texture)
        glUniformMatrix4fv(self._model_loc, 1, GL_FALSE, self._position)
        glDrawElements(GL_TRIANGLES, len(self.indices), GL_UNSIGNED_INT, None)

class Cloud(ShapeBase, DaytimeBase):
    def __init__(self, pModel_loc, pSwitcher_loc, pCordinates):
        super().__init__(pModel_loc, pSwitcher_loc, pCordinates)
        quad_vertices = [-0.5, -0.5,  0.5, 0.0, 0.0,
                          1, -0.5,  0.5, 1.0, 0.0,
                          0.5,  0.5,  0.5, 1.0, 1.0,
                         -1,  0.5,  0.5, 0.0, 1.0,]

        quad_indices = [0, 1, 2, 2, 3, 0]
        super()._handleObject(quad_vertices, quad_indices)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, self.vertices.itemsize * 5, ctypes.c_void_p(0))

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, self.vertices.itemsize * 5, ctypes.c_void_p(12))

        load_texture("textures/cloud.png", super()._getTexture())

    def draw(self):
        glBindVertexArray(self._VAO)
        glBindTexture(GL_TEXTURE_2D, self._texture)
        glUniformMatrix4fv(self._model_loc, 1, GL_FALSE, self._position)
        glDrawElements(GL_TRIANGLES, len(self.indices), GL_UNSIGNED_INT, None)

class Sun(ShapeBase, DaytimeBase):
    def __init__(self, pModel_loc, pSwitcher_loc, pCordinates):
        super().__init__(pModel_loc, pSwitcher_loc, pCordinates)
        quad_vertices = [-0.5, -0.5,  0.5, 0.0, 0.0,
                          0.5, -0.5,  0.5, 1.0, 0.0,
                          0.5,  0.5,  0.5, 1.0, 1.0,
                         -0.5,  0.5,  0.5, 0.0, 1.0,]

        quad_indices = [0, 1, 2, 2, 3, 0]
        super()._handleObject(quad_vertices, quad_indices)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, self.vertices.itemsize * 5, ctypes.c_void_p(0))

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, self.vertices.itemsize * 5, ctypes.c_void_p(12))

        load_texture("textures/sun.png", super()._getTexture())

    def draw(self):
        glBindVertexArray(self._VAO)
        glBindTexture(GL_TEXTURE_2D, self._texture)
        glUniformMatrix4fv(self._model_loc, 1, GL_FALSE, self._position)
        glDrawElements(GL_TRIANGLES, len(self.indices), GL_UNSIGNED_INT, None)
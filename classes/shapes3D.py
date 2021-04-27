from OpenGL.GL import *
from .parents import ShapeBase, DayNightTimeBase

class Cube(ShapeBase):
    def __init__(self, pModel_loc, pSwitcher_loc, pCordinates):
        super().__init__(pModel_loc, pSwitcher_loc, pCordinates)
        color  = [1,1,1]
        color1 = [1/255, 31/255, 75/255]
        color2 = [3/255, 57/255, 108/255]
        color3 = [0/255, 91/255, 150/255]
        color4 = [100/255, 151/255, 177/255]
        cube_vertices = [-0.5, -0.5, 0.5, *color2,
                          0.5, -0.5, 0.5, *color2,
                          0.5,  0.5, 0.5, *color2,
                         -0.5,  0.5, 0.5, *color2,

                         -0.5, -0.5, -0.5, *color3,
                          0.5, -0.5, -0.5, *color3,
                          0.5,  0.5, -0.5, *color3,
                         -0.5,  0.5, -0.5, *color3]

        cube_indices = [0, 1, 2, 2, 3, 0,
                        4, 5, 6, 6, 7, 4,
                        4, 5, 1, 1, 0, 4,
                        6, 7, 3, 3, 2, 6,
                        5, 6, 2, 2, 1, 5,
                        7, 4, 0, 0, 3, 7]

        super()._handleObject(cube_vertices, cube_indices)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, super()._getVertices().itemsize * 6, ctypes.c_void_p(0))

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, super()._getVertices().itemsize * 6, ctypes.c_void_p(12))

    def draw(self):
        glUniform1i(self._getSwitcher_loc(), 1)
        glBindVertexArray(self._VAO)
        glBindTexture(GL_TEXTURE_2D, self._texture)
        glUniformMatrix4fv(self._model_loc, 1, GL_FALSE, self._position)
        glDrawElements(GL_TRIANGLES, len(self.indices), GL_UNSIGNED_INT, None)

class Roof(ShapeBase):
    def __init__(self, pModel_loc, pSwitcher_loc, pCordinates):
        super().__init__(pModel_loc, pSwitcher_loc, pCordinates)
        color  = [1,1,1]
        color1 = [254/255, 156/255, 143/255]
        color2 = [54/255, 119/255, 31/255]
        color3 = [254/255, 156/255, 143/255]
        color4 = [254/255, 156/255, 143/255]
        cube_vertices = [-0.8, -0.5, 0.5, *color2,
                          0.5, -0.5, 0.5, *color2,
                         -0.15,  0.1, 0.5, *color2,
                         
                         -0.8, -0.5, -0.5, *color2,
                          0.5, -0.5, -0.5, *color2,
                         -0.15,  0.1, -0.5, *color2]

        cube_indices = [0, 1, 2, 2, 3, 0,
                        4, 5, 6, 6, 7, 4,
                        4, 5, 1, 1, 0, 4,
                        6, 7, 3, 3, 2, 6,
                        5, 6, 2, 2, 1, 5,
                        7, 4, 0, 0, 3, 7]

        super()._handleObject(cube_vertices, cube_indices)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, super()._getVertices().itemsize * 6, ctypes.c_void_p(0))

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, super()._getVertices().itemsize * 6, ctypes.c_void_p(12))

    def draw(self):
        glUniform1i(self._getSwitcher_loc(), 1)
        glBindVertexArray(self._VAO)
        glBindTexture(GL_TEXTURE_2D, self._texture)
        glUniformMatrix4fv(self._model_loc, 1, GL_FALSE, self._position)
        glDrawElements(GL_TRIANGLES, len(self.indices), GL_UNSIGNED_INT, None)
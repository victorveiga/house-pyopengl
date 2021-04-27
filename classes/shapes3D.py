from OpenGL.GL import *
from .parents import ShapeBase, DayNightTimeBase, UseColorType
    
class Cube(ShapeBase, UseColorType):
    def __init__(self, pModel_loc=None, pSwitcher_loc=None, pCordinates=None, pColor_loc=None):
        super().__init__(pModel_loc, pSwitcher_loc, pCordinates)
        vertices   = [ -0.5, -0.5,  0.5, 0.0, 0.0,
                        0.5, -0.5,  0.5, 1.0, 0.0,
                        0.5,  0.5,  0.5, 1.0, 1.0,
                       -0.5,  0.5,  0.5, 0.0, 1.0,

                       -0.5, -0.5, -0.5, 0.0, 0.0,
                        0.5, -0.5, -0.5, 1.0, 0.0,
                        0.5,  0.5, -0.5, 1.0, 1.0,
                       -0.5,  0.5, -0.5, 0.0, 1.0,

                       0.5, -0.5, -0.5, 0.0, 0.0,
                       0.5,  0.5, -0.5, 1.0, 0.0,
                       0.5,  0.5,  0.5, 1.0, 1.0,
                       0.5, -0.5,  0.5, 0.0, 1.0,

                       -0.5,  0.5, -0.5, 0.0, 0.0,
                       -0.5, -0.5, -0.5, 1.0, 0.0,
                       -0.5, -0.5,  0.5, 1.0, 1.0,
                       -0.5,  0.5,  0.5, 0.0, 1.0,

                       -0.5, -0.5, -0.5, 0.0, 0.0,
                        0.5, -0.5, -0.5, 1.0, 0.0,
                        0.5, -0.5,  0.5, 1.0, 1.0,
                       -0.5, -0.5,  0.5, 0.0, 1.0,

                       0.5,  0.5, -0.5, 0.0, 0.0,
                       -0.5,  0.5, -0.5, 1.0, 0.0,
                       -0.5,  0.5,  0.5, 1.0, 1.0,
                       0.5,  0.5,  0.5, 0.0, 1.0]

        indices = [ 0,  1,  2,  2,  3,  0,
                    4,  5,  6,  6,  7,  4,
                    8,  9, 10, 10, 11,  8,
                    12, 13, 14, 14, 15, 12,
                    16, 17, 18, 18, 19, 16,
                    20, 21, 22, 22, 23, 20 ]

        super()._handleObject(vertices, indices)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, super()._getVertices().itemsize * 5, ctypes.c_void_p(0))

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, super()._getVertices().itemsize * 5, ctypes.c_void_p(12))

        self._color_loc = pColor_loc

    def draw(self):
        glUniform1i(self._getSwitcher_loc(), 2)
        glBindVertexArray(self._VAO)
        glUniform3iv(self._color_loc, 1, (69, 30, 62))
        glUniformMatrix4fv(self._model_loc, 1, GL_FALSE, self._position)
        glDrawElements(GL_TRIANGLES, len(self.indices), GL_UNSIGNED_INT, None)
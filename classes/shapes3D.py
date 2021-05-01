from OpenGL.GL import *
from .parents import ShapeBase, DayNightTimeBase, UseColorType
from utils.TextureLoader import load_texture


class Floor(ShapeBase):
    def __init__(self, pModel_loc=None, pSwitcher_loc=None, pCordinates=None, pColor_loc=None):
        super().__init__(pModel_loc, pSwitcher_loc, pCordinates, pColor_loc)
        color    = [54/255, 119/255, 31/255]
        vertices = [-20, 0.0, 20, *color,
                     20, 0.0, 20, *color,
                    -20, 0.0, -20, *color,
                     20, 0.0, -20, *color]

        super()._handleObject(vertices, [])
    
class House(ShapeBase):
    def __init__(self, pModel_loc=None, pSwitcher_loc=None, pCordinates=None, pColor_loc=None):
        super().__init__(pModel_loc, pSwitcher_loc, pCordinates, pColor_loc)
        front_color = [182/255, 81/255, 87/255]
        side_color  = [31/255, 58/255, 84/255]
        back_color  = [31/255, 58/255, 84/255]
        none_color  = [0,0,0]
        vertices   = [ -2.0, -0.0,  2.0, *front_color, #front
                        2.0, -0.0,  2.0, *front_color,  
                        2.0,  1.0,  2.0, *front_color, 
                       -2.0,  1.0,  2.0, *front_color, 

                       -2.0, -0.0, -2.0, *back_color, # back
                        2.0, -0.0, -2.0, *back_color,
                        2.0,  1.0, -2.0, *back_color,
                       -2.0,  1.0, -2.0, *back_color,

                        2.0, -0.0, -2.0, *side_color, # right
                        2.0,  1.0, -2.0, *side_color,
                        2.0,  1.0,  2.0, *side_color,
                        2.0, -0.0,  2.0, *side_color,

                       -2.0,  1.0, -2.0, *side_color, # left
                       -2.0, -0.0, -2.0, *side_color, 
                       -2.0, -0.0,  2.0, *side_color, 
                       -2.0,  1.0,  2.0, *side_color, 

                       -2.0, -0.0, -2.0, *none_color, # down
                        2.0, -0.0, -2.0, *none_color,
                        2.0, -0.0,  2.0, *none_color,
                       -2.0, -0.0,  2.0, *none_color,

                        2.0,  1.0, -2.0, *none_color, # top
                        -2.0, 1.0, -2.0, *none_color,
                        -2.0, 1.0,  2.0, *none_color,
                        2.0,  1.0,  2.0, *none_color]

        indices = [ 0,  1,  2,  2,  3,  0,
                    4,  5,  6,  6,  7,  4,
                    8,  9, 10, 10, 11,  8,
                    12, 13, 14, 14, 15, 12,
                    16, 17, 18, 18, 19, 16,
                    20, 21, 22, 22, 23, 20 ]

        super()._handleObject(vertices, indices)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, super()._getVertices().itemsize * 6, ctypes.c_void_p(0))

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, super()._getVertices().itemsize * 6, ctypes.c_void_p(12))

    def draw(self):
        glUniform1i(self._getSwitcher_loc(), 1)
        glBindVertexArray(self._VAO)
        #glUniform3iv(self._color_loc, 1, (69, 30, 62))
        glUniformMatrix4fv(self._model_loc, 1, GL_FALSE, self._position)
        glDrawElements(GL_TRIANGLES, len(self.indices), GL_UNSIGNED_INT, None)

class Roof(ShapeBase):
    def __init__(self, pModel_loc=None, pSwitcher_loc=None, pCordinates=None, pColor_loc=None):
        super().__init__(pModel_loc, pSwitcher_loc, pCordinates, pColor_loc)
        front_color = [170/255, 170/255, 170/255]
        side_color  = [204/255, 204/255, 204/255]
        vertices   = [ -2.0, -2.0,  2.0, *front_color, #front
                        2.0, -2.0,  2.0, *front_color,  
                        0.0,  2.0,  2.0, *front_color, 
                        0.0,  2.0,  2.0, *front_color,  

                       -2.0, -2.0, -2.0, *front_color, # back
                        2.0, -2.0, -2.0, *front_color,
                        0.0,  2.0, -2.0, *front_color,
                        0.0,  2.0, -2.0, *front_color, 
#
                        2.0, -2.0, -2.0, *side_color, # right
                        0.0,  2.0, -2.0, *side_color,
                        0.0,  2.0,  2.0, *side_color,
                        2.0, -2.0,  2.0, *side_color, 
#
                       -0.0,  2.0, -2.0, *side_color, # left
                       -2.0, -2.0, -2.0, *side_color, 
                       -2.0, -2.0,  2.0, *side_color, 
                       -0.0,  2.0,  2.0, *side_color ]

        indices = [ 0,  1,  2,  2,  3,  0,
                    4,  5,  6,  6,  7,  4,
                    8,  9, 10, 10, 11,  8,
                    12, 13, 14, 14, 15, 12 ]

        super()._handleObject(vertices, indices)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, super()._getVertices().itemsize * 6, ctypes.c_void_p(0))

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, super()._getVertices().itemsize * 6, ctypes.c_void_p(12))

    def draw(self):
        glUniform1i(self._getSwitcher_loc(), 1)
        glBindVertexArray(self._VAO)
        glUniformMatrix4fv(self._model_loc, 1, GL_FALSE, self._position)
        glDrawElements(GL_TRIANGLES, len(self.indices), GL_UNSIGNED_INT, None)

class Window(ShapeBase):
    def __init__(self, pModel_loc=None, pSwitcher_loc=None, pCordinates=None, pColor_loc=None):
        super().__init__(pModel_loc, pSwitcher_loc, pCordinates, pColor_loc)
        vertices = [-0.2, -0.2, 0.2, 0.0, 0.0,
                    0.2, -0.2, 0.2, 1.0, 0.0,
                    0.2, 0.2, 0.2, 1.0, 1.0,
                    -0.2, 0.2, 0.2, 0.0, 1.0,

                    -0.2, -0.2, -0.2, 0.0, 0.0,
                    0.2, -0.2, -0.2, 1.0, 0.0,
                    0.2, 0.2, -0.2, 1.0, 1.0,
                    -0.2, 0.2, -0.2, 0.0, 1.0,

                    0.2, -0.2, -0.2, 0.0, 0.0,
                    0.2, 0.2, -0.2, 1.0, 0.0,
                    0.2, 0.2, 0.2, 1.0, 1.0,
                    0.2, -0.2, 0.2, 0.0, 1.0,

                    -0.2, 0.2, -0.2, 0.0, 0.0,
                    -0.2, -0.2, -0.2, 1.0, 0.0,
                    -0.2, -0.2, 0.2, 1.0, 1.0,
                    -0.2, 0.2, 0.2, 0.0, 1.0,

                    -0.2, -0.2, -0.2, 0.0, 0.0,
                    0.2, -0.2, -0.2, 1.0, 0.0,
                    0.2, -0.2, 0.2, 1.0, 1.0,
                    -0.2, -0.2, 0.2, 0.0, 1.0,

                    0.2, 0.2, -0.2, 0.0, 0.0,
                    -0.2, 0.2, -0.2, 1.0, 0.0,
                    -0.2, 0.2, 0.2, 1.0, 1.0,
                    0.2, 0.2, 0.2, 0.0, 1.0]

        indices = [ 0, 1, 2, 2, 3, 0,
                    4, 5, 6, 6, 7, 4,
                    8, 9, 10, 10, 11, 8,
                    12, 13, 14, 14, 15, 12,
                    16, 17, 18, 18, 19, 16,
                    20, 21, 22, 22, 23, 20]

        super()._handleObject(vertices, indices)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, super()._getVertices().itemsize * 5, ctypes.c_void_p(0))

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, super()._getVertices().itemsize * 5, ctypes.c_void_p(12))

        load_texture("textures/window.webp", super()._getTexture())

    def draw(self):
        glBindVertexArray(self._VAO)
        glBindTexture(GL_TEXTURE_2D, self._texture)
        glUniformMatrix4fv(self._model_loc, 1, GL_FALSE, self._position)
        glDrawElements(GL_TRIANGLES, len(self.indices), GL_UNSIGNED_INT, None)
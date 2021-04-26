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

class Moon(ShapeBase):
    def __init__(self, pModel_loc, pSwitcher_loc, pCordinates):
        super().__init__(pModel_loc, pSwitcher_loc, pCordinates)
        color    = [1,1,1]
        vertices = [-0.60, 0.77, 0, *color,
                    -0.68, 0.77, 0, *color,
                    -0.70, 0.68, 0, *color,
                    -0.64, 0.63, 0, *color,
                    -0.58, 0.68, 0, *color ]

        super()._handleObject(self._getCustomVertices(), [])
        super()._setDefaultShape(GL_POLYGON)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, self.vertices.itemsize * 6, ctypes.c_void_p(0))

        glEnableVertexAttribArray(2)
        glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, self.vertices.itemsize * 6, ctypes.c_void_p(12))

    '''def _getCustomVertices(self):
        color = [1,1,1] # midnight green
        PI = 3.14159265358979323846264
        statcky=60 #divide into 60 parts
        angleHy = ( 2 * PI ) / statcky
        NumAngleHy = 0.0 # current horizontal angle

        d = np.array([], np.float32)
        R = 0.3
        x0 = 0.0
        y0 = 0.0
        for i in range(statcky): #Drawing a circle
            NumAngleHy = angleHy*i  # 
            x=R*np.cos(NumAngleHy)
            y=R*np.sin(NumAngleHy)
            d=np.hstack((d,np.array([x0+x,y0+y,0], np.float32) ))

        return np.array(d, np.float32)'''
    def _getCustomVertices(self):
        return [ 3.0000001e-01 , 0.0000000e+00 , 0.0000000e+00 , 2.9835656e-01 ,
                 3.1358540e-02 , 0.0000000e+00 , 2.9344428e-01 , 6.2373508e-02 ,
                 0.0000000e+00 , 2.8531694e-01 , 9.2705101e-02 , 0.0000000e+00 ,
                 2.7406365e-01 , 1.2202099e-01 , 0.0000000e+00 , 2.5980762e-01 ,
                 1.5000001e-01 , 0.0000000e+00 , 2.4270509e-01 , 1.7633557e-01 ,
                 0.0000000e+00 , 2.2294345e-01 , 2.0073918e-01 , 0.0000000e+00 ,
                 2.0073918e-01 , 2.2294345e-01 , 0.0000000e+00 , 1.7633557e-01 ,
                 2.4270509e-01 , 0.0000000e+00 , 1.5000001e-01 , 2.5980762e-01 ,
                 0.0000000e+00 , 1.2202099e-01 , 2.7406365e-01 , 0.0000000e+00 ,
                 9.2705101e-02 , 2.8531694e-01 , 0.0000000e+00 , 6.2373508e-02 ,
                 2.9344428e-01 , 0.0000000e+00 , 3.1358540e-02 , 2.9835656e-01 ,
                 0.0000000e+00 , 1.8369703e-17 , 3.0000001e-01 , 0.0000000e+00 ,
                 -3.1358540e-02 , 2.9835656e-01 , 0.0000000e+00 , -6.2373508e-02  ,
                 2.9344428e-01 , 0.0000000e+00 , -9.2705101e-02 ,  2.8531694e-01 ,
                 0.0000000e+00 , -1.2202099e-01 , 2.7406365e-01 , 0.0000000e+00 ,
                 -1.5000001e-01 , 2.5980762e-01 , 0.0000000e+00 , -1.7633557e-01 ,
                 2.4270509e-01 , 0.0000000e+00 , -2.0073918e-01 , 2.2294345e-01 ,
                 0.0000000e+00 , -2.2294345e-01 , 2.0073918e-01 , 0.0000000e+00 ,
                 -2.4270509e-01 , 1.7633557e-01 , 0.0000000e+00 , -2.5980762e-01 ,
                 1.5000001e-01 , 0.0000000e+00 , -2.7406365e-01 , 1.2202099e-01 ,
                 0.0000000e+00 , -2.8531694e-01 , 9.2705101e-02 , 0.0000000e+00 ,
                 -2.9344428e-01 , 6.2373508e-02 , 0.0000000e+00 , -2.9835656e-01 ,
                 3.1358540e-02 , 0.0000000e+00 , -3.0000001e-01 , 3.6739406e-17 ,
                 0.0000000e+00 , -2.9835656e-01 , -3.1358540e-02 , 0.0000000e+00 ,
                 -2.9344428e-01 , -6.2373508e-02 , 0.0000000e+00 , -2.8531694e-01 ,
                 -9.2705101e-02 , 0.0000000e+00 , -2.7406365e-01 , -1.2202099e-01 ,
                 0.0000000e+00 , -2.5980762e-01 , -1.5000001e-01 , 0.0000000e+00 ,
                 -2.4270509e-01 , -1.7633557e-01 , 0.0000000e+00 , -2.2294345e-01 ,
                 -2.0073918e-01 , 0.0000000e+00 , -2.0073918e-01 , -2.2294345e-01 ,
                 0.0000000e+00 , -1.7633557e-01 , -2.4270509e-01 ,  0.0000000e+00 ,
                 -1.5000001e-01 , -2.5980762e-01 , 0.0000000e+00 , -1.2202099e-01 ,
                 -2.7406365e-01 , 0.0000000e+00 , -9.2705101e-02 , -2.8531694e-01 ,
                 0.0000000e+00 , -6.2373508e-02 , -2.9344428e-01 , 0.0000000e+00 ,
                 -3.1358540e-02 , -2.9835656e-01 , 0.0000000e+00 , -5.5109105e-17 ,
                 -3.0000001e-01 , 0.0000000e+00 , 3.1358540e-02 , -2.9835656e-01 ,
                 0.0000000e+00 , 6.2373508e-02 , -2.9344428e-01 , 0.0000000e+00 ,
                 9.2705101e-02 , -2.8531694e-01 , 0.0000000e+00 , 1.2202099e-01 ,
                 -2.7406365e-01 , 0.0000000e+00 , 1.5000001e-01 , -2.5980762e-01 ,
                 0.0000000e+00 , 1.7633557e-01 , -2.4270509e-01 , 0.0000000e+00 ,
                 2.0073918e-01 , -2.2294345e-01 , 0.0000000e+00 , 2.2294345e-01 ,
                 -2.0073918e-01 , 0.0000000e+00 , 2.4270509e-01 , -1.7633557e-01 ,
                 0.0000000e+00 , 2.5980762e-01 , -1.5000001e-01 , 0.0000000e+00 ,
                 2.7406365e-01 , -1.2202099e-01 , 0.0000000e+00 , 2.8531694e-01 ,
                 -9.2705101e-02 , 0.0000000e+00 , 2.9344428e-01 , -6.2373508e-02 ,
                 0.0000000e+00 , 2.9835656e-01 , -3.1358540e-02 , 0.0000000e+00]

    def draw(self):
        super().draw()
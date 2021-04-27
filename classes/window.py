import sys
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import OpenGL.GLUT as glut
import pyrr
from .parents import DayNightTimeBase, DaytimeBase, NighttimeBase, UseColorType
import numpy as np

vertex_src = """
# version 330

layout(location = 0) in vec3 a_position;
layout(location = 1) in vec2 a_texture;
layout(location = 2) in vec3 a_color;

uniform mat4 model;
uniform mat4 projection;
uniform mat4 view;

out vec3 v_color;
out vec2 v_texture;

void main()
{
    gl_Position = projection * view * model * vec4(a_position, 1.0);
    v_texture = a_texture;
    v_color = a_color;
}
"""

fragment_src = """
# version 330

in vec2 v_texture;
in vec3 v_color;

out vec4 out_color;
uniform int switcher;
uniform ivec3 icolor;
uniform sampler2D s_texture;

void main()
{
    if (switcher == 0){
        out_color = texture(s_texture, v_texture);
    } else if (switcher == 1){
        out_color = vec4(v_color, 1.0);           
    } else if (switcher == 2) {
        out_color = vec4(icolor.r/255.0, icolor.g/255.0, icolor.b/255.0, 1.0);
    }
}
"""

class Window:
    def __init__(self, width: int, height: int, title: str):
        self.__Daytime = True

        glut.glutInit()
        glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGBA)
        glut.glutInitWindowSize(width, height)
        glut.glutInitWindowPosition(0,0)
        glut.glutCreateWindow(title)
        glut.glutReshapeFunc(self.__window_resize)
        glut.glutDisplayFunc(self.__display)
        glut.glutKeyboardFunc(self.__keyboard)

        self._create_shader()
        self.__setSky(True)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        self.__ElementsList = []

    def __setSky(self, Daytime:bool):
        if (Daytime == True):
            glClearColor(173/255, 203/255, 227/255, 1) # blue sky
        else:
            glClearColor(0/255, 3/255, 22/255, 1) # midnight blue sky

    def _create_shader(self):
        shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER), compileShader(fragment_src, GL_FRAGMENT_SHADER))

        glUseProgram(shader)
        self.projection = pyrr.matrix44.create_perspective_projection_matrix(45, 1280 / 720, 0.1, 100)

        # eye, target, up
        self.view = pyrr.matrix44.create_look_at(pyrr.Vector3([0, 0, 4]), pyrr.Vector3([0, 0, 0]), pyrr.Vector3([0, 1, 0]))

        self.model_loc    = glGetUniformLocation(shader, "model")
        self.proj_loc     = glGetUniformLocation(shader, "projection")
        self.view_loc     = glGetUniformLocation(shader, "view")
        self.switcher_loc = glGetUniformLocation(shader, "switcher")
        self.icolor_loc   = glGetUniformLocation(shader, "icolor")

        glUniformMatrix4fv(self.proj_loc, 1, GL_FALSE, self.projection)
        glUniformMatrix4fv(self.view_loc, 1, GL_FALSE, self.view)

    def __keyboard(self, key, x, y ):
        if key == b'\x1b': # ESC key pressed
            sys.exit()

        if key.lower() == b'n': # N key pressed
            self.__Daytime = False
            self.__display()

        if key.lower() == b'd': # D key pressed
            self.__Daytime = True
            self.__display()

    def __display(self):
        self.__setSky(self.__Daytime)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for element in self.__ElementsList:

            if isinstance(element, DayNightTimeBase):
                element.setDaytime(self.__Daytime)

            glUniform1i(self.switcher_loc, 0)

            if isinstance(element, DaytimeBase):
                if self.__Daytime == True:
                    element.draw()
            elif isinstance(element, NighttimeBase):
                if self.__Daytime == False:
                    element.draw()
            else:
                element.draw()

        glut.glutSwapBuffers()

    def __window_resize(self, width,height):
        glViewport(0, 0, width, height)
        projection = pyrr.matrix44.create_perspective_projection_matrix(45, width / height, 0.1, 100)
        glUniformMatrix4fv(self.proj_loc, 1, GL_FALSE, projection)

    def addElement(self, element, cordinates): 
        self.__ElementsList.append(element(pModel_loc=self.model_loc, pSwitcher_loc=self.switcher_loc, pCordinates=cordinates, pColor_loc=self.icolor_loc))

    def execute(self):
        glut.glutMainLoop()
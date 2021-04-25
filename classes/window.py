import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np
import pyrr

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

uniform sampler2D s_texture;

void main()
{
    if (switcher == 0){
        out_color = texture(s_texture, v_texture);
    }
    else if (switcher == 1){
        out_color = vec4(v_color, 1.0);   
    }

}
"""

class Window:
    def __init__(self, width: int, height: int, title: str):
        # initializing glfw library
        if not glfw.init():
            raise Exception("glfw can not be initialized!")

        # creating the window
        self._window = glfw.create_window(width, height, title, None, None)

        # check if window was created
        if not self._window:
            glfw.terminate()
            raise Exception("glfw window can not be created!")

        # set window's position
        glfw.set_window_pos(self._window, 400, 200)

        # set the callback function for window resize
        glfw.set_window_size_callback(self._window, self._window_resize)

        # make the context current
        glfw.make_context_current(self._window)

        self._create_shader()
        glClearColor(1/255, 31/255, 75/255, 1)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        self.__ElementsList = []

    # glfw callback functions
    def _window_resize(self, window, width, height):
        glViewport(0, 0, width, height)
        projection = pyrr.matrix44.create_perspective_projection_matrix(45, width / height, 0.1, 100)
        glUniformMatrix4fv(self.proj_loc, 1, GL_FALSE, projection)

    def _create_shader(self):
        shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER), compileShader(fragment_src, GL_FRAGMENT_SHADER))

        glUseProgram(shader)
        self.projection = pyrr.matrix44.create_perspective_projection_matrix(45, 1280 / 720, 0.1, 100)

        # eye, target, up
        self.view = pyrr.matrix44.create_look_at(pyrr.Vector3([0, 0, 4]), pyrr.Vector3([0, 0, 0]), pyrr.Vector3([0, 1, 0]))

        self.model_loc = glGetUniformLocation(shader, "model")
        self.proj_loc = glGetUniformLocation(shader, "projection")
        self.view_loc = glGetUniformLocation(shader, "view")
        self.switcher_loc = glGetUniformLocation(shader, "switcher")

        glUniformMatrix4fv(self.proj_loc, 1, GL_FALSE, self.projection)
        glUniformMatrix4fv(self.view_loc, 1, GL_FALSE, self.view)

    def addElement(self, element, cordinates):
        self.__ElementsList.append(element(self.model_loc, self.switcher_loc, cordinates))

    def main_loop(self):
        # the main application loop
        while not glfw.window_should_close(self._window):
            glfw.poll_events()

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            for element in self.__ElementsList:
                glUniform1i(self.switcher_loc, 0)
                element.draw()

            glfw.swap_buffers(self._window)

        # terminate glfw, free up allocated resources
        glfw.terminate()
import glm
import numpy as np
from math import sin, cos, radians

class Camera:
    def __init__(self):
        self.setInitCamera()
        self.mouse_sensitivity = 0.10
        self.jaw               = -90
        self.pitch             = 0

    def setInitCamera(self):
        self.camera_pos   = glm.vec3(3.6, 2, 11.3)
        self.camera_front = glm.vec3(-0.32053047,  0.02268733, -0.94696647)
        self.camera_up    = glm.vec3(0.007, 1, 0.02)
        self.camera_right = glm.vec3(0.95,  0.0 , -0.3)

    def get_view_matrix(self):
        return np.array(glm.lookAt(self.camera_pos, self.camera_pos + self.camera_front, self.camera_up), dtype=np.float32)

    def process_mouse_movement(self, xoffset, yoffset, constrain_pitch=True):
        xoffset *= self.mouse_sensitivity
        yoffset *= self.mouse_sensitivity

        self.jaw += xoffset
        self.pitch += yoffset

        if constrain_pitch:
            if self.pitch > 45:
                self.pitch = 45
            if self.pitch < -45:
                self.pitch = -45

        self.update_camera_vectors()

    def update_camera_vectors(self):
        front = glm.vec3(0.0, 0.0, 0.0)
        front.x = cos(radians(self.jaw)) * cos(radians(self.pitch))
        front.y = sin(radians(self.pitch))
        front.z = sin(radians(self.jaw)) * cos(radians(self.pitch))

        self.camera_front = glm.normalize(front)
        self.camera_right = glm.normalize(glm.cross(self.camera_front, glm.vec3(0.0, 1.0, 0.0)))
        self.camera_up = glm.normalize(glm.cross(self.camera_right, self.camera_front))

    # Camera method for the WASD movement
    def process_keyboard(self, direction, velocity):
        if direction == "FORWARD":
            self.camera_pos += self.camera_front * velocity
        if direction == "BACKWARD":
            self.camera_pos -= self.camera_front * velocity
        if direction == "LEFT":
            self.camera_pos -= self.camera_right * velocity
        if direction == "RIGHT":
            self.camera_pos += self.camera_right * velocity

















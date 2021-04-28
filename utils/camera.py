from pyrr import Vector3, vector, vector3, matrix44
from math import sin, cos, radians

class Camera:
    def __init__(self):
        self.setInitCamera()
        self.mouse_sensitivity = 0.10
        self.jaw               = -90
        self.pitch             = 0

    def setInitCamera(self):
        '''self.camera_pos   = Vector3([1.0, 2.0, 10.0])
        self.camera_front = Vector3([-0.2, 0.0, -3.0])
        self.camera_up    = Vector3([0.0, 1.0, 0.0])
        self.camera_right = Vector3([1.0, 0.0, 0.0])'''

        self.camera_pos   = Vector3([3.6, 2, 11.3])
        self.camera_front = Vector3([-0.32053047,  0.02268733, -0.94696647])
        self.camera_up    = Vector3([0.007, 1, 0.02])
        self.camera_right = Vector3([ 0.95,  0.0 , -0.3])

    def get_view_matrix(self):
        return matrix44.create_look_at(self.camera_pos, self.camera_pos + self.camera_front, self.camera_up)

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
        front = Vector3([0.0, 0.0, 0.0])
        front.x = cos(radians(self.jaw)) * cos(radians(self.pitch))
        front.y = sin(radians(self.pitch))
        front.z = sin(radians(self.jaw)) * cos(radians(self.pitch))

        self.camera_front = vector.normalise(front)
        self.camera_right = vector.normalise(vector3.cross(self.camera_front, Vector3([0.0, 1.0, 0.0])))
        self.camera_up = vector.normalise(vector3.cross(self.camera_right, self.camera_front))

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

















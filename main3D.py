from classes.window import Window
import classes.shapes3D as shapes3D
import classes.shapes2D as shapes2D
from OpenGL.GL import glClearColor

def setBackground(parameter):
    glClearColor(0, 0.1, 0.1, 1)

if __name__ == '__main__':
    window = Window(1300, 768, 'House 3D simulation', True)
    window.setSky = setBackground

    window.addElement(shapes3D.House, [-1, 0, 0])
    window.addElement(shapes3D.Roof, [-1, 3, 0])
    window.addElement(shapes3D.Floor, [0, 0, 0])
    window.addElement(shapes2D.Door, [-1, 0.51, 2.01])
    window.addElement(shapes2D.DoorHandle, [-1.1, 0.3, 2.011])
    window.addElement(shapes3D.Window, [0.81, 0.5, 1])
    window.addElement(shapes3D.Window, [0.81, 0.5, -1])
    window.addElement(shapes3D.Window, [-2.81, 0.5, 1])
    window.addElement(shapes3D.Window, [-2.81, 0.5, -1])

    window.execute()
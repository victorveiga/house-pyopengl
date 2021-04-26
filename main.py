from classes.window import Window
import classes.shapes2D as shapes2D
import classes.shapes3D as shapes3D

if __name__ == '__main__':
    window = Window(1300, 768, 'House 2D simulation')

    window.addElement(shapes2D.Roof1, [-1, 0.8, 1])
    window.addElement(shapes2D.Roof2, [0, 0.8, 1])
    window.addElement(shapes2D.Wall1, [-1, -0.2, 1])
    window.addElement(shapes2D.Wall2, [0, -0.2, 1])
    window.addElement(shapes2D.Door, [-1.2, -0.2, 1.01])
    window.addElement(shapes2D.DoorHandle, [-1.3, -0.35, 1.011])
    window.addElement(shapes2D.Path, [-1.2, -0.9, 1.011])
    window.addElement(shapes2D.WindowObj, [-0.1, -0.2, 1.01])
    window.addElement(shapes2D.WindowObj, [1.3, -0.2, 1.01])

    window.addElement(shapes2D.Garden, [-1.2, -0.3, 1.0])
    window.addElement(shapes2D.Sky, [-1.2, 0.7, 1.0])

    
    window.addElement(shapes3D.Cube, [1,0,0])

    window.execute()
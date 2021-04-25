from classes.window import Window
import classes.shapes2D as shapes

if __name__ == '__main__':
    window = Window(1300, 768, 'House 2D simulation')

    window.addElement(shapes.Roof1, [-1, 0.8, 1])
    window.addElement(shapes.Roof2, [0, 0.8, 1])
    window.addElement(shapes.Wall1, [-1, -0.2, 1])
    window.addElement(shapes.Wall2, [0, -0.2, 1])
    window.addElement(shapes.Door, [-1.2, -0.2, 1.01])
    window.addElement(shapes.DoorHandle, [-1.3, -0.35, 1.011])
    window.addElement(shapes.Path, [-1.2, -0.9, 1.011])
    window.addElement(shapes.WindowObj, [-0.1, -0.2, 1.01])
    window.addElement(shapes.WindowObj, [1.3, -0.2, 1.01])

    window.addElement(shapes.Garden, [-1.2, -0.3, 1.0])
    window.addElement(shapes.Sky, [-1.2, 0.7, 1.0])

    window.execute()
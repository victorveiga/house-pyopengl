from classes.window import Window
import classes.shapes2D as shapes2D

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

    # Stars
    window.addElement(shapes2D.Star, [1,2,-3])
    window.addElement(shapes2D.Star, [2,2,-4])
    window.addElement(shapes2D.Star, [3,2,-3])
    window.addElement(shapes2D.Star, [3.1,2,-4])
    window.addElement(shapes2D.Star, [-1,2.2,-5])
    window.addElement(shapes2D.Star, [-3,2,-3])
    window.addElement(shapes2D.Star, [-4,2,-4])
    window.addElement(shapes2D.Star, [3,2,0])
    window.addElement(shapes2D.Moon, [2.9,1.5,-1])
    window.addElement(shapes2D.Cloud, [1,1.5,-1])
    window.addElement(shapes2D.Cloud, [-2.2,1.0,-1])
    window.addElement(shapes2D.Sun, [3,1.7,-1])

    window.execute()
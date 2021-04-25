from classes.window import Window
from classes.shapes import Cube, Quad, Triangle, Roof1, Roof2, Wall1, Wall2, Door, DoorHandle, Path, WindowObj, Garden, Sky

if __name__ == '__main__':
    window = Window(1200, 768, 'House')

    window.addElement(Roof1, [-1, 0.8, 1])
    window.addElement(Roof2, [0, 0.8, 1])
    window.addElement(Wall1, [-1, -0.2, 1])
    window.addElement(Wall2, [0, -0.2, 1])
    window.addElement(Door, [-1.2, -0.2, 1.01])
    window.addElement(DoorHandle, [-1.3, -0.35, 1.011])
    window.addElement(Path, [-1.2, -0.9, 1.011])
    window.addElement(WindowObj, [-0.1, -0.2, 1.01])
    window.addElement(WindowObj, [1.3, -0.2, 1.01])
    
    window.addElement(Garden, [-1.2, -0.3, 1.0])
    window.addElement(Sky, [-1.2, 0.7, 1.0])

    window.main_loop()
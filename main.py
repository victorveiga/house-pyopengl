from classes.window import Window
from classes.shapes import Cube, Quad, Triangle, Roof1, Roof2, Wall1, Wall2, Door, DoorHandle, Path, Window1, Window2

if __name__ == '__main__':
    window = Window(1200, 768, 'House')

    window.addElement(Roof1, [-1, 1, 1])
    window.addElement(Roof2, [0, 1, 1])
    window.addElement(Wall1, [-1, 0, 1])
    window.addElement(Wall2, [0, 0, 1])
    window.addElement(Door, [-1.2, 0, 1.01])
    window.addElement(DoorHandle, [-1.3, -0.15, 1.011])
    window.addElement(Path, [-1.2, -0.7, 1.011])
    window.addElement(Window1, [-0.1, 0, 1.01])
    window.addElement(Window2, [1.3, 0, 1.01])

    window.main_loop()
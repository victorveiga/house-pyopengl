from classes.window import Window
from classes.shapes import Cube, Quad, Triangle

if __name__ == '__main__':
    window = Window(1200, 768, 'House')
    window.addElement(Cube(window.model_loc))
    window.addElement(Quad(window.model_loc))
    window.addElement(Triangle(window.model_loc, window.switcher_loc))
    window.main_loop()
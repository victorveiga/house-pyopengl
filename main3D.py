from classes.window import Window
import classes.shapes3D as shapes3D

if __name__ == '__main__':
    window = Window(1300, 768, 'House 3D simulation')

    window.addElement(shapes3D.Cube, [-1, 0, 0])
    window.addElement(shapes3D.Roof, [-1, 1.0, 0])

    window.execute()
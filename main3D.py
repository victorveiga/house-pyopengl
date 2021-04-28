from classes.window import Window
import classes.shapes3D as shapes3D

if __name__ == '__main__':
    window = Window(1300, 768, 'House 3D simulation', True)

    window.addElement(shapes3D.House, [-1, 0, 0])
    window.addElement(shapes3D.Floor, [0, -0.5, 0])

    window.execute()
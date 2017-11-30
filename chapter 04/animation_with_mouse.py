# animate_with_keys.py
#
# This program illustrates how to animate a drawing using input from the mouse.
#
# by Mr. Ciccolo

from graphics import *


def main():
    print("Click the mouse to move the circle!")

    window_size = 600
    canvas_size = 20

    win = GraphWin("Animation Example with Mouse", window_size, window_size)
    win.setCoords(0, 0, canvas_size, canvas_size)
    win.setBackground("black")

    circle = Circle(Point(canvas_size / 2, canvas_size / 2), 2)
    circle.setFill("white")
    circle.draw(win)

    while True:
        click_point = win.getMouse()

        current_x = circle.getCenter().getX()
        current_y = circle.getCenter().getY()

        next_x = click_point.getX()
        next_y = click_point.getY()

        delta_x = next_x - current_x
        delta_y = next_y - current_y

        circle.move(delta_x, delta_y)


main()

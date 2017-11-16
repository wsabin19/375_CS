from graphics import *


def main():
    win = GraphWin("picture", 800, 800)
    win.setCoords(0, 0, 20, 20)
    ground = Rectangle(Point(0, 0),Point(20, 3))
    ground.setFill(color_rgb(102, 51, 0))
    ground.draw(win)

    grass = Rectangle(Point(0, 3), Point(20, 4))
    grass.setFill(color_rgb(102, 204, 0))
    grass.draw(win)

    trunk = Rectangle(Point(8, 4), Point(10, 10))
    trunk.setFill(color_rgb(153, 76, 0))
    trunk.draw(win)

    leaves = Circle(Point(9, 13), 4)
    leaves.setFill('green')
    leaves.draw(win)


    cloudA = Oval(Point(1, 17), Point(5, 19))
    cloudA.setFill('white')
    cloudA.draw(win)

    cloudB = Oval(Point(13, 15), Point(17, 18))
    cloudB.setFill('white')
    cloudB.draw(win)


    input("Press any key to quit")





main()


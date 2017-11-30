# py_83.py
#
# This program simulates the graphing capabilities of a TI-83 calculator.
#
# by Mr. Ciccolo

from graphics import *


def main():

    # Step 1: Ask the user for the equation to graph and the range of values
    #         to use for x.

    equation = input("Enter your equation (must be in terms of 'x'): ")
    lower_x = int(input("Enter x lower bounds: "))
    upper_x = int(input("Enter x upper bounds: "))

    lower_y = 0
    upper_y = 0
    points = []

    # Step 2: Calculate y for each value of x and print a chart of the results.
    #         Also remember each point (as a graphics object) along with the
    #         max and min y values so we can graph them later.

    print("x      | y    ")
    print("-------+-------")
    for x in range(lower_x, upper_x + 1):
        y = eval(equation)

        if y < lower_y:
            lower_y = y
        elif y > upper_y:
            upper_y = y

        print("% 7d|% 7d" % (x, y))
        points.append(Point(x, y))

    # Step 3: Create a graph with a coordinate system based on the lower/upper
    #         bounds for x and y. Label the axes and plot the points calculated
    #         above.

    win = GraphWin("PY-83 Graphing Calculator", 500, 500)
    win.setBackground("white")
    win.setCoords(lower_x, lower_y, upper_x, upper_y)

    Line(Point(lower_x, 0), Point(upper_x, 0)).draw(win)
    Line(Point(0, lower_y), Point(0, upper_y)).draw(win)

    Text(Point(lower_x + 0.5, 1), str(lower_x)).draw(win)
    Text(Point(upper_x - 0.5, 1), str(upper_x)).draw(win)

    Text(Point(1, lower_y + 0.5), str(lower_y)).draw(win)
    Text(Point(1, upper_y - 0.5), str(upper_y)).draw(win)

    for point in points:
        point.draw(win)

    # Step 4: Pause the program
    input("Press the Return key to quit")


main()

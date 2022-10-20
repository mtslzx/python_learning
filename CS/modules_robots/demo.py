from cs1graphics import *
from cs1graphicsHelper import *

# Reference points:
# Basic shapes (Square, Circle, Rectangle): Center of the shape
# Polygon: First point of the polygon
# Layer: 0,0


paper = Canvas(500, 500, 'yellow')


def exampleBasicShapes():
    ''' Draws basic shapes (Circle, Square, Rectangle);
    Demonstrates the reference point is the center of the shapes '''
    circle = Circle(50, Point(100, 100))
    circle.setFillColor('purple')
    paper.add(circle)

    square = Square(100, Point(225, 100))
    square.setFillColor('purple')
    paper.add(square)

    rectangle = Rectangle(150, 100, Point(400, 100))
    rectangle.setFillColor('purple')
    paper.add(rectangle)

exampleBasicShapes()


def examplePolygon():
    ''' Draws a polygon;
    Demonstrates the reference point is the first point in the polygon '''
    poly = Polygon(Point(-50, 0), Point(50, 0), Point(0, 100))
    poly.setFillColor('green')
    poly.moveTo(100, 200)
    paper.add(poly)

examplePolygon()


def exampleLayer():
    ''' Draws a layer with two shapes
    Demonstrates the reference point of a layer is 0,0 '''

    toybox = Layer()

    # Shape 1 - A blue cone
    cone = Polygon(Point(-50, 0), Point(50, 0), Point(0, 100))
    cone.setFillColor('blue')
    toybox.add(cone)

    # Shape 2 - A blue circle
    ball = Circle(50, Point(50, 50))
    ball.setFillColor('blue')
    toybox.add(ball)

    toybox.moveTo(100, 375)
    paper.add(toybox)

exampleLayer()


# Invoke helper functions as the last step
drawReferencePoints(paper)
drawGrid(paper,100)
#markClicks(paper)

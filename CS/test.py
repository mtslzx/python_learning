from cs1graphics import *

paper = Canvas()
paper.setWidth(300)
paper.setHeight(200)
paper.setBackgroundColor('skyblue')
paper.setTitle('My World')

sun = Circle()
paper.add(sun)
sun.setRadius(30)
sun.setFillColor('yellow')
sun.move(250, 50)

facade = Square(60, Point(140, 130))
facade.setFillColor('White')
paper.add(facade)

chimney = Rectangle(15, 28, Point(155,85))
chimney.setFillColor('red')
paper.add(chimney)

tree = Polygon(Point(50,80), Point(30,140), Point(70,140))
tree.setFillColor('darkgreen')
paper.add(tree)
roof = Polygon(Point(105,105), Point(175,105), Point(170,85), Point(110,85))
roof.setFillColor('darkgray')
paper.add(roof)

smoke = Path(Point(155,70), Point(150,65), Point(160,55), Point(155,50))
paper.add(smoke)



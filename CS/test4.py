from cs1graphics import *
from cs1graphicsHelper import *

paper = Canvas()
paper.setWidth(300)
paper.setHeight(200)
paper.setBackgroundColor('skyblue')
paper.setTitle('My World')

sun = Circle(30)
sun.setFillColor('yellow')
sun.move(250, 50)
paper.add(sun)

spl = Spline(Point(50,80), Point(30,140), Point(70,140))
cspl = ClosedSpline(Point(50,80), Point(30,140), Point(70,140))


spl.move(100,0)
paper.add(cspl)
paper.add(spl)

drawReferencePoints(paper)
drawGrid(paper, 100)
markClicks(paper)



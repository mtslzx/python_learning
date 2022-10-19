from cs1graphics import *

paper = Canvas()
paper.setWidth(300)
paper.setHeight(200)
paper.setBackgroundColor('skyblue')
paper.setTitle('My World')

sun = Circle(30)
sun.setFillColor('yellow')
sun.move(250, 50)
paper.add(sun)

sun.setFillColor('White')
sun.move(3, 3)
paper.add(sun)




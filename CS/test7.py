from cs1graphics import *
from time import sleep

paper = Canvas( )
cue = paper.wait( ) # wait indefinitely for user event 
ball = Circle(10, cue.getMouseLocation( ))
ball.setFillColor('red')
paper.add(ball)
paper.getAutoRefresh() # refresh
for i in range(20):
    print(paper.getMouseCoordinates())
    # paper.rotateView(45)
    # paper.zoomView(1.1)
    sleep(0.5)
    
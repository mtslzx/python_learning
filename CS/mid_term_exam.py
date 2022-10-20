from cs1graphics import *
# http://www.cs1graphics.org/
from cs1graphicsHelper import *
# https://github.com/wellesleycs111/cs1graphicsHelper
from time import sleep
# Pixel Art , Train , Pinky Sunset , Counting stars , little bit dark sky , sun , sea , cloud, steam ...


canvas = Canvas(400, 600, (119,125,183), 'Midterm Exam')

# Background

# Clouds
Clouds = Layer()



# Moon
Moon = Layer()
# moon.add(Circle(50).setFillColor((137, 151, 149))) Didn't work right...

moon1 = Circle(30)
moon1.setFillColor((249,255,255))  # Bright side color of moon
moon1.setBorderWidth(0)  # No border
Moon.add(moon1)  # Add to moon layer

moon2 = Circle(30)
moon2.setFillColor((119,125,183))  # Dark side color of moon
moon2.move(7.5,0)
moon2.setBorderWidth(0)  # No border
moon2.stretch(0.85, 1, )  # Shear to make moon look like a moon
Moon.add(moon2)  # Add to moon layer


Moon.rotate(-45)  # Rotate Moon
Moon.move(310, 60)  # Move Moon to (100, 100)
Moon.scale(0.7)  # Scale Moon to 50%






# Make Gradient
gradient = Layer()

gradient1 = Rectangle(400, 400)
gradient1.setFillColor((143,123,163))
gradient1.move(200, 350)
gradient1.setBorderWidth(0)  # No border
gradient.add(gradient1)

gradient2 = Rectangle(400, 400)
gradient2.setFillColor((172,116,155	))
gradient2.move(200, 400)
gradient2.setBorderWidth(0)  # No border
gradient.add(gradient2)

gradient3 = Rectangle(400, 400)
gradient3.setFillColor((188,104,143	))
gradient3.move(200, 450)
gradient3.setBorderWidth(0)  # No border
gradient.add(gradient3)

gradient4 = Rectangle(400, 400)
gradient4.setFillColor((215,94,136))
gradient4.move(200, 500)
gradient4.setBorderWidth(0)  # No border
gradient.add(gradient4)

gradient5 = Rectangle(400, 400)
gradient5.setFillColor((234,83,121))
gradient5.move(200, 550)
gradient5.setBorderWidth(0)  # No border
gradient.add(gradient5)

# Foreground
# Bridge


B = Layer()
Bridge = Rectangle(1400, 30)
Bridge.moveTo(0, 465)
Bridge.setFillColor('black')
B.add(Bridge)

# Pilar of Bridge
PoB = Layer()
# Pillar width is 30
# pillar = Spline(Point(200,450), Point(220,460), Point(225,480), Point(230,500), Point(230, 600), Point(260, 600), Point(260, 500), Point(265, 480), Point(270, 460), Point(290, 450))

# pillar = Spline(Point(200,450), Point(220,460), Point(225,480), Point(230,500), Point(230, 600), Point(260, 600), Point(260, 500), Point(265, 480), Point(270, 460), Point(290, 450))
# pillar = Spline(Point(200,600), Point(200, 500), Point(230, 450), Point(260, 500), Point(260, 600))
# # pillar = Polygon(Point(200,600), Point(200, 500), Point(230, 450), Point(260, 500), Point(260, 600), Point(290,600), Point(290, 500), Point(320, 450), Point(350, 500), Point(350, 600))
# pillar = Polygon(Point(100, 480), Point(110, 485), Point(115, 490), Point(117, 495), Point(120, 500), Point(120, 600), Point(140, 600), Point(140, 500), Point(143, 495), Point(145 ,490), Point(150 , 485), Point(160, 480))
# pillar.setFillColor('black')

# PoB.add(pillar)
    

for i in range(30):
    pillar = Polygon(Point(100, 480), Point(110, 485), Point(115, 490), Point(117, 495), Point(120, 500), Point(120, 600), Point(140, 600), Point(140, 500), Point(143, 495), Point(145 ,490), Point(150 , 485), Point(160, 480))
    pillar.move(-70*i, 0)
    pillar.setFillColor('black')    
    PoB.add(pillar)
    

# Train

# Steam



# Zoom in to train
# inside of train




# Add layer to canvas
canvas.add(gradient)
canvas.add(Moon)
canvas.add(PoB)
canvas.add(B)
PoB.move(300,0)


for i in range(1000):
    PoB.move(1, 0)
    sleep(0.05)


drawReferencePoints(canvas)
drawGrid(canvas, 100)
markClicks(canvas)



# Animation


for i in range(1000):
    PoB.move(10, 0)
    sleep(0.1)
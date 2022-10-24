from cs1graphics import *
# http://www.cs1graphics.org/
from cs1graphicsHelper import *
# https://github.com/wellesleycs111/cs1graphicsHelper
from time import sleep
# Pixel Art , Train , Pinky Sunset , Counting stars , little bit dark sky , sun , sea , cloud, steam ...
import random
from PIL import ImageColor



canvas = Canvas(400, 600, (119,125,183), 'Midterm Exam')

# Background

# Clouds
Clouds = Layer()

#3F499B #59639E
# Cloud 1 Generator 63	73	155 (mid) 
Cloud1 = Layer()
MidCloud1 = Circle(18)
MidCloud1.setFillColor(ImageColor.getcolor("#3F499B","RGB"))
MidCloud1.setBorderWidth(0)  # No border
Cloud1.add(MidCloud1)
for i in range(90):
    cloud = Circle(random.randrange(9, 18))
    cloud.move(random.randrange(-30, 50), random.randrange(0, 60))
    cloud.setFillColor(ImageColor.getcolor("#59639E","RGB"))
    cloud.setBorderWidth(0)  # No border
    cloud.move(random.randrange(-50, 50), random.randrange(-10, 10))  # Make Position random
    Cloud1.add(cloud)

# Cloud 1 Generator 63	73	155 (side)
for i in range(60):
    cloud = Circle(random.randrange(13, 20))
    cloud.move(random.randrange(-100, 160), random.randrange(45, 89))
    cloud.setFillColor(ImageColor.getcolor("#8EA3E7","RGB"))
    cloud.setBorderWidth(0)  # No border
    cloud.move(random.randrange(-50, 50), random.randrange(-10, 10))  # Make Position random
    Cloud1.add(cloud)
    
Cloud1.scale(random.uniform(0.5, 0.7))
Clouds.add(Cloud1)





'''
# Cloud 2 Generator 89, 99, 158
for i in range(100):
    cloud = Circle(random.randrange(6, 14))
    cloud.move(random.randrange(-114, 160), random.randrange(72, 130))
    cloud.setFillColor(ImageColor.getcolor("#59639E","RGB"))
    cloud.setBorderWidth(0)  # No border
    Clouds.add(cloud)
    
# Cloud 3 Generator 80,81,140 
for i in range(100):
    cloud = Circle(random.randrange(6, 12))
    cloud.move(random.randrange(-0, 200), random.randrange(115, 148))
    cloud.setFillColor(ImageColor.getcolor("#51518C","RGB"))
    cloud.setBorderWidth(0)  # No border
    Clouds.add(cloud)

# Cloud 4 Generator 157,63,126
for i in range(100):
    cloud = Circle(random.randrange(4, 8))
    cloud.move(random.randrange(-96, 120), random.randrange(136, 185))
    cloud.setFillColor(ImageColor.getcolor("#9D3F7E","RGB"))
    cloud.setBorderWidth(0)  # No border
    Clouds.add(cloud)
'''


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

gradient6 = Rectangle(400, 400)
gradient6.setFillColor(ImageColor.getcolor("#E54A79","RGB"))
gradient6.move(200, 600)
gradient6.setBorderWidth(0)  # No border
gradient.add(gradient6)

gradient7 = Rectangle(400, 400)
gradient7.setFillColor(ImageColor.getcolor("#FEB87B","RGB"))
gradient7.move(200, 550)
gradient7.setBorderWidth(0)  # No border
gradient.add(gradient7)

gradient8 = Rectangle(400, 400)
gradient8.setFillColor(ImageColor.getcolor("#FC713E","RGB"))
gradient8.move(200, 600)
gradient8.setBorderWidth(0)  # No border
gradient.add(gradient8)


# Make A Mountain #ED553E #810444 #410C42 #190946 #0C0D0B
Mountains = Layer()


mountain = Polygon(Point(20, 458), Point(random.randrange(65, 92), random.randrange(380, 400)), Point(random.randrange(110, 129), random.randrange(394, 447)), Point(random.randrange(147, 159), random.randrange(370, 450)), Point(random.randrange(187, 204), random.randrange(388, 411)), Point(random.randrange(221, 234), random.randrange(407, 421)), Point(random.randrange(237, 251), random.randrange(418, 442)), Point(300, 458))
mountain.setFillColor(ImageColor.getcolor("#ED553E","RGB"))
mountain.setBorderWidth(0)  # No border
# mountain.adjustReference(140, 458)  # Make AnchorPoint to center bottom corner. for make depth color
mountain.adjustReference(120,0)  # Make AnchorPoint to center bottom corner. for make depth color
print(mountain.getReferencePoint())


mountain2 = mountain.clone()  # Create new Mountain front side
mountain2.setFillColor(ImageColor.getcolor("#410C42","RGB"))
# mountain2.scale(0.8)  # Make Depth
mountain2.stretch(1, 0.9) # Make Depth

mountain3 = mountain.clone()  # Create new Mountain front side
mountain3.setFillColor(ImageColor.getcolor("#190946","RGB"))
# mountain3.scale(0.8)  # Make Depth
mountain3.stretch(1, 0.75) # Make Depth

mountain4 = mountain.clone()  # Create new Mountain front side
mountain4.setFillColor(ImageColor.getcolor("#0C0D0B","RGB"))
# mountain4.scale(0.8)  # Make Depth
mountain4.stretch(1, 0.65) # Make Depth

print(mountain.getReferencePoint())
print(mountain2.getReferencePoint())

Mountains.add(mountain)
Mountains.add(mountain2)
Mountains.add(mountain3)
Mountains.add(mountain4)



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
canvas.add(Mountains)
canvas.add(PoB)
canvas.add(B)
canvas.add(Clouds)

# Position Reset
Clouds.move(100,330)
PoB.move(300,0)


for i in range(1000):
    PoB.move(1, 0)
    if i % 100 == 0:
        Clouds.move(1,0)
    if i % 500 == 0:
        Mountains.move(1, 0)
    sleep(0.05)


drawReferencePoints(canvas)
drawGrid(canvas, 100)
markClicks(canvas)



# Animation


for i in range(1000):
    PoB.move(10, 0)
    
    sleep(0.01)
    
    
    





# Code Archive

'''
# Clouds
Clouds = Layer()

# Cloud 1 Generator 63	73	155 (mid)
Cloud1 = Layer()
MidCloud1 = Circle(18)
MidCloud1.setFillColor(ImageColor.getcolor("#3F499B","RGB"))
MidCloud1.setBorderWidth(0)  # No border
Cloud1.add(MidCloud1)
for i in range(90):
    cloud = Circle(random.randrange(9, 18))
    cloud.move(random.randrange(-30, 50), random.randrange(0, 60))
    cloud.setFillColor(ImageColor.getcolor("#3F499B","RGB"))
    cloud.setBorderWidth(0)  # No border
    cloud.move(random.randrange(-50, 50), random.randrange(-10, 10))  # Make Position random
    Cloud1.add(cloud)

# Cloud 1 Generator 63	73	155 (side)
for i in range(60):
    cloud = Circle(random.randrange(13, 20))
    cloud.move(random.randrange(-100, 160), random.randrange(45, 89))
    cloud.setFillColor(ImageColor.getcolor("#3F499B","RGB"))
    cloud.setBorderWidth(0)  # No border
    cloud.move(random.randrange(-50, 50), random.randrange(-10, 10))  # Make Position random
    Cloud1.add(cloud)

Cloud1.scale(0.7)
Clouds.add(Cloud1)
'''
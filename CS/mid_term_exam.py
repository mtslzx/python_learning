from cs1graphics import *
# http://www.cs1graphics.org/
from cs1graphicsHelper import *
# https://github.com/wellesleycs111/cs1graphicsHelper
from time import sleep
# Pixel Art , Train , Pinky Sunset , Counting stars , little bit dark sky , sun , sea , cloud, steam ...
import random
from PIL import ImageColor

# = MEMO =
# 1. Canvas
# 2. Layer
# 3. Rectangle
# 4. Circle
# 5. Polygon
# 6. Path
# 7. Text
# 8. Image
# 9. Group
# 10. Animation
# 11. Event
# 12. Color
#   - from PIL import ImageColor
#   - ImageColor.getcolor("#HEXNUM","RGB")
# 13. Point
# 14. Transform
#   - Stars -> (0,0) ~ (0,150)
#   - Moon -> (310,60)
#   - Cloud ->
#   - Sea ->
#   - Train -> (0, 425) ~ (400, 436)
#   - Sun ->
#   - Steam ->
#   - Sky ->
#   - Grass ->
#   - Bridge -> (0,450) ~ (0,600)
#   - Mountain -> (0,400) ~ (0,450)
# 15. Helper


# Main Canvas
canvas = Canvas(400, 600, (119,125,183), 'Midterm Exam')

# ==== Background ====

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

# = Moon =
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
Moon.move(310, 60)  # Move Moon
Moon.scale(0.7)  # Scale Moon to 50%

# = Stars =
# Star Generator
Stars = Layer()

# Little Star Generator
for i in range(10):
    Star = Layer()
    star = Circle(10);star_ = Circle(10)
    star.stretch(4, 1);star_.stretch(1, 4)
    star.setFillColor(ImageColor.getcolor("#FFFFFF","RGB"));star_.setFillColor(ImageColor.getcolor("#FFFFFF","RGB"))
    star.setBorderWidth(0);star_.setBorderWidth(0)
    Star.add(star);Star.add(star_)
    Star.scale(random.uniform(0.05, 0.07))
    Star.move(random.randrange(10, 440),random.randrange(10,140))  # Move Star to random position (Margin 10px)
    Stars.add(Star)

# Big Star Generator
for i in range(5):
    Star = Layer()
    star = Circle(10);star_ = Circle(10)
    star.stretch(4, 1);star_.stretch(1, 4)
    star.setFillColor(ImageColor.getcolor("#FFFFFF","RGB"));star_.setFillColor(ImageColor.getcolor("#FFFFFF","RGB"))
    star.setBorderWidth(0);star_.setBorderWidth(0)
    Star.add(star);Star.add(star_)
    #Star.rotate(random.randrange(0,360))
    Star.scale(random.uniform(0.07, 0.25))
    Star.move(random.randrange(0, 270),random.randrange(10,140))  # Move Star to random position (Margin 10px)
    Stars.add(Star)


# ==== Gradient Generator ================================================
# Make a gradient layer
Gradient = Layer()
# Adjustable Variable
offset = 100  # Offset of gradient start point
dense = 30  # You can adjust this value. Make that looks beautiful. bigger -> less dense
palete = (  # You can add more colors. Just add color hex text.
    "#8F7BA3", 
    "#AC749B", 
    "#BC688F", 
    "#D75E88", 
    "#E54A79", 
    "#f16371",
    "#f87c6e",
    "#fc946f",
    "#feac75",
    "#FEB87B", 
    "#feaa6b",
    "#fd9b5c",
    "#fd8b4e",
    "#fc7a43",
    "#FC713E",
    "#AAAAAA"
    )
# Gradient generator
for idx, hex in enumerate(palete):
    gradient_ = Rectangle(400, 400)  # Adjust this with your canvas size.
    gradient_.setFillColor(ImageColor.getcolor(hex,"RGB"))  # Thanks to PIL :)
    gradient_.move(0, idx*dense)
    gradient_.setBorderWidth(0)  # No border
    Gradient.add(gradient_)
# Reset pos & add to canvas
Gradient.move(200, 200 + offset)  # Move a whole Gradient


# = Make A Mountain = #ED553E #810444 #410C42 #190946 #0C0D0B
Mountains = Layer()
mountain = Polygon(Point(20, 458), Point(random.randrange(65, 92), random.randrange(380, 400)), Point(random.randrange(110, 129), random.randrange(394, 427)), Point(random.randrange(147, 159), random.randrange(310, 341)), Point(random.randrange(187, 204), random.randrange(346, 411)), Point(random.randrange(221, 234), random.randrange(407, 421)), Point(random.randrange(237, 251), random.randrange(418, 442)), Point(300, 458))
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

# TEST
Mountains.move(0, 84) 

# = Sun =
Sun = Layer()
sun = Circle(60)
sun.setBorderWidth(2)
sun.setFillColor(ImageColor.getcolor("#F9FDF4","RGB"))
sun.setBorderColor(ImageColor.getcolor("#FEB77C","RGB"))
sun.move(200, 430)
Sun.add(sun)




# = Seas =
Seas = Layer()
sea_base = Rectangle(400, 200)
sea_base.setBorderWidth(0)  # No border
sea_base.setFillColor(ImageColor.getcolor("#3259A5","RGB"))


Seas.add(sea_base)
Seas.move(200,640)

# ==== Foreground ====

# = Bridge =
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
    

# = Train =
Trains = Layer()
# Main Train
MTrain = Layer()




train_main = Rectangle(60, 25)
train_main.setBorderWidth(0)  # No border
train_main.setFillColor(ImageColor.getcolor("#190A09","RGB"))

train_mainUpper = Rectangle(50, 10)
train_mainUpper.setBorderWidth(0)  # No border
train_mainUpper.setFillColor(ImageColor.getcolor("#190A09","RGB"))
train_mainUpper.move(0, -11)



MTrain.add(train_main);MTrain.add(train_mainUpper)

MTrain.move(130, 436)
Trains.add(MTrain)
# Train Cabin Generator

for i in range(3):  # Make N Train Cabins. You can adjust this value to make more or less cabins.
    Train = Layer()
    train_cabin = Rectangle(70, 25);train_cabin_ = Rectangle(70, 25);train_cabin__ = Rectangle(70, 25)
    train_cabin.setFillColor(ImageColor.getcolor("#410D42","RGB")) #410D42  # Set Cabin Color
    train_cabin_.setFillColor(ImageColor.getcolor("#190946","RGB")) #190946  # Set Cabin Color
    train_cabin__.setFillColor(ImageColor.getcolor("#190A09","RGB")) #090A09  # Set Cabin Color
    train_cabin_.stretch(1, 0.90);train_cabin__.stretch(1, 0.9) # Make Depth
    train_cabin_.move(0,1);train_cabin__.move(0,3)  # Make Depth
    train_window = Rectangle(17, 7)
    train_window.setFillColor(ImageColor.getcolor("#FDA22B","RGB"))  # Set Window Color
    train_window.move(-20,-3)
    train_window_ = train_window.clone()
    train_window_.move(20,0)
    train_window__ = train_window_.clone()
    train_window__.move(20,0)
    train_connectingRod = Rectangle(5, 5)
    train_connectingRod.setFillColor(ImageColor.getcolor("#190A09","RGB"))  # Set Connecting Rod Color
    train_connectingRod.move(-38, 8)
    # No Border
    train_cabin.setBorderWidth(0);train_cabin_.setBorderWidth(0);train_cabin__.setBorderWidth(0)
    train_window.setBorderWidth(0);train_window_.setBorderWidth(0);train_window__.setBorderWidth(0)
    train_connectingRod.setBorderWidth(0)
    # Add to Train Layer
    Train.add(train_cabin);Train.add(train_cabin_);Train.add(train_cabin__)
    Train.add(train_window);Train.add(train_window_);Train.add(train_window__)
    Train.add(train_connectingRod)
    Train.move(200 + (75 * i), 436)  # move For make N trains
    Trains.add(Train) # Add to Trains Layer


# = Steam =



# == Zoom in to train ==
# == inside of train ==




# === Add layer to canvas ===
Background = Layer()
Foreground = Layer()

Background.add(Gradient)
Background.add(Sun)
Background.add(Stars)
Background.add(Moon)
Background.add(Seas)
Background.add(Mountains)
Background.add(Clouds)
Foreground.add(PoB)
Foreground.add(B)
Foreground.add(Trains)


canvas.add(Background)
canvas.add(Foreground)


# Position Reset
Clouds.move(100,330)
PoB.move(300,0)

# Test
Moon.move(0, -100)
Stars.move(0,-100)


# = Animation =
for i in range(100):
    PoB.move(1, 0)
    # if i % 100 == 0:
    #     Clouds.move(1,0)
    Mountains.move(0.05, 0)
    Sun.move(0.001,0)
    # if i % 50 == 0:
     
    sleep(0.05)
    
for i in range(1000):
    Background.move(0,1)
    Foreground.move(0,2)
    sleep(0.05)
    

# = Helper =
drawReferencePoints(canvas)
drawGrid(canvas, 100)
markClicks(canvas)



# ==== Animation ====

    
    
    





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
    
# Code Archive - Make Mountain
'''
# = Make A Mountain = #ED553E #810444 #410C42 #190946 #0C0D0B
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
'''

# Code Archive - Gradient
'''
# = Make Gradient =
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
'''
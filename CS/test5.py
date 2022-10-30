from cs1graphics import *
from cs1graphicsHelper import *
from PIL import ImageColor
import random

canvas = Canvas()
canvas.setWidth(400)
canvas.setHeight(600)
canvas.setBackgroundColor(ImageColor.getcolor("#777DB7","RGB"))
# canvas.setBackgroundColor('skyblue')
canvas.setTitle('My World')

'''
# sun = Circle(30)
# sun.setFillColor('yellow')
# sun.move(250, 50)
# canvas.add(sun)

# spl = Spline(Point(50,80), Point(30,140), Point(70,140))
# cspl = ClosedSpline(Point(50,80), Point(30,140), Point(70,140))
# spl.move(100,0)
# canvas.add(cspl)
# canvas.add(spl)
'''

# ==== Gradient Generator ================================================
# Make a gradient layer
Gradient = Layer()
# Adjustable Variable
dense = 25  # You can adjust this value. Make that looks beautiful. bigger -> less dense
palete = (  # You can add more colors. Just add color hex text.
    "#8F7BA3", 
    "#AC749B", 
    "#BC688F", 
    "#D75E88", 
    "#E54A79", 
    "#FEB87B", 
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
Gradient.move(200, 200)  # Move a whole Gradient
canvas.add(Gradient)


# ==== Star Generator ====================================================
# Make a star layer
Stars = Layer()

for i in range(10):
    Star = Layer()
    star = Circle(10)
    star_ = Circle(10)

    star.stretch(4, 1)
    star_.stretch(1, 4)

    star.setFillColor(ImageColor.getcolor("#FFFFFF","RGB"))
    star_.setFillColor(ImageColor.getcolor("#FFFFFF","RGB"))

    star.setBorderWidth(0)
    star_.setBorderWidth(0)

    Star.add(star)
    Star.add(star_)

    Star.scale(random.uniform(0.01, 0.25))
    Star. move(random.randrange(0, 400),random.randrange(0,150))
    Stars.add(Star)

canvas.add(Stars)





# ==== Cloud Generator ===================================================
#3F499B #59639E
# Cloud 1 Generator 63	73	155 (mid) 
Cloud1 = Layer()
MidCloud1 = Circle(18)
MidCloud1.setFillColor(ImageColor.getcolor("#FFFFFF","RGB"))
MidCloud1.setBorderWidth(0)  # No border
Cloud1.add(MidCloud1)

CtCloud1 = Circle(40)
CtCloud1.setFillColor(ImageColor.getcolor("#FFFFFF","RGB"))
CtCloud1.setBorderWidth(0)  # No border
CtCloud1.move(20, 50)
Cloud1.add(CtCloud1)

for i in range(60):
    cloud = Circle(random.randrange(9, 18))
    cloud.move(random.randrange(-30, 50), random.randrange(0, 60))
    cloud.setFillColor(ImageColor.getcolor("#FFFFFF","RGB"))
    cloud.setBorderWidth(0)  # No border
    cloud.move(random.randrange(-50, 50), random.randrange(-10, 10))  # Make Position random
    Cloud1.add(cloud)

# Cloud 1 Generator 63	73	155 (side)
for i in range(50):
    cloud = Circle(random.randrange(13, 20))
    cloud.move(random.randrange(-100, 160), random.randrange(45, 89))
    cloud.setFillColor(ImageColor.getcolor("#FFFFFF","RGB"))
    cloud.setBorderWidth(0)  # No border
    cloud.move(random.randrange(-50, 50), random.randrange(-10, 10))  # Make Position random
    Cloud1.add(cloud)
    
# Cloud 1 Generator (under)
for i in range(30):
    cloud = Circle(random.randrange(4, 15))
    cloud.move(random.randrange(-70, 70), random.randrange(50, 120))
    cloud.setFillColor(ImageColor.getcolor("#FFFFFF","RGB"))
    cloud.setBorderWidth(0)  # No border
    cloud.move(random.randrange(-50, 50), random.randrange(-10, 10))  # Make Position random
    Cloud1.add(cloud)
    
Cloud1.scale(random.uniform(0.5, 0.7))
Cloud1.move(150, 100)
canvas.add(Cloud1)

# Cloud1.shear(random.uniform(0.1, 0.5))




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

canvas.add(Trains)


















drawReferencePoints(canvas)
drawGrid(canvas, 100)
markClicks(canvas)






# Code Archive
# Star Generator
'''
# ==== Star Generator ====================================================
# Make a star layer
Star = Layer()

star = Circle(10)
star_ = Circle(10)

star.stretch(4, 1)
star_.stretch(1, 4)

star.setFillColor(ImageColor.getcolor("#FFFFFF","RGB"))
star_.setFillColor(ImageColor.getcolor("#FFFFFF","RGB"))

star.setBorderWidth(0)
star_.setBorderWidth(0)

Star.add(star)
Star.add(star_)

Star.scale(0.3)
Star. move(200,200)

canvas.add(Star)
'''
from cs1graphics import *
from cs1graphicsHelper import *
from PIL import ImageColor
import random





paper = Canvas()
paper.setWidth(400)
paper.setHeight(600)
paper.setBackgroundColor(ImageColor.getcolor("#777DB7","RGB"))
# paper.setBackgroundColor('skyblue')
paper.setTitle('My World')

# sun = Circle(30)
# sun.setFillColor('yellow')
# sun.move(250, 50)
# paper.add(sun)

# spl = Spline(Point(50,80), Point(30,140), Point(70,140))
# cspl = ClosedSpline(Point(50,80), Point(30,140), Point(70,140))
# spl.move(100,0)
# paper.add(cspl)
# paper.add(spl)

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
    "#FC713E"
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
paper.add(Gradient)



# gradient1 = Rectangle(400, 400)
# gradient1.setFillColor(ImageColor.getcolor("#8F7BA3","RGB"))
# gradient1.move(200, 350)
# gradient1.setBorderWidth(0)  # No border
# gradient.add(gradient1)

# gradient2 = Rectangle(400, 400)
# gradient2.setFillColor(ImageColor.getcolor("#AC749B","RGB"))
# gradient2.move(200, 400)
# gradient2.setBorderWidth(0)  # No border
# gradient.add(gradient2)

# gradient3 = Rectangle(400, 400)
# gradient3.setFillColor(ImageColor.getcolor("#BC688F","RGB"))
# gradient3.move(200, 450)
# gradient3.setBorderWidth(0)  # No border
# gradient.add(gradient3)

# gradient4 = Rectangle(400, 400)
# gradient4.setFillColor(ImageColor.getcolor("#D75E88","RGB"))
# gradient4.move(200, 500)
# gradient4.setBorderWidth(0)  # No border
# gradient.add(gradient4)

# gradient5 = Rectangle(400, 400)
# gradient5.setFillColor(ImageColor.getcolor("#E54A79","RGB"))
# gradient5.move(200, 550)
# gradient5.setBorderWidth(0)  # No border
# gradient.add(gradient5)

# gradient6 = Rectangle(400, 400)
# gradient6.setFillColor(ImageColor.getcolor("#E54A79","RGB"))
# gradient6.move(200, 600)
# gradient6.setBorderWidth(0)  # No border
# gradient.add(gradient6)

# gradient7 = Rectangle(400, 400)
# gradient7.setFillColor(ImageColor.getcolor("#FEB87B","RGB"))
# gradient7.move(200, 550)
# gradient7.setBorderWidth(0)  # No border
# gradient.add(gradient7)

# gradient8 = Rectangle(400, 400)
# gradient8.setFillColor(ImageColor.getcolor("#FC713E","RGB"))
# gradient8.move(200, 600)
# gradient8.setBorderWidth(0)  # No border
# gradient.add(gradient8)

# paper.add(gradient)

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

paper.add(Star)





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
paper.add(Cloud1)

# Cloud1.shear(random.uniform(0.1, 0.5))

drawReferencePoints(paper)
drawGrid(paper, 100)
markClicks(paper)



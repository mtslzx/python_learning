from cs1graphics import *
# http://www.cs1graphics.org/
# Pixel Art , Train , Pinky Sunset , Counting stars , little bit dark sky , sun , sea , cloud, steam ...


canvas = Canvas(400, 600, (119,125,183), 'Midterm Exam')

# Background

# Clouds
cloud = Layer()



# Moon
moon = Layer()
# moon.add(Circle(50).setFillColor((137, 151, 149))) Didn't work right...

moon1 = Circle(30)
moon1.setFillColor((249,255,255))  # Bright side color of moon
moon1.setBorderWidth(0)  # No border
moon.add(moon1)  # Add to moon layer

moon2 = Circle(30)
moon2.setFillColor((119,125,183))  # Dark side color of moon
moon2.move(7.5,0)
moon2.setBorderWidth(0)  # No border
moon2.stretch(0.85, 1, )  # Shear to make moon look like a moon
moon.add(moon2)  # Add to moon layer


moon.rotate(-45)  # Rotate moon
moon.move(310, 60)  # Move moon to (100, 100)
moon.scale(0.7)  # Scale moon to 50%






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

# Train

# Steam



# Zoom in to train
# inside of train




# Add layer to canvas
canvas.add(gradient)
canvas.add(moon)

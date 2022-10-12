from cs1robots import *
create_world()
hubo = Robot()
hubo.set_trace("blue")
hubo.set_pause(0.1)
hubo.turn_left()
for i in range(5):
    for i in range(9):
        hubo.move()
    for i in range(3):
        hubo.turn_left()
    hubo.move()
    for i in range(3):
        hubo.turn_left()
    for i in range(9):
        hubo.move()
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()
    
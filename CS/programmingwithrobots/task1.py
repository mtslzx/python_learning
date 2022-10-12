from cs1robots import *

class Robot2(Robot):
    def turn_right(self):
        for i in range(3):
            self.turn_left()

    def move_n_times(self, n):
        for i in range(n):
            self.move()

create_world(7,7)
hubo = Robot2(orientation='N')
hubo.set_trace("blue")

for i in range(3):
    hubo.move_n_times(6)
    hubo.turn_right()
    hubo.move()
    hubo.turn_right()
    hubo.move_n_times(6)
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()
hubo.move_n_times(6)

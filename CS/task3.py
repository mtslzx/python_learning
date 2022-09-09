from cs1robots import *

class Robot2(Robot):
    def turn_right(self):
        for i in range(3):
            self.turn_left()

    def move_n_times(self, n):
        for i in range(n):
            self.move()
            
    def jump(self):
        self.turn_left()
        self.move()
        self.turn_right()
        self.move()
        self.turn_right()
        self.move()
        self.turn_left()
    
    def up_stair(self):
        self.move()
        self.turn_left()
        self.move()
        self.turn_right()
        self.move()
        
    def down_stair(self):
        self.move()
        self.turn_left()
        self.move()
        self.turn_right()
        self.move()

load_world("/Users/hailhwan/Code/python_learning/CS/worlds/newspaper.wld")
hubo = Robot2(orientation='E', beepers=1)
hubo.set_trace("blue")

for i in range(4):
    hubo.up_stair()
hubo.move()
hubo.turn_right()
hubo.turn_right()
hubo.move()
for i in range(4):
    hubo.down_stair()
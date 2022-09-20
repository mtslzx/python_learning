from threading import Thread
from cs1robots import *

class Robot2(Robot):
    def pick_if(self):
        if (self.on_beeper()):
            self.pick_beeper()
    
    def pick_while(self):
        while (self.on_beeper()):
            self.pick_beeper()
            
    def turn_right(self):
        for i in range(3):
            self.turn_left()
            
    def turn_around(self):
        self.turn_left()
        self.turn_left()

    def move_n_times(self, n):
        for i in range(n):
            self.move()
            
    def move_n_times_if(self, n):
        for i in range(n):
            self.move()
            self.pick_if()
            
    def move_n_times_while(self, n):
        for i in range(n):
            self.move()
            self.pick_while()
            
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

    def zigzag(self):
        self.move_n_times(6)
        self.turn_right()
        self.move()
        self.turn_right()
        self.move_n_times(6)
        self.turn_left()
        self.move()
        self.turn_left()
        
    def zigzag_if(self):
        self.pick_if()
        self.move_n_times_if(6)
        self.pick_if()
        self.turn_right()
        self.pick_if()
        self.move()
        self.pick_if()
        self.turn_right()
        self.pick_if()
        self.move_n_times_if(6)
        self.turn_left()
        self.pick_if()
        self.move()
        self.pick_if()
        self.turn_left()
        self.pick_if()
        
    def zigzag_while(self):
        self.pick_while()
        self.move_n_times_while(6)
        self.pick_while()
        self.turn_right()
        self.pick_while()
        self.move()
        self.pick_while()
        self.turn_right()
        self.pick_while()
        self.move_n_times_while(6)
        self.pick_while()
        self.turn_left()
        self.pick_while()
        self.move()
        self.pick_while()
        self.turn_left()
        self.pick_while()
        
    def deploy(self):
        while (self.carries_beepers()):
            self.drop_beeper()
        
    # def pick_beeper(self):
    #     return super().pick_beeper()
        

            
# Work with every worlds (trash1.wld , trash2.wld)

load_world("/Users/hailhwan/Code/python_learning/CS/worlds/trash2.wld")
hubo = Robot2()
hubo.set_trace("blue")

# Trash 1
hubo.move_n_times_while(9)  # goto end of the world
hubo.turn_around()
hubo.move_n_times_while(9)
hubo.turn_right()
hubo.move()
hubo.turn_around()
hubo.deploy()
hubo.move()

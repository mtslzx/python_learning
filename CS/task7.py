# from threading import Thread
from cs1robots import *

class UselessClass(object):
     @property
     def and_on(self):
         return self
     def forever(self):
         return "I can see into forever"

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
    
    def front_clear_pick(self):
        while(self.front_is_clear()):
            self.move()
            self.pick_while()
    
   
                
    def moving(self):  # Make Code Clear
        return(self)
    
    def and_on.when_left_blank_drop(self):  # Task 7
        while(self.front_is_clear()):
            self.move()
            if(not self.left_is_clear()):
                self.drop_beeper()
        
        


# Setup
load_world("/Users/hailhwan/Code/python_learning/CS/worlds/rain.wld")
hubo = Robot2(avenue=3, street=6, orientation='N', beepers=10)
hubo.set_trace("blue")

# Task
hu



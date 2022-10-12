# from threading import Thread
from cs1robots import *

class Robot2(Robot):
    def pick_if(self):
        if (self.on_beeper()):
            self.pick_beeper()
            
    def turn_right(self):
        for i in range(3):
            self.turn_left()

    def move_n_times(self, n):
        for i in range(n):
            self.move()
            
    def move_n_times_if(self, n):
        for i in range(n):
            self.pick_if()
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
        
    # def pick_beeper(self):
    #     return super().pick_beeper()
        

            
# if 조건으로 판별하는 경우 beeper가 2개 이상 있을 시 하나만 먹는다.
# while 조건으로 판별하는 경우 beeper가 2개 이상 있을 시 모두 먹는다.
# 이 코드에서 harvest2.wld를 월드로 불러올 경우 확인해 볼 수 있다.

load_world("/Users/hailhwan/Code/python_learning/CS/worlds/harvest1.wld")
hubo = Robot2(orientation='N')
hubo.set_trace("blue")

for i in range(3):  # zigzag 3 times
    hubo.zigzag_if()
hubo.move_n_times_if(6)  # goto end of the world
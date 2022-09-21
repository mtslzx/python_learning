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

    def move_n_times(self, n):
        for i in range(n):
            self.move()
            
    def move_n_times_if(self, n):
        for i in range(n):
            self.pick_if()
            self.move()
            
    def move_n_times_while(self, n):
        for i in range(n):
            self.pick_while()
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
        
    def zigzag_while(self):  # 이 코드 최적화 필요함.
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
        
    # def pick_beeper(self):
    #     return super().pick_beeper()
        

            
        

load_world("/Users/hailhwan/Code/python_learning/CS/worlds/harvest2.wld")
hubo = Robot2(orientation='N')
hubo.set_trace("blue")

# for i in range(3):  # zigzag 3 times
#     hubo.zigzag_while()
# hubo.move_n_times_while(6)  # goto end of the world

p1 = Thread()
p2 = Thread()

p1.join(target = hubo.zigzag())
p2.join(target = hubo.pick_while())



'''
pick
move
pick
move
pick
move


return?

list?

move -> Temp = T
if Temp == T:
pick

줍는건 줍는거대로 계속 줍게하고 (while pick.)
움직이는건 움직이는거대로 계속 움직이게하고 (move. move. move.)
동시에 돌리고 싶은데...


zigzag(), pick_while()을 동시에 돌리고 싶다~


'''
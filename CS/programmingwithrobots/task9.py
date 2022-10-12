# from threading import Thread
from cs1robots import *
import random


class Robot(Robot):
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
    
    def move_whenLeftBlank_drop(self):  # Task 7
        while(self.front_is_clear()):
            self.move()
            if(self.left_is_clear()):
                self.drop_beeper()
    
    def smart_hurdle(self):  # Task 8
        while(not self.on_beeper()):  # Beeper에 도달할 경우 While 중단.
            if(self.on_beeper()):  # 종료조건... 이거 없애버리고 싶은데
                return 0
            counter = 0
            while(self.front_is_clear()):  # Hurdle을 넘기 위해 앞으로 이동하며 벽을 만날 때 까지 이동.
                self.move()
                if(self.on_beeper()):  # 종료조건...
                    return 0
            self.turn_left()  # 벽을 만나면 왼쪽으로 회전.
            while(not self.right_is_clear()):  # 오른쪽에 벽이 있는동안 북쪽(위쪽)으로 이동.
                self.move()
                if(self.on_beeper()):  # 종료조건...
                    return 0
                counter += 1
            self.turn_right()  # 오른쪽에 벽이 없으면 오른쪽으로 회전.
            self.move()  # 오른쪽으로 한 칸 이동.
            self.turn_right()  # 오른쪽으로 회전.
            for i in range(counter):  # 벽을 만날 때 까지 이동했던 칸 수만큼 이동.
                self.move()
                if(self.on_beeper()):  # 종료조건...
                    return 0
            self.turn_left()  # 왼쪽으로 회전.
            
    def smart_zigzag(self):  # Task 9
        while(True):  # 함수가 종료될 때 까지 무한루프
            while(self.front_is_clear()):  # 전면에 벽이 나올때 까지 이동
                self.move()
            if(not self.right_is_clear()):  # 종료조건, 오른쪽에 벽이 없을경우 오른쪽으로 회전
                return 0
            self.turn_right()
            self.move()
            self.turn_right()
            while(self.front_is_clear()):  # 전면에 벽이 나올때 까지 이동
                self.move()
            if(not self.left_is_clear()):  # 종료조건, 왼쪽에 벽이 없을경우 왼쪽으로 회전
                return 0
            self.turn_left()
            self.move()
            self.turn_left()
            


        

# 같은 코드로 임의의 크기의 월드에서 동작해야하므로
# Setup 코드를 수정함.

# Setup
create_world(random.randrange(1, 20), random.randrange(1, 20))  # Create a random world
hubo = Robot(orientation='N')
hubo.set_trace("blue")

# Task
hubo.smart_zigzag()
